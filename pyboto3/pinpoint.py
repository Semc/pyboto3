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

def create_app(CreateApplicationRequest=None):
    """
    Creates or updates an app.
    See also: AWS API Documentation
    
    
    :example: response = client.create_app(
        CreateApplicationRequest={
            'Name': 'string'
        }
    )
    
    
    :type CreateApplicationRequest: dict
    :param CreateApplicationRequest: [REQUIRED] Application Request.
            Name (string) -- The display name of the application. Used in the Amazon Pinpoint console.
            

    :rtype: dict
    :return: {
        'ApplicationResponse': {
            'Id': 'string',
            'Name': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 201 response
    ApplicationResponse (dict) -- Application Response.
    Id (string) -- The unique application ID.
    Name (string) -- The display name of the application.
    
    
    
    
    
    """
    pass

def create_campaign(ApplicationId=None, WriteCampaignRequest=None):
    """
    Creates or updates a campaign.
    See also: AWS API Documentation
    
    
    :example: response = client.create_campaign(
        ApplicationId='string',
        WriteCampaignRequest={
            'AdditionalTreatments': [
                {
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'EventFilter': {
                            'Dimensions': {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'EventType': {
                                    'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                }
                            },
                            'FilterType': 'SYSTEM'|'ENDPOINT'
                        },
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'Description': 'string',
            'HoldoutPercent': 123,
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'IsPaused': True|False,
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'EventFilter': {
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'EventType': {
                            'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                            'Values': [
                                'string',
                            ]
                        },
                        'Metrics': {
                            'string': {
                                'ComparisonOperator': 'string',
                                'Value': 123.0
                            }
                        }
                    },
                    'FilterType': 'SYSTEM'|'ENDPOINT'
                },
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'TreatmentDescription': 'string',
            'TreatmentName': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type WriteCampaignRequest: dict
    :param WriteCampaignRequest: [REQUIRED] Used to create a campaign.
            AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
            (dict) -- Used to create a campaign treatment.
            MessageConfiguration (dict) -- The message configuration settings.
            ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            EmailMessage (dict) -- The email message configuration.
            Body (string) -- The email text body.
            FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
            HtmlBody (string) -- The email html body.
            Title (string) -- The email title (Or subject).
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The SMS message configuration.
            Body (string) -- The SMS text body.
            MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
            SenderId (string) -- Sender ID of sent message.
            
            Schedule (dict) -- The campaign schedule.
            EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
            EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
            Dimensions (dict) -- An object that defines the dimensions for the event filter.
            Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
            (string) --
            (dict) -- Custom metric dimension
            ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
            Value (float) -- The value to be compared.
            
            
            FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
            Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
            IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
            QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
            End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
            Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
            StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
            Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
            SizePercent (integer) -- The allocated percentage of users for this treatment.
            TreatmentDescription (string) -- A custom description for the treatment.
            TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
            
            Description (string) -- A description of the campaign.
            HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
            Hook (dict) -- Campaign hook information.
            LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
            Mode (string) -- What mode Lambda should be invoked in.
            WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
            IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
            Limits (dict) -- The campaign limits settings.
            Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
            MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
            MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
            Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
            MessageConfiguration (dict) -- The message configuration settings.
            ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            EmailMessage (dict) -- The email message configuration.
            Body (string) -- The email text body.
            FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
            HtmlBody (string) -- The email html body.
            Title (string) -- The email title (Or subject).
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The SMS message configuration.
            Body (string) -- The SMS text body.
            MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
            SenderId (string) -- Sender ID of sent message.
            
            Name (string) -- The custom name of the campaign.
            Schedule (dict) -- The campaign schedule.
            EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
            EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
            Dimensions (dict) -- An object that defines the dimensions for the event filter.
            Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
            (string) --
            (dict) -- Custom metric dimension
            ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
            Value (float) -- The value to be compared.
            
            
            FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
            Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
            IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
            QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
            End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
            Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
            StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
            Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
            SegmentId (string) -- The ID of the segment to which the campaign sends messages.
            SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
            TreatmentDescription (string) -- A custom description for the treatment.
            TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
            

    :rtype: dict
    :return: {
        'CampaignResponse': {
            'AdditionalTreatments': [
                {
                    'Id': 'string',
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'EventFilter': {
                            'Dimensions': {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'EventType': {
                                    'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                }
                            },
                            'FilterType': 'SYSTEM'|'ENDPOINT'
                        },
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultState': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
            },
            'Description': 'string',
            'HoldoutPercent': 123,
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'EventFilter': {
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'EventType': {
                            'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                            'Values': [
                                'string',
                            ]
                        },
                        'Metrics': {
                            'string': {
                                'ComparisonOperator': 'string',
                                'Value': 123.0
                            }
                        }
                    },
                    'FilterType': 'SYSTEM'|'ENDPOINT'
                },
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'State': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
            },
            'TreatmentDescription': 'string',
            'TreatmentName': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 201 response
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    
    """
    pass

def create_export_job(ApplicationId=None, ExportJobRequest=None):
    """
    Creates an export job.
    See also: AWS API Documentation
    
    
    :example: response = client.create_export_job(
        ApplicationId='string',
        ExportJobRequest={
            'RoleArn': 'string',
            'S3UrlPrefix': 'string',
            'SegmentId': 'string',
            'SegmentVersion': 123
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type ExportJobRequest: dict
    :param ExportJobRequest: [REQUIRED] Export job request.
            RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that endpoints will be exported to.
            S3UrlPrefix (string) -- A URL that points to the location within an Amazon S3 bucket that will receive the export. The location is typically a folder with multiple files. The URL should follow this format: s3://bucket-name/folder-name/ Amazon Pinpoint will export endpoints to this location.
            SegmentId (string) -- The ID of the segment to export endpoints from. If not present, Amazon Pinpoint exports all of the endpoints that belong to the application.
            SegmentVersion (integer) -- The version of the segment to export if specified.
            

    :rtype: dict
    :return: {
        'ExportJobResponse': {
            'ApplicationId': 'string',
            'CompletedPieces': 123,
            'CompletionDate': 'string',
            'CreationDate': 'string',
            'Definition': {
                'RoleArn': 'string',
                'S3UrlPrefix': 'string',
                'SegmentId': 'string',
                'SegmentVersion': 123
            },
            'FailedPieces': 123,
            'Failures': [
                'string',
            ],
            'Id': 'string',
            'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
            'TotalFailures': 123,
            'TotalPieces': 123,
            'TotalProcessed': 123,
            'Type': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 202 response
    ExportJobResponse (dict) -- Export job response.
    ApplicationId (string) -- The unique ID of the application associated with the export job.
    CompletedPieces (integer) -- The number of pieces that have successfully completed as of the time of the request.
    CompletionDate (string) -- The date the job completed in ISO 8601 format.
    CreationDate (string) -- The date the job was created in ISO 8601 format.
    Definition (dict) -- The export job settings.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that endpoints will be exported to.
    S3UrlPrefix (string) -- A URL that points to the location within an Amazon S3 bucket that will receive the export. The location is typically a folder with multiple files. The URL should follow this format: s3://bucket-name/folder-name/ Amazon Pinpoint will export endpoints to this location.
    SegmentId (string) -- The ID of the segment to export endpoints from. If not present, Amazon Pinpoint exports all of the endpoints that belong to the application.
    SegmentVersion (integer) -- The version of the segment to export if specified.
    
    
    FailedPieces (integer) -- The number of pieces that failed to be processed as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the job.
    JobStatus (string) -- The status of the job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed.
    TotalFailures (integer) -- The number of endpoints that were not processed; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be processed to finish the job. Each piece is an approximately equal portion of the endpoints.
    TotalProcessed (integer) -- The number of endpoints that were processed by the job.
    Type (string) -- The job type. Will be 'EXPORT'.
    
    
    
    
    
    """
    pass

def create_import_job(ApplicationId=None, ImportJobRequest=None):
    """
    Creates or updates an import job.
    See also: AWS API Documentation
    
    
    :example: response = client.create_import_job(
        ApplicationId='string',
        ImportJobRequest={
            'DefineSegment': True|False,
            'ExternalId': 'string',
            'Format': 'CSV'|'JSON',
            'RegisterEndpoints': True|False,
            'RoleArn': 'string',
            'S3Url': 'string',
            'SegmentId': 'string',
            'SegmentName': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type ImportJobRequest: dict
    :param ImportJobRequest: [REQUIRED] Import job request.
            DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
            ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
            Format (string) -- The format of the files that contain the endpoint definitions. Valid values: CSV, JSON
            RegisterEndpoints (boolean) -- Sets whether the endpoints are registered with Amazon Pinpoint when they are imported.
            RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that contains the endpoints to import.
            S3Url (string) -- The URL of the S3 bucket that contains the segment information to import. The location can be a folder or a single file. The URL should use the following format: s3://bucket-name/folder-name/file-name Amazon Pinpoint imports endpoints from this location and any subfolders it contains.
            SegmentId (string) -- The ID of the segment to update if the import job is meant to update an existing segment.
            SegmentName (string) -- A custom name for the segment created by the import job. Use if DefineSegment is true.
            

    :rtype: dict
    :return: {
        'ImportJobResponse': {
            'ApplicationId': 'string',
            'CompletedPieces': 123,
            'CompletionDate': 'string',
            'CreationDate': 'string',
            'Definition': {
                'DefineSegment': True|False,
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RegisterEndpoints': True|False,
                'RoleArn': 'string',
                'S3Url': 'string',
                'SegmentId': 'string',
                'SegmentName': 'string'
            },
            'FailedPieces': 123,
            'Failures': [
                'string',
            ],
            'Id': 'string',
            'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
            'TotalFailures': 123,
            'TotalPieces': 123,
            'TotalProcessed': 123,
            'Type': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 201 response
    ImportJobResponse (dict) -- Import job response.
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the files that contain the endpoint definitions. Valid values: CSV, JSON
    RegisterEndpoints (boolean) -- Sets whether the endpoints are registered with Amazon Pinpoint when they are imported.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that contains the endpoints to import.
    S3Url (string) -- The URL of the S3 bucket that contains the segment information to import. The location can be a folder or a single file. The URL should use the following format: s3://bucket-name/folder-name/file-name Amazon Pinpoint imports endpoints from this location and any subfolders it contains.
    SegmentId (string) -- The ID of the segment to update if the import job is meant to update an existing segment.
    SegmentName (string) -- A custom name for the segment created by the import job. Use if DefineSegment is true.
    
    
    FailedPieces (integer) -- The number of pieces that have failed to import as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the import job.
    JobStatus (string) -- The status of the import job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed to import.
    TotalFailures (integer) -- The number of endpoints that failed to import; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be imported to finish the job. Each piece is an approximately equal portion of the endpoints to import.
    TotalProcessed (integer) -- The number of endpoints that were processed by the import job.
    Type (string) -- The job type. Will be Import.
    
    
    
    
    
    """
    pass

def create_segment(ApplicationId=None, WriteSegmentRequest=None):
    """
    Used to create or update a segment.
    See also: AWS API Documentation
    
    
    :example: response = client.create_segment(
        ApplicationId='string',
        WriteSegmentRequest={
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Channel': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'GPSPoint': {
                        'Coordinates': {
                            'Latitude': 123.0,
                            'Longitude': 123.0
                        },
                        'RangeInKilometers': 123.0
                    }
                },
                'Metrics': {
                    'string': {
                        'ComparisonOperator': 'string',
                        'Value': 123.0
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Name': 'string',
            'SegmentGroups': {
                'Groups': [
                    {
                        'Dimensions': [
                            {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Behavior': {
                                    'Recency': {
                                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                        'RecencyType': 'ACTIVE'|'INACTIVE'
                                    }
                                },
                                'Demographic': {
                                    'AppVersion': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Channel': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'DeviceType': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Make': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Model': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Platform': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Location': {
                                    'Country': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'GPSPoint': {
                                        'Coordinates': {
                                            'Latitude': 123.0,
                                            'Longitude': 123.0
                                        },
                                        'RangeInKilometers': 123.0
                                    }
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                },
                                'UserAttributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                }
                            },
                        ],
                        'SourceSegments': [
                            {
                                'Id': 'string',
                                'Version': 123
                            },
                        ],
                        'SourceType': 'ALL'|'ANY'|'NONE',
                        'Type': 'ALL'|'ANY'|'NONE'
                    },
                ],
                'Include': 'ALL'|'ANY'|'NONE'
            }
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type WriteSegmentRequest: dict
    :param WriteSegmentRequest: [REQUIRED] Segment definition.
            Dimensions (dict) -- The segment dimensions attributes.
            Attributes (dict) -- Custom segment attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Behavior (dict) -- The segment behaviors attributes.
            Recency (dict) -- The recency of use.
            Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
            RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
            
            Demographic (dict) -- The segment demographics attributes.
            AppVersion (dict) -- The app version criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Channel (dict) -- The channel criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            DeviceType (dict) -- The device type criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Make (dict) -- The device make criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Model (dict) -- The device model criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Platform (dict) -- The device platform criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Location (dict) -- The segment location attributes.
            Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            GPSPoint (dict) -- The GPS Point dimension.
            Coordinates (dict) -- Coordinate to measure distance from.
            Latitude (float) -- Latitude
            Longitude (float) -- Longitude
            RangeInKilometers (float) -- Range in kilometers from the coordinate.
            
            Metrics (dict) -- Custom segment metrics.
            (string) --
            (dict) -- Custom metric dimension
            ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
            Value (float) -- The value to be compared.
            
            UserAttributes (dict) -- Custom segment user attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Name (string) -- The name of segment
            SegmentGroups (dict) -- A segment group, which consists of zero or more source segments, plus dimensions that are applied to those source segments. Your request can only include one segment group. Your request can include either a SegmentGroups object or a Dimensions object, but not both.
            Groups (list) -- A set of segment criteria to evaluate.
            (dict) -- Segment group definition.
            Dimensions (list) -- List of dimensions to include or exclude.
            (dict) -- Segment dimensions
            Attributes (dict) -- Custom segment attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Behavior (dict) -- The segment behaviors attributes.
            Recency (dict) -- The recency of use.
            Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
            RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
            
            Demographic (dict) -- The segment demographics attributes.
            AppVersion (dict) -- The app version criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Channel (dict) -- The channel criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            DeviceType (dict) -- The device type criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Make (dict) -- The device make criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Model (dict) -- The device model criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Platform (dict) -- The device platform criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Location (dict) -- The segment location attributes.
            Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            GPSPoint (dict) -- The GPS Point dimension.
            Coordinates (dict) -- Coordinate to measure distance from.
            Latitude (float) -- Latitude
            Longitude (float) -- Longitude
            RangeInKilometers (float) -- Range in kilometers from the coordinate.
            
            Metrics (dict) -- Custom segment metrics.
            (string) --
            (dict) -- Custom metric dimension
            ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
            Value (float) -- The value to be compared.
            
            UserAttributes (dict) -- Custom segment user attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            
            SourceSegments (list) -- The base segment that you build your segment on. The source segment defines the starting 'universe' of endpoints. When you add dimensions to the segment, it filters the source segment based on the dimensions that you specify. You can specify more than one dimensional segment. You can only specify one imported segment. NOTE: If you specify an imported segment for this attribute, the segment size estimate that appears in the Amazon Pinpoint console shows the size of the imported segment, without any filters applied to it.
            (dict) -- Segment reference.
            Id (string) -- A unique identifier for the segment.
            Version (integer) -- If specified contains a specific version of the segment included.
            
            SourceType (string) -- Specify how to handle multiple source segments. For example, if you specify three source segments, should the resulting segment be based on any or all of the segments? Acceptable values: ANY or ALL.
            Type (string) -- Specify how to handle multiple segment dimensions. For example, if you specify three dimensions, should the resulting segment include endpoints that are matched by all, any, or none of the dimensions? Acceptable values: ALL, ANY, or NONE.
            
            Include (string) -- Specify how to handle multiple segment groups. For example, if the segment includes three segment groups, should the resulting segment include endpoints that are matched by all, any, or none of the segment groups you created. Acceptable values: ALL, ANY, or NONE.
            

    :rtype: dict
    :return: {
        'SegmentResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Channel': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'GPSPoint': {
                        'Coordinates': {
                            'Latitude': 123.0,
                            'Longitude': 123.0
                        },
                        'RangeInKilometers': 123.0
                    }
                },
                'Metrics': {
                    'string': {
                        'ComparisonOperator': 'string',
                        'Value': 123.0
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Id': 'string',
            'ImportDefinition': {
                'ChannelCounts': {
                    'string': 123
                },
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RoleArn': 'string',
                'S3Url': 'string',
                'Size': 123
            },
            'LastModifiedDate': 'string',
            'Name': 'string',
            'SegmentGroups': {
                'Groups': [
                    {
                        'Dimensions': [
                            {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Behavior': {
                                    'Recency': {
                                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                        'RecencyType': 'ACTIVE'|'INACTIVE'
                                    }
                                },
                                'Demographic': {
                                    'AppVersion': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Channel': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'DeviceType': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Make': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Model': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Platform': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Location': {
                                    'Country': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'GPSPoint': {
                                        'Coordinates': {
                                            'Latitude': 123.0,
                                            'Longitude': 123.0
                                        },
                                        'RangeInKilometers': 123.0
                                    }
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                },
                                'UserAttributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                }
                            },
                        ],
                        'SourceSegments': [
                            {
                                'Id': 'string',
                                'Version': 123
                            },
                        ],
                        'SourceType': 'ALL'|'ANY'|'NONE',
                        'Type': 'ALL'|'ANY'|'NONE'
                    },
                ],
                'Include': 'ALL'|'ANY'|'NONE'
            },
            'SegmentType': 'DIMENSIONAL'|'IMPORT',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 201 response
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application that the segment applies to.
    CreationDate (string) -- The date and time when the segment was created.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- The number of channel types in the imported segment.
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- The URL of the S3 bucket that the segment was imported from.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date and time when the segment was last modified.
    Name (string) -- The name of the segment.
    SegmentGroups (dict) -- A segment group, which consists of zero or more source segments, plus dimensions that are applied to those source segments.
    Groups (list) -- A set of segment criteria to evaluate.
    (dict) -- Segment group definition.
    Dimensions (list) -- List of dimensions to include or exclude.
    (dict) -- Segment dimensions
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    
    SourceSegments (list) -- The base segment that you build your segment on. The source segment defines the starting "universe" of endpoints. When you add dimensions to the segment, it filters the source segment based on the dimensions that you specify. You can specify more than one dimensional segment. You can only specify one imported segment. NOTE: If you specify an imported segment for this attribute, the segment size estimate that appears in the Amazon Pinpoint console shows the size of the imported segment, without any filters applied to it.
    (dict) -- Segment reference.
    Id (string) -- A unique identifier for the segment.
    Version (integer) -- If specified contains a specific version of the segment included.
    
    
    
    
    SourceType (string) -- Specify how to handle multiple source segments. For example, if you specify three source segments, should the resulting segment be based on any or all of the segments? Acceptable values: ANY or ALL.
    Type (string) -- Specify how to handle multiple segment dimensions. For example, if you specify three dimensions, should the resulting segment include endpoints that are matched by all, any, or none of the dimensions? Acceptable values: ALL, ANY, or NONE.
    
    
    
    
    Include (string) -- Specify how to handle multiple segment groups. For example, if the segment includes three segment groups, should the resulting segment include endpoints that are matched by all, any, or none of the segment groups you created. Acceptable values: ALL, ANY, or NONE.
    
    
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def delete_adm_channel(ApplicationId=None):
    """
    Delete an ADM channel.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_adm_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'ADMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_apns_channel(ApplicationId=None):
    """
    Deletes the APNs channel for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_apns_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_apns_sandbox_channel(ApplicationId=None):
    """
    Delete an APNS sandbox channel.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_apns_sandbox_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_apns_voip_channel(ApplicationId=None):
    """
    Delete an APNS VoIP channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_apns_voip_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSVoipChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_apns_voip_sandbox_channel(ApplicationId=None):
    """
    Delete an APNS VoIP sandbox channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_apns_voip_sandbox_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSVoipSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_app(ApplicationId=None):
    """
    Deletes an app.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_app(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'ApplicationResponse': {
            'Id': 'string',
            'Name': 'string'
        }
    }
    
    
    """
    pass

def delete_baidu_channel(ApplicationId=None):
    """
    Delete a BAIDU GCM channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_baidu_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'BaiduChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_campaign(ApplicationId=None, CampaignId=None):
    """
    Deletes a campaign.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_campaign(
        ApplicationId='string',
        CampaignId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type CampaignId: string
    :param CampaignId: [REQUIRED] The unique ID of the campaign.

    :rtype: dict
    :return: {
        'CampaignResponse': {
            'AdditionalTreatments': [
                {
                    'Id': 'string',
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'EventFilter': {
                            'Dimensions': {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'EventType': {
                                    'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                }
                            },
                            'FilterType': 'SYSTEM'|'ENDPOINT'
                        },
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultState': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
            },
            'Description': 'string',
            'HoldoutPercent': 123,
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'EventFilter': {
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'EventType': {
                            'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                            'Values': [
                                'string',
                            ]
                        },
                        'Metrics': {
                            'string': {
                                'ComparisonOperator': 'string',
                                'Value': 123.0
                            }
                        }
                    },
                    'FilterType': 'SYSTEM'|'ENDPOINT'
                },
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'State': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
            },
            'TreatmentDescription': 'string',
            'TreatmentName': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    
    """
    pass

def delete_email_channel(ApplicationId=None):
    """
    Delete an email channel.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_email_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'EmailChannelResponse': {
            'ApplicationId': 'string',
            'ConfigurationSet': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'FromAddress': 'string',
            'HasCredential': True|False,
            'Id': 'string',
            'Identity': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'MessagesPerSecond': 123,
            'Platform': 'string',
            'RoleArn': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_endpoint(ApplicationId=None, EndpointId=None):
    """
    Deletes an endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_endpoint(
        ApplicationId='string',
        EndpointId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type EndpointId: string
    :param EndpointId: [REQUIRED] The unique ID of the endpoint.

    :rtype: dict
    :return: {
        'EndpointResponse': {
            'Address': 'string',
            'ApplicationId': 'string',
            'Attributes': {
                'string': [
                    'string',
                ]
            },
            'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'VOICE'|'EMAIL'|'BAIDU'|'CUSTOM',
            'CohortId': 'string',
            'CreationDate': 'string',
            'Demographic': {
                'AppVersion': 'string',
                'Locale': 'string',
                'Make': 'string',
                'Model': 'string',
                'ModelVersion': 'string',
                'Platform': 'string',
                'PlatformVersion': 'string',
                'Timezone': 'string'
            },
            'EffectiveDate': 'string',
            'EndpointStatus': 'string',
            'Id': 'string',
            'Location': {
                'City': 'string',
                'Country': 'string',
                'Latitude': 123.0,
                'Longitude': 123.0,
                'PostalCode': 'string',
                'Region': 'string'
            },
            'Metrics': {
                'string': 123.0
            },
            'OptOut': 'string',
            'RequestId': 'string',
            'User': {
                'UserAttributes': {
                    'string': [
                        'string',
                    ]
                },
                'UserId': 'string'
            }
        }
    }
    
    
    :returns: 
    (dict) -- 202 response
    EndpointResponse (dict) -- Endpoint response
    Address (string) -- The address of the endpoint as provided by your push provider. For example, the DeviceToken or RegistrationId.
    ApplicationId (string) -- The ID of the application that is associated with the endpoint.
    Attributes (dict) -- Custom attributes that describe the endpoint by associating a name with an array of values. For example, an attribute named "interests" might have the following values: ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    CohortId (string) -- A number from 0-99 that represents the cohort the endpoint is assigned to. Endpoints are grouped into cohorts randomly, and each cohort contains approximately 1 percent of the endpoints for an app. Amazon Pinpoint assigns cohorts to the holdout or treatment allocations for a campaign.
    CreationDate (string) -- The date and time when the endpoint was created, shown in ISO 8601 format.
    Demographic (dict) -- The endpoint demographic attributes.
    AppVersion (string) -- The version of the application associated with the endpoint.
    Locale (string) -- The endpoint locale in the following format: The ISO 639-1 alpha-2 code, followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
    Make (string) -- The manufacturer of the endpoint device, such as Apple or Samsung.
    Model (string) -- The model name or number of the endpoint device, such as iPhone.
    ModelVersion (string) -- The model version of the endpoint device.
    Platform (string) -- The platform of the endpoint device, such as iOS or Android.
    PlatformVersion (string) -- The platform version of the endpoint device.
    Timezone (string) -- The timezone of the endpoint. Specified as a tz database value, such as Americas/Los_Angeles.
    
    
    EffectiveDate (string) -- The date and time when the endpoint was last updated, shown in ISO 8601 format.
    EndpointStatus (string) -- Unused.
    Id (string) -- The unique ID that you assigned to the endpoint. The ID should be a globally unique identifier (GUID) to ensure that it doesn't conflict with other endpoint IDs associated with the application.
    Location (dict) -- The endpoint location attributes.
    City (string) -- The city where the endpoint is located.
    Country (string) -- The two-letter code for the country or region of the endpoint. Specified as an ISO 3166-1 alpha-2 code, such as "US" for the United States.
    Latitude (float) -- The latitude of the endpoint location, rounded to one decimal place.
    Longitude (float) -- The longitude of the endpoint location, rounded to one decimal place.
    PostalCode (string) -- The postal code or zip code of the endpoint.
    Region (string) -- The region of the endpoint location. For example, in the United States, this corresponds to a state.
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint.
    (string) --
    (float) --
    
    
    
    
    OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
    RequestId (string) -- The unique ID for the most recent request to update the endpoint.
    User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
    UserAttributes (dict) -- Custom attributes that describe the user by associating a name with an array of values. For example, an attribute named "interests" might have the following values: ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    UserId (string) -- The unique ID of the user.
    
    
    
    
    
    
    
    """
    pass

def delete_event_stream(ApplicationId=None):
    """
    Deletes the event stream for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_event_stream(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'EventStream': {
            'ApplicationId': 'string',
            'DestinationStreamArn': 'string',
            'ExternalId': 'string',
            'LastModifiedDate': 'string',
            'LastUpdatedBy': 'string',
            'RoleArn': 'string'
        }
    }
    
    
    """
    pass

def delete_gcm_channel(ApplicationId=None):
    """
    Deletes the GCM channel for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_gcm_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'GCMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_segment(ApplicationId=None, SegmentId=None):
    """
    Deletes a segment.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_segment(
        ApplicationId='string',
        SegmentId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type SegmentId: string
    :param SegmentId: [REQUIRED] The unique ID of the segment.

    :rtype: dict
    :return: {
        'SegmentResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Channel': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'GPSPoint': {
                        'Coordinates': {
                            'Latitude': 123.0,
                            'Longitude': 123.0
                        },
                        'RangeInKilometers': 123.0
                    }
                },
                'Metrics': {
                    'string': {
                        'ComparisonOperator': 'string',
                        'Value': 123.0
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Id': 'string',
            'ImportDefinition': {
                'ChannelCounts': {
                    'string': 123
                },
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RoleArn': 'string',
                'S3Url': 'string',
                'Size': 123
            },
            'LastModifiedDate': 'string',
            'Name': 'string',
            'SegmentGroups': {
                'Groups': [
                    {
                        'Dimensions': [
                            {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Behavior': {
                                    'Recency': {
                                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                        'RecencyType': 'ACTIVE'|'INACTIVE'
                                    }
                                },
                                'Demographic': {
                                    'AppVersion': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Channel': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'DeviceType': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Make': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Model': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Platform': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Location': {
                                    'Country': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'GPSPoint': {
                                        'Coordinates': {
                                            'Latitude': 123.0,
                                            'Longitude': 123.0
                                        },
                                        'RangeInKilometers': 123.0
                                    }
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                },
                                'UserAttributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                }
                            },
                        ],
                        'SourceSegments': [
                            {
                                'Id': 'string',
                                'Version': 123
                            },
                        ],
                        'SourceType': 'ALL'|'ANY'|'NONE',
                        'Type': 'ALL'|'ANY'|'NONE'
                    },
                ],
                'Include': 'ALL'|'ANY'|'NONE'
            },
            'SegmentType': 'DIMENSIONAL'|'IMPORT',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application that the segment applies to.
    CreationDate (string) -- The date and time when the segment was created.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- The number of channel types in the imported segment.
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- The URL of the S3 bucket that the segment was imported from.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date and time when the segment was last modified.
    Name (string) -- The name of the segment.
    SegmentGroups (dict) -- A segment group, which consists of zero or more source segments, plus dimensions that are applied to those source segments.
    Groups (list) -- A set of segment criteria to evaluate.
    (dict) -- Segment group definition.
    Dimensions (list) -- List of dimensions to include or exclude.
    (dict) -- Segment dimensions
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    
    SourceSegments (list) -- The base segment that you build your segment on. The source segment defines the starting "universe" of endpoints. When you add dimensions to the segment, it filters the source segment based on the dimensions that you specify. You can specify more than one dimensional segment. You can only specify one imported segment. NOTE: If you specify an imported segment for this attribute, the segment size estimate that appears in the Amazon Pinpoint console shows the size of the imported segment, without any filters applied to it.
    (dict) -- Segment reference.
    Id (string) -- A unique identifier for the segment.
    Version (integer) -- If specified contains a specific version of the segment included.
    
    
    
    
    SourceType (string) -- Specify how to handle multiple source segments. For example, if you specify three source segments, should the resulting segment be based on any or all of the segments? Acceptable values: ANY or ALL.
    Type (string) -- Specify how to handle multiple segment dimensions. For example, if you specify three dimensions, should the resulting segment include endpoints that are matched by all, any, or none of the dimensions? Acceptable values: ALL, ANY, or NONE.
    
    
    
    
    Include (string) -- Specify how to handle multiple segment groups. For example, if the segment includes three segment groups, should the resulting segment include endpoints that are matched by all, any, or none of the segment groups you created. Acceptable values: ALL, ANY, or NONE.
    
    
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def delete_sms_channel(ApplicationId=None):
    """
    Delete an SMS channel.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_sms_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'SMSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'PromotionalMessagesPerSecond': 123,
            'SenderId': 'string',
            'ShortCode': 'string',
            'TransactionalMessagesPerSecond': 123,
            'Version': 123
        }
    }
    
    
    """
    pass

def delete_user_endpoints(ApplicationId=None, UserId=None):
    """
    Deletes endpoints that are associated with a User ID.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user_endpoints(
        ApplicationId='string',
        UserId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type UserId: string
    :param UserId: [REQUIRED] The unique ID of the user.

    :rtype: dict
    :return: {
        'EndpointsResponse': {
            'Item': [
                {
                    'Address': 'string',
                    'ApplicationId': 'string',
                    'Attributes': {
                        'string': [
                            'string',
                        ]
                    },
                    'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'VOICE'|'EMAIL'|'BAIDU'|'CUSTOM',
                    'CohortId': 'string',
                    'CreationDate': 'string',
                    'Demographic': {
                        'AppVersion': 'string',
                        'Locale': 'string',
                        'Make': 'string',
                        'Model': 'string',
                        'ModelVersion': 'string',
                        'Platform': 'string',
                        'PlatformVersion': 'string',
                        'Timezone': 'string'
                    },
                    'EffectiveDate': 'string',
                    'EndpointStatus': 'string',
                    'Id': 'string',
                    'Location': {
                        'City': 'string',
                        'Country': 'string',
                        'Latitude': 123.0,
                        'Longitude': 123.0,
                        'PostalCode': 'string',
                        'Region': 'string'
                    },
                    'Metrics': {
                        'string': 123.0
                    },
                    'OptOut': 'string',
                    'RequestId': 'string',
                    'User': {
                        'UserAttributes': {
                            'string': [
                                'string',
                            ]
                        },
                        'UserId': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    (dict) -- 202 response
    EndpointsResponse (dict) -- List of endpoints
    Item (list) -- The list of endpoints.
    (dict) -- Endpoint response
    Address (string) -- The address of the endpoint as provided by your push provider. For example, the DeviceToken or RegistrationId.
    ApplicationId (string) -- The ID of the application that is associated with the endpoint.
    Attributes (dict) -- Custom attributes that describe the endpoint by associating a name with an array of values. For example, an attribute named "interests" might have the following values: ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    CohortId (string) -- A number from 0-99 that represents the cohort the endpoint is assigned to. Endpoints are grouped into cohorts randomly, and each cohort contains approximately 1 percent of the endpoints for an app. Amazon Pinpoint assigns cohorts to the holdout or treatment allocations for a campaign.
    CreationDate (string) -- The date and time when the endpoint was created, shown in ISO 8601 format.
    Demographic (dict) -- The endpoint demographic attributes.
    AppVersion (string) -- The version of the application associated with the endpoint.
    Locale (string) -- The endpoint locale in the following format: The ISO 639-1 alpha-2 code, followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
    Make (string) -- The manufacturer of the endpoint device, such as Apple or Samsung.
    Model (string) -- The model name or number of the endpoint device, such as iPhone.
    ModelVersion (string) -- The model version of the endpoint device.
    Platform (string) -- The platform of the endpoint device, such as iOS or Android.
    PlatformVersion (string) -- The platform version of the endpoint device.
    Timezone (string) -- The timezone of the endpoint. Specified as a tz database value, such as Americas/Los_Angeles.
    
    
    EffectiveDate (string) -- The date and time when the endpoint was last updated, shown in ISO 8601 format.
    EndpointStatus (string) -- Unused.
    Id (string) -- The unique ID that you assigned to the endpoint. The ID should be a globally unique identifier (GUID) to ensure that it doesn't conflict with other endpoint IDs associated with the application.
    Location (dict) -- The endpoint location attributes.
    City (string) -- The city where the endpoint is located.
    Country (string) -- The two-letter code for the country or region of the endpoint. Specified as an ISO 3166-1 alpha-2 code, such as "US" for the United States.
    Latitude (float) -- The latitude of the endpoint location, rounded to one decimal place.
    Longitude (float) -- The longitude of the endpoint location, rounded to one decimal place.
    PostalCode (string) -- The postal code or zip code of the endpoint.
    Region (string) -- The region of the endpoint location. For example, in the United States, this corresponds to a state.
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint.
    (string) --
    (float) --
    
    
    
    
    OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
    RequestId (string) -- The unique ID for the most recent request to update the endpoint.
    User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
    UserAttributes (dict) -- Custom attributes that describe the user by associating a name with an array of values. For example, an attribute named "interests" might have the following values: ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    UserId (string) -- The unique ID of the user.
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def delete_voice_channel(ApplicationId=None):
    """
    Delete an Voice channel
    See also: AWS API Documentation
    
    
    :example: response = client.delete_voice_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'VoiceChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
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

def get_adm_channel(ApplicationId=None):
    """
    Get an ADM channel.
    See also: AWS API Documentation
    
    
    :example: response = client.get_adm_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'ADMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_apns_channel(ApplicationId=None):
    """
    Returns information about the APNs channel for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.get_apns_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_apns_sandbox_channel(ApplicationId=None):
    """
    Get an APNS sandbox channel.
    See also: AWS API Documentation
    
    
    :example: response = client.get_apns_sandbox_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_apns_voip_channel(ApplicationId=None):
    """
    Get an APNS VoIP channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_apns_voip_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSVoipChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_apns_voip_sandbox_channel(ApplicationId=None):
    """
    Get an APNS VoIPSandbox channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_apns_voip_sandbox_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSVoipSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_app(ApplicationId=None):
    """
    Returns information about an app.
    See also: AWS API Documentation
    
    
    :example: response = client.get_app(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'ApplicationResponse': {
            'Id': 'string',
            'Name': 'string'
        }
    }
    
    
    """
    pass

def get_application_settings(ApplicationId=None):
    """
    Used to request the settings for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.get_application_settings(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'ApplicationSettingsResource': {
            'ApplicationId': 'string',
            'CampaignHook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'QuietTime': {
                'End': 'string',
                'Start': 'string'
            }
        }
    }
    
    
    """
    pass

def get_apps(PageSize=None, Token=None):
    """
    Returns information about your apps.
    See also: AWS API Documentation
    
    
    :example: response = client.get_apps(
        PageSize='string',
        Token='string'
    )
    
    
    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ApplicationsResponse': {
            'Item': [
                {
                    'Id': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ApplicationsResponse (dict) -- Get Applications Result.
    Item (list) -- List of applications returned in this page.
    (dict) -- Application Response.
    Id (string) -- The unique application ID.
    Name (string) -- The display name of the application.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_baidu_channel(ApplicationId=None):
    """
    Get a BAIDU GCM channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_baidu_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'BaiduChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_campaign(ApplicationId=None, CampaignId=None):
    """
    Returns information about a campaign.
    See also: AWS API Documentation
    
    
    :example: response = client.get_campaign(
        ApplicationId='string',
        CampaignId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type CampaignId: string
    :param CampaignId: [REQUIRED] The unique ID of the campaign.

    :rtype: dict
    :return: {
        'CampaignResponse': {
            'AdditionalTreatments': [
                {
                    'Id': 'string',
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'EventFilter': {
                            'Dimensions': {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'EventType': {
                                    'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                }
                            },
                            'FilterType': 'SYSTEM'|'ENDPOINT'
                        },
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultState': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
            },
            'Description': 'string',
            'HoldoutPercent': 123,
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'EventFilter': {
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'EventType': {
                            'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                            'Values': [
                                'string',
                            ]
                        },
                        'Metrics': {
                            'string': {
                                'ComparisonOperator': 'string',
                                'Value': 123.0
                            }
                        }
                    },
                    'FilterType': 'SYSTEM'|'ENDPOINT'
                },
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'State': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
            },
            'TreatmentDescription': 'string',
            'TreatmentName': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    
    """
    pass

def get_campaign_activities(ApplicationId=None, CampaignId=None, PageSize=None, Token=None):
    """
    Returns information about the activity performed by a campaign.
    See also: AWS API Documentation
    
    
    :example: response = client.get_campaign_activities(
        ApplicationId='string',
        CampaignId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type CampaignId: string
    :param CampaignId: [REQUIRED] The unique ID of the campaign.

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ActivitiesResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CampaignId': 'string',
                    'End': 'string',
                    'Id': 'string',
                    'Result': 'string',
                    'ScheduledStart': 'string',
                    'Start': 'string',
                    'State': 'string',
                    'SuccessfulEndpointCount': 123,
                    'TimezonesCompletedCount': 123,
                    'TimezonesTotalCount': 123,
                    'TotalEndpointCount': 123,
                    'TreatmentId': 'string'
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ActivitiesResponse (dict) -- Activities for campaign.
    Item (list) -- List of campaign activities
    (dict) -- Activity definition
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CampaignId (string) -- The ID of the campaign to which the activity applies.
    End (string) -- The actual time the activity was marked CANCELLED or COMPLETED. Provided in ISO 8601 format.
    Id (string) -- The unique activity ID.
    Result (string) -- Indicates whether the activity succeeded. Valid values: SUCCESS, FAIL
    ScheduledStart (string) -- The scheduled start time for the activity in ISO 8601 format.
    Start (string) -- The actual start time of the activity in ISO 8601 format.
    State (string) -- The state of the activity. Valid values: PENDING, INITIALIZING, RUNNING, PAUSED, CANCELLED, COMPLETED
    SuccessfulEndpointCount (integer) -- The total number of endpoints to which the campaign successfully delivered messages.
    TimezonesCompletedCount (integer) -- The total number of timezones completed.
    TimezonesTotalCount (integer) -- The total number of unique timezones present in the segment.
    TotalEndpointCount (integer) -- The total number of endpoints to which the campaign attempts to deliver messages.
    TreatmentId (string) -- The ID of a variation of the campaign used for A/B testing.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_campaign_version(ApplicationId=None, CampaignId=None, Version=None):
    """
    Returns information about a specific version of a campaign.
    See also: AWS API Documentation
    
    
    :example: response = client.get_campaign_version(
        ApplicationId='string',
        CampaignId='string',
        Version='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type CampaignId: string
    :param CampaignId: [REQUIRED] The unique ID of the campaign.

    :type Version: string
    :param Version: [REQUIRED] The version of the campaign.

    :rtype: dict
    :return: {
        'CampaignResponse': {
            'AdditionalTreatments': [
                {
                    'Id': 'string',
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'EventFilter': {
                            'Dimensions': {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'EventType': {
                                    'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                }
                            },
                            'FilterType': 'SYSTEM'|'ENDPOINT'
                        },
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultState': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
            },
            'Description': 'string',
            'HoldoutPercent': 123,
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'EventFilter': {
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'EventType': {
                            'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                            'Values': [
                                'string',
                            ]
                        },
                        'Metrics': {
                            'string': {
                                'ComparisonOperator': 'string',
                                'Value': 123.0
                            }
                        }
                    },
                    'FilterType': 'SYSTEM'|'ENDPOINT'
                },
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'State': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
            },
            'TreatmentDescription': 'string',
            'TreatmentName': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    
    """
    pass

def get_campaign_versions(ApplicationId=None, CampaignId=None, PageSize=None, Token=None):
    """
    Returns information about your campaign versions.
    See also: AWS API Documentation
    
    
    :example: response = client.get_campaign_versions(
        ApplicationId='string',
        CampaignId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type CampaignId: string
    :param CampaignId: [REQUIRED] The unique ID of the campaign.

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'CampaignsResponse': {
            'Item': [
                {
                    'AdditionalTreatments': [
                        {
                            'Id': 'string',
                            'MessageConfiguration': {
                                'ADMMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'TimeToLive': 123,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'APNSMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'TimeToLive': 123,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'BaiduMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'TimeToLive': 123,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'DefaultMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'TimeToLive': 123,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'EmailMessage': {
                                    'Body': 'string',
                                    'FromAddress': 'string',
                                    'HtmlBody': 'string',
                                    'Title': 'string'
                                },
                                'GCMMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'TimeToLive': 123,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'SMSMessage': {
                                    'Body': 'string',
                                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                                    'SenderId': 'string'
                                }
                            },
                            'Schedule': {
                                'EndTime': 'string',
                                'EventFilter': {
                                    'Dimensions': {
                                        'Attributes': {
                                            'string': {
                                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            }
                                        },
                                        'EventType': {
                                            'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                            'Values': [
                                                'string',
                                            ]
                                        },
                                        'Metrics': {
                                            'string': {
                                                'ComparisonOperator': 'string',
                                                'Value': 123.0
                                            }
                                        }
                                    },
                                    'FilterType': 'SYSTEM'|'ENDPOINT'
                                },
                                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                                'IsLocalTime': True|False,
                                'QuietTime': {
                                    'End': 'string',
                                    'Start': 'string'
                                },
                                'StartTime': 'string',
                                'Timezone': 'string'
                            },
                            'SizePercent': 123,
                            'State': {
                                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                            },
                            'TreatmentDescription': 'string',
                            'TreatmentName': 'string'
                        },
                    ],
                    'ApplicationId': 'string',
                    'CreationDate': 'string',
                    'DefaultState': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                    },
                    'Description': 'string',
                    'HoldoutPercent': 123,
                    'Hook': {
                        'LambdaFunctionName': 'string',
                        'Mode': 'DELIVERY'|'FILTER',
                        'WebUrl': 'string'
                    },
                    'Id': 'string',
                    'IsPaused': True|False,
                    'LastModifiedDate': 'string',
                    'Limits': {
                        'Daily': 123,
                        'MaximumDuration': 123,
                        'MessagesPerSecond': 123,
                        'Total': 123
                    },
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
                        }
                    },
                    'Name': 'string',
                    'Schedule': {
                        'EndTime': 'string',
                        'EventFilter': {
                            'Dimensions': {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'EventType': {
                                    'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                }
                            },
                            'FilterType': 'SYSTEM'|'ENDPOINT'
                        },
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SegmentId': 'string',
                    'SegmentVersion': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignsResponse (dict) -- List of available campaigns.
    Item (list) -- A list of campaigns.
    (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_campaigns(ApplicationId=None, PageSize=None, Token=None):
    """
    Returns information about your campaigns.
    See also: AWS API Documentation
    
    
    :example: response = client.get_campaigns(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'CampaignsResponse': {
            'Item': [
                {
                    'AdditionalTreatments': [
                        {
                            'Id': 'string',
                            'MessageConfiguration': {
                                'ADMMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'TimeToLive': 123,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'APNSMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'TimeToLive': 123,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'BaiduMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'TimeToLive': 123,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'DefaultMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'TimeToLive': 123,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'EmailMessage': {
                                    'Body': 'string',
                                    'FromAddress': 'string',
                                    'HtmlBody': 'string',
                                    'Title': 'string'
                                },
                                'GCMMessage': {
                                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                                    'Body': 'string',
                                    'ImageIconUrl': 'string',
                                    'ImageSmallIconUrl': 'string',
                                    'ImageUrl': 'string',
                                    'JsonBody': 'string',
                                    'MediaUrl': 'string',
                                    'RawContent': 'string',
                                    'SilentPush': True|False,
                                    'TimeToLive': 123,
                                    'Title': 'string',
                                    'Url': 'string'
                                },
                                'SMSMessage': {
                                    'Body': 'string',
                                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                                    'SenderId': 'string'
                                }
                            },
                            'Schedule': {
                                'EndTime': 'string',
                                'EventFilter': {
                                    'Dimensions': {
                                        'Attributes': {
                                            'string': {
                                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            }
                                        },
                                        'EventType': {
                                            'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                            'Values': [
                                                'string',
                                            ]
                                        },
                                        'Metrics': {
                                            'string': {
                                                'ComparisonOperator': 'string',
                                                'Value': 123.0
                                            }
                                        }
                                    },
                                    'FilterType': 'SYSTEM'|'ENDPOINT'
                                },
                                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                                'IsLocalTime': True|False,
                                'QuietTime': {
                                    'End': 'string',
                                    'Start': 'string'
                                },
                                'StartTime': 'string',
                                'Timezone': 'string'
                            },
                            'SizePercent': 123,
                            'State': {
                                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                            },
                            'TreatmentDescription': 'string',
                            'TreatmentName': 'string'
                        },
                    ],
                    'ApplicationId': 'string',
                    'CreationDate': 'string',
                    'DefaultState': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                    },
                    'Description': 'string',
                    'HoldoutPercent': 123,
                    'Hook': {
                        'LambdaFunctionName': 'string',
                        'Mode': 'DELIVERY'|'FILTER',
                        'WebUrl': 'string'
                    },
                    'Id': 'string',
                    'IsPaused': True|False,
                    'LastModifiedDate': 'string',
                    'Limits': {
                        'Daily': 123,
                        'MaximumDuration': 123,
                        'MessagesPerSecond': 123,
                        'Total': 123
                    },
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
                        }
                    },
                    'Name': 'string',
                    'Schedule': {
                        'EndTime': 'string',
                        'EventFilter': {
                            'Dimensions': {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'EventType': {
                                    'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                }
                            },
                            'FilterType': 'SYSTEM'|'ENDPOINT'
                        },
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SegmentId': 'string',
                    'SegmentVersion': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignsResponse (dict) -- List of available campaigns.
    Item (list) -- A list of campaigns.
    (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_channels(ApplicationId=None):
    """
    Get all channels.
    See also: AWS API Documentation
    
    
    :example: response = client.get_channels(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'ChannelsResponse': {
            'Channels': {
                'string': {
                    'ApplicationId': 'string',
                    'CreationDate': 'string',
                    'Enabled': True|False,
                    'HasCredential': True|False,
                    'Id': 'string',
                    'IsArchived': True|False,
                    'LastModifiedBy': 'string',
                    'LastModifiedDate': 'string',
                    'Version': 123
                }
            }
        }
    }
    
    
    """
    pass

def get_email_channel(ApplicationId=None):
    """
    Get an email channel.
    See also: AWS API Documentation
    
    
    :example: response = client.get_email_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'EmailChannelResponse': {
            'ApplicationId': 'string',
            'ConfigurationSet': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'FromAddress': 'string',
            'HasCredential': True|False,
            'Id': 'string',
            'Identity': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'MessagesPerSecond': 123,
            'Platform': 'string',
            'RoleArn': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_endpoint(ApplicationId=None, EndpointId=None):
    """
    Returns information about an endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.get_endpoint(
        ApplicationId='string',
        EndpointId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type EndpointId: string
    :param EndpointId: [REQUIRED] The unique ID of the endpoint.

    :rtype: dict
    :return: {
        'EndpointResponse': {
            'Address': 'string',
            'ApplicationId': 'string',
            'Attributes': {
                'string': [
                    'string',
                ]
            },
            'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'VOICE'|'EMAIL'|'BAIDU'|'CUSTOM',
            'CohortId': 'string',
            'CreationDate': 'string',
            'Demographic': {
                'AppVersion': 'string',
                'Locale': 'string',
                'Make': 'string',
                'Model': 'string',
                'ModelVersion': 'string',
                'Platform': 'string',
                'PlatformVersion': 'string',
                'Timezone': 'string'
            },
            'EffectiveDate': 'string',
            'EndpointStatus': 'string',
            'Id': 'string',
            'Location': {
                'City': 'string',
                'Country': 'string',
                'Latitude': 123.0,
                'Longitude': 123.0,
                'PostalCode': 'string',
                'Region': 'string'
            },
            'Metrics': {
                'string': 123.0
            },
            'OptOut': 'string',
            'RequestId': 'string',
            'User': {
                'UserAttributes': {
                    'string': [
                        'string',
                    ]
                },
                'UserId': 'string'
            }
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    EndpointResponse (dict) -- Endpoint response
    Address (string) -- The address of the endpoint as provided by your push provider. For example, the DeviceToken or RegistrationId.
    ApplicationId (string) -- The ID of the application that is associated with the endpoint.
    Attributes (dict) -- Custom attributes that describe the endpoint by associating a name with an array of values. For example, an attribute named "interests" might have the following values: ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    CohortId (string) -- A number from 0-99 that represents the cohort the endpoint is assigned to. Endpoints are grouped into cohorts randomly, and each cohort contains approximately 1 percent of the endpoints for an app. Amazon Pinpoint assigns cohorts to the holdout or treatment allocations for a campaign.
    CreationDate (string) -- The date and time when the endpoint was created, shown in ISO 8601 format.
    Demographic (dict) -- The endpoint demographic attributes.
    AppVersion (string) -- The version of the application associated with the endpoint.
    Locale (string) -- The endpoint locale in the following format: The ISO 639-1 alpha-2 code, followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
    Make (string) -- The manufacturer of the endpoint device, such as Apple or Samsung.
    Model (string) -- The model name or number of the endpoint device, such as iPhone.
    ModelVersion (string) -- The model version of the endpoint device.
    Platform (string) -- The platform of the endpoint device, such as iOS or Android.
    PlatformVersion (string) -- The platform version of the endpoint device.
    Timezone (string) -- The timezone of the endpoint. Specified as a tz database value, such as Americas/Los_Angeles.
    
    
    EffectiveDate (string) -- The date and time when the endpoint was last updated, shown in ISO 8601 format.
    EndpointStatus (string) -- Unused.
    Id (string) -- The unique ID that you assigned to the endpoint. The ID should be a globally unique identifier (GUID) to ensure that it doesn't conflict with other endpoint IDs associated with the application.
    Location (dict) -- The endpoint location attributes.
    City (string) -- The city where the endpoint is located.
    Country (string) -- The two-letter code for the country or region of the endpoint. Specified as an ISO 3166-1 alpha-2 code, such as "US" for the United States.
    Latitude (float) -- The latitude of the endpoint location, rounded to one decimal place.
    Longitude (float) -- The longitude of the endpoint location, rounded to one decimal place.
    PostalCode (string) -- The postal code or zip code of the endpoint.
    Region (string) -- The region of the endpoint location. For example, in the United States, this corresponds to a state.
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint.
    (string) --
    (float) --
    
    
    
    
    OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
    RequestId (string) -- The unique ID for the most recent request to update the endpoint.
    User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
    UserAttributes (dict) -- Custom attributes that describe the user by associating a name with an array of values. For example, an attribute named "interests" might have the following values: ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    UserId (string) -- The unique ID of the user.
    
    
    
    
    
    
    
    """
    pass

def get_event_stream(ApplicationId=None):
    """
    Returns the event stream for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.get_event_stream(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'EventStream': {
            'ApplicationId': 'string',
            'DestinationStreamArn': 'string',
            'ExternalId': 'string',
            'LastModifiedDate': 'string',
            'LastUpdatedBy': 'string',
            'RoleArn': 'string'
        }
    }
    
    
    """
    pass

def get_export_job(ApplicationId=None, JobId=None):
    """
    Returns information about an export job.
    See also: AWS API Documentation
    
    
    :example: response = client.get_export_job(
        ApplicationId='string',
        JobId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type JobId: string
    :param JobId: [REQUIRED] The unique ID of the job.

    :rtype: dict
    :return: {
        'ExportJobResponse': {
            'ApplicationId': 'string',
            'CompletedPieces': 123,
            'CompletionDate': 'string',
            'CreationDate': 'string',
            'Definition': {
                'RoleArn': 'string',
                'S3UrlPrefix': 'string',
                'SegmentId': 'string',
                'SegmentVersion': 123
            },
            'FailedPieces': 123,
            'Failures': [
                'string',
            ],
            'Id': 'string',
            'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
            'TotalFailures': 123,
            'TotalPieces': 123,
            'TotalProcessed': 123,
            'Type': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ExportJobResponse (dict) -- Export job response.
    ApplicationId (string) -- The unique ID of the application associated with the export job.
    CompletedPieces (integer) -- The number of pieces that have successfully completed as of the time of the request.
    CompletionDate (string) -- The date the job completed in ISO 8601 format.
    CreationDate (string) -- The date the job was created in ISO 8601 format.
    Definition (dict) -- The export job settings.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that endpoints will be exported to.
    S3UrlPrefix (string) -- A URL that points to the location within an Amazon S3 bucket that will receive the export. The location is typically a folder with multiple files. The URL should follow this format: s3://bucket-name/folder-name/ Amazon Pinpoint will export endpoints to this location.
    SegmentId (string) -- The ID of the segment to export endpoints from. If not present, Amazon Pinpoint exports all of the endpoints that belong to the application.
    SegmentVersion (integer) -- The version of the segment to export if specified.
    
    
    FailedPieces (integer) -- The number of pieces that failed to be processed as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the job.
    JobStatus (string) -- The status of the job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed.
    TotalFailures (integer) -- The number of endpoints that were not processed; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be processed to finish the job. Each piece is an approximately equal portion of the endpoints.
    TotalProcessed (integer) -- The number of endpoints that were processed by the job.
    Type (string) -- The job type. Will be 'EXPORT'.
    
    
    
    
    
    """
    pass

def get_export_jobs(ApplicationId=None, PageSize=None, Token=None):
    """
    Returns information about your export jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.get_export_jobs(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ExportJobsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CompletedPieces': 123,
                    'CompletionDate': 'string',
                    'CreationDate': 'string',
                    'Definition': {
                        'RoleArn': 'string',
                        'S3UrlPrefix': 'string',
                        'SegmentId': 'string',
                        'SegmentVersion': 123
                    },
                    'FailedPieces': 123,
                    'Failures': [
                        'string',
                    ],
                    'Id': 'string',
                    'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
                    'TotalFailures': 123,
                    'TotalPieces': 123,
                    'TotalProcessed': 123,
                    'Type': 'string'
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ExportJobsResponse (dict) -- Export job list.
    Item (list) -- A list of export jobs for the application.
    (dict) -- Export job response.
    ApplicationId (string) -- The unique ID of the application associated with the export job.
    CompletedPieces (integer) -- The number of pieces that have successfully completed as of the time of the request.
    CompletionDate (string) -- The date the job completed in ISO 8601 format.
    CreationDate (string) -- The date the job was created in ISO 8601 format.
    Definition (dict) -- The export job settings.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that endpoints will be exported to.
    S3UrlPrefix (string) -- A URL that points to the location within an Amazon S3 bucket that will receive the export. The location is typically a folder with multiple files. The URL should follow this format: s3://bucket-name/folder-name/ Amazon Pinpoint will export endpoints to this location.
    SegmentId (string) -- The ID of the segment to export endpoints from. If not present, Amazon Pinpoint exports all of the endpoints that belong to the application.
    SegmentVersion (integer) -- The version of the segment to export if specified.
    
    
    FailedPieces (integer) -- The number of pieces that failed to be processed as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the job.
    JobStatus (string) -- The status of the job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed.
    TotalFailures (integer) -- The number of endpoints that were not processed; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be processed to finish the job. Each piece is an approximately equal portion of the endpoints.
    TotalProcessed (integer) -- The number of endpoints that were processed by the job.
    Type (string) -- The job type. Will be 'EXPORT'.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_gcm_channel(ApplicationId=None):
    """
    Returns information about the GCM channel for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.get_gcm_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'GCMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_import_job(ApplicationId=None, JobId=None):
    """
    Returns information about an import job.
    See also: AWS API Documentation
    
    
    :example: response = client.get_import_job(
        ApplicationId='string',
        JobId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type JobId: string
    :param JobId: [REQUIRED] The unique ID of the job.

    :rtype: dict
    :return: {
        'ImportJobResponse': {
            'ApplicationId': 'string',
            'CompletedPieces': 123,
            'CompletionDate': 'string',
            'CreationDate': 'string',
            'Definition': {
                'DefineSegment': True|False,
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RegisterEndpoints': True|False,
                'RoleArn': 'string',
                'S3Url': 'string',
                'SegmentId': 'string',
                'SegmentName': 'string'
            },
            'FailedPieces': 123,
            'Failures': [
                'string',
            ],
            'Id': 'string',
            'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
            'TotalFailures': 123,
            'TotalPieces': 123,
            'TotalProcessed': 123,
            'Type': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ImportJobResponse (dict) -- Import job response.
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the files that contain the endpoint definitions. Valid values: CSV, JSON
    RegisterEndpoints (boolean) -- Sets whether the endpoints are registered with Amazon Pinpoint when they are imported.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that contains the endpoints to import.
    S3Url (string) -- The URL of the S3 bucket that contains the segment information to import. The location can be a folder or a single file. The URL should use the following format: s3://bucket-name/folder-name/file-name Amazon Pinpoint imports endpoints from this location and any subfolders it contains.
    SegmentId (string) -- The ID of the segment to update if the import job is meant to update an existing segment.
    SegmentName (string) -- A custom name for the segment created by the import job. Use if DefineSegment is true.
    
    
    FailedPieces (integer) -- The number of pieces that have failed to import as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the import job.
    JobStatus (string) -- The status of the import job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed to import.
    TotalFailures (integer) -- The number of endpoints that failed to import; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be imported to finish the job. Each piece is an approximately equal portion of the endpoints to import.
    TotalProcessed (integer) -- The number of endpoints that were processed by the import job.
    Type (string) -- The job type. Will be Import.
    
    
    
    
    
    """
    pass

def get_import_jobs(ApplicationId=None, PageSize=None, Token=None):
    """
    Returns information about your import jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.get_import_jobs(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ImportJobsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CompletedPieces': 123,
                    'CompletionDate': 'string',
                    'CreationDate': 'string',
                    'Definition': {
                        'DefineSegment': True|False,
                        'ExternalId': 'string',
                        'Format': 'CSV'|'JSON',
                        'RegisterEndpoints': True|False,
                        'RoleArn': 'string',
                        'S3Url': 'string',
                        'SegmentId': 'string',
                        'SegmentName': 'string'
                    },
                    'FailedPieces': 123,
                    'Failures': [
                        'string',
                    ],
                    'Id': 'string',
                    'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
                    'TotalFailures': 123,
                    'TotalPieces': 123,
                    'TotalProcessed': 123,
                    'Type': 'string'
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ImportJobsResponse (dict) -- Import job list.
    Item (list) -- A list of import jobs for the application.
    (dict) -- Import job response.
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the files that contain the endpoint definitions. Valid values: CSV, JSON
    RegisterEndpoints (boolean) -- Sets whether the endpoints are registered with Amazon Pinpoint when they are imported.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that contains the endpoints to import.
    S3Url (string) -- The URL of the S3 bucket that contains the segment information to import. The location can be a folder or a single file. The URL should use the following format: s3://bucket-name/folder-name/file-name Amazon Pinpoint imports endpoints from this location and any subfolders it contains.
    SegmentId (string) -- The ID of the segment to update if the import job is meant to update an existing segment.
    SegmentName (string) -- A custom name for the segment created by the import job. Use if DefineSegment is true.
    
    
    FailedPieces (integer) -- The number of pieces that have failed to import as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the import job.
    JobStatus (string) -- The status of the import job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed to import.
    TotalFailures (integer) -- The number of endpoints that failed to import; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be imported to finish the job. Each piece is an approximately equal portion of the endpoints to import.
    TotalProcessed (integer) -- The number of endpoints that were processed by the import job.
    Type (string) -- The job type. Will be Import.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
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

def get_segment(ApplicationId=None, SegmentId=None):
    """
    Returns information about a segment.
    See also: AWS API Documentation
    
    
    :example: response = client.get_segment(
        ApplicationId='string',
        SegmentId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type SegmentId: string
    :param SegmentId: [REQUIRED] The unique ID of the segment.

    :rtype: dict
    :return: {
        'SegmentResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Channel': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'GPSPoint': {
                        'Coordinates': {
                            'Latitude': 123.0,
                            'Longitude': 123.0
                        },
                        'RangeInKilometers': 123.0
                    }
                },
                'Metrics': {
                    'string': {
                        'ComparisonOperator': 'string',
                        'Value': 123.0
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Id': 'string',
            'ImportDefinition': {
                'ChannelCounts': {
                    'string': 123
                },
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RoleArn': 'string',
                'S3Url': 'string',
                'Size': 123
            },
            'LastModifiedDate': 'string',
            'Name': 'string',
            'SegmentGroups': {
                'Groups': [
                    {
                        'Dimensions': [
                            {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Behavior': {
                                    'Recency': {
                                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                        'RecencyType': 'ACTIVE'|'INACTIVE'
                                    }
                                },
                                'Demographic': {
                                    'AppVersion': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Channel': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'DeviceType': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Make': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Model': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Platform': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Location': {
                                    'Country': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'GPSPoint': {
                                        'Coordinates': {
                                            'Latitude': 123.0,
                                            'Longitude': 123.0
                                        },
                                        'RangeInKilometers': 123.0
                                    }
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                },
                                'UserAttributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                }
                            },
                        ],
                        'SourceSegments': [
                            {
                                'Id': 'string',
                                'Version': 123
                            },
                        ],
                        'SourceType': 'ALL'|'ANY'|'NONE',
                        'Type': 'ALL'|'ANY'|'NONE'
                    },
                ],
                'Include': 'ALL'|'ANY'|'NONE'
            },
            'SegmentType': 'DIMENSIONAL'|'IMPORT',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application that the segment applies to.
    CreationDate (string) -- The date and time when the segment was created.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- The number of channel types in the imported segment.
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- The URL of the S3 bucket that the segment was imported from.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date and time when the segment was last modified.
    Name (string) -- The name of the segment.
    SegmentGroups (dict) -- A segment group, which consists of zero or more source segments, plus dimensions that are applied to those source segments.
    Groups (list) -- A set of segment criteria to evaluate.
    (dict) -- Segment group definition.
    Dimensions (list) -- List of dimensions to include or exclude.
    (dict) -- Segment dimensions
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    
    SourceSegments (list) -- The base segment that you build your segment on. The source segment defines the starting "universe" of endpoints. When you add dimensions to the segment, it filters the source segment based on the dimensions that you specify. You can specify more than one dimensional segment. You can only specify one imported segment. NOTE: If you specify an imported segment for this attribute, the segment size estimate that appears in the Amazon Pinpoint console shows the size of the imported segment, without any filters applied to it.
    (dict) -- Segment reference.
    Id (string) -- A unique identifier for the segment.
    Version (integer) -- If specified contains a specific version of the segment included.
    
    
    
    
    SourceType (string) -- Specify how to handle multiple source segments. For example, if you specify three source segments, should the resulting segment be based on any or all of the segments? Acceptable values: ANY or ALL.
    Type (string) -- Specify how to handle multiple segment dimensions. For example, if you specify three dimensions, should the resulting segment include endpoints that are matched by all, any, or none of the dimensions? Acceptable values: ALL, ANY, or NONE.
    
    
    
    
    Include (string) -- Specify how to handle multiple segment groups. For example, if the segment includes three segment groups, should the resulting segment include endpoints that are matched by all, any, or none of the segment groups you created. Acceptable values: ALL, ANY, or NONE.
    
    
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def get_segment_export_jobs(ApplicationId=None, PageSize=None, SegmentId=None, Token=None):
    """
    Returns a list of export jobs for a specific segment.
    See also: AWS API Documentation
    
    
    :example: response = client.get_segment_export_jobs(
        ApplicationId='string',
        PageSize='string',
        SegmentId='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type SegmentId: string
    :param SegmentId: [REQUIRED] The unique ID of the segment.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ExportJobsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CompletedPieces': 123,
                    'CompletionDate': 'string',
                    'CreationDate': 'string',
                    'Definition': {
                        'RoleArn': 'string',
                        'S3UrlPrefix': 'string',
                        'SegmentId': 'string',
                        'SegmentVersion': 123
                    },
                    'FailedPieces': 123,
                    'Failures': [
                        'string',
                    ],
                    'Id': 'string',
                    'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
                    'TotalFailures': 123,
                    'TotalPieces': 123,
                    'TotalProcessed': 123,
                    'Type': 'string'
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ExportJobsResponse (dict) -- Export job list.
    Item (list) -- A list of export jobs for the application.
    (dict) -- Export job response.
    ApplicationId (string) -- The unique ID of the application associated with the export job.
    CompletedPieces (integer) -- The number of pieces that have successfully completed as of the time of the request.
    CompletionDate (string) -- The date the job completed in ISO 8601 format.
    CreationDate (string) -- The date the job was created in ISO 8601 format.
    Definition (dict) -- The export job settings.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that endpoints will be exported to.
    S3UrlPrefix (string) -- A URL that points to the location within an Amazon S3 bucket that will receive the export. The location is typically a folder with multiple files. The URL should follow this format: s3://bucket-name/folder-name/ Amazon Pinpoint will export endpoints to this location.
    SegmentId (string) -- The ID of the segment to export endpoints from. If not present, Amazon Pinpoint exports all of the endpoints that belong to the application.
    SegmentVersion (integer) -- The version of the segment to export if specified.
    
    
    FailedPieces (integer) -- The number of pieces that failed to be processed as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the job.
    JobStatus (string) -- The status of the job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed.
    TotalFailures (integer) -- The number of endpoints that were not processed; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be processed to finish the job. Each piece is an approximately equal portion of the endpoints.
    TotalProcessed (integer) -- The number of endpoints that were processed by the job.
    Type (string) -- The job type. Will be 'EXPORT'.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_segment_import_jobs(ApplicationId=None, PageSize=None, SegmentId=None, Token=None):
    """
    Returns a list of import jobs for a specific segment.
    See also: AWS API Documentation
    
    
    :example: response = client.get_segment_import_jobs(
        ApplicationId='string',
        PageSize='string',
        SegmentId='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type SegmentId: string
    :param SegmentId: [REQUIRED] The unique ID of the segment.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ImportJobsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CompletedPieces': 123,
                    'CompletionDate': 'string',
                    'CreationDate': 'string',
                    'Definition': {
                        'DefineSegment': True|False,
                        'ExternalId': 'string',
                        'Format': 'CSV'|'JSON',
                        'RegisterEndpoints': True|False,
                        'RoleArn': 'string',
                        'S3Url': 'string',
                        'SegmentId': 'string',
                        'SegmentName': 'string'
                    },
                    'FailedPieces': 123,
                    'Failures': [
                        'string',
                    ],
                    'Id': 'string',
                    'JobStatus': 'CREATED'|'INITIALIZING'|'PROCESSING'|'COMPLETING'|'COMPLETED'|'FAILING'|'FAILED',
                    'TotalFailures': 123,
                    'TotalPieces': 123,
                    'TotalProcessed': 123,
                    'Type': 'string'
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ImportJobsResponse (dict) -- Import job list.
    Item (list) -- A list of import jobs for the application.
    (dict) -- Import job response.
    ApplicationId (string) -- The unique ID of the application to which the import job applies.
    CompletedPieces (integer) -- The number of pieces that have successfully imported as of the time of the request.
    CompletionDate (string) -- The date the import job completed in ISO 8601 format.
    CreationDate (string) -- The date the import job was created in ISO 8601 format.
    Definition (dict) -- The import job settings.
    DefineSegment (boolean) -- Sets whether the endpoints create a segment when they are imported.
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the files that contain the endpoint definitions. Valid values: CSV, JSON
    RegisterEndpoints (boolean) -- Sets whether the endpoints are registered with Amazon Pinpoint when they are imported.
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the Amazon S3 location that contains the endpoints to import.
    S3Url (string) -- The URL of the S3 bucket that contains the segment information to import. The location can be a folder or a single file. The URL should use the following format: s3://bucket-name/folder-name/file-name Amazon Pinpoint imports endpoints from this location and any subfolders it contains.
    SegmentId (string) -- The ID of the segment to update if the import job is meant to update an existing segment.
    SegmentName (string) -- A custom name for the segment created by the import job. Use if DefineSegment is true.
    
    
    FailedPieces (integer) -- The number of pieces that have failed to import as of the time of the request.
    Failures (list) -- Provides up to 100 of the first failed entries for the job, if any exist.
    (string) --
    
    
    Id (string) -- The unique ID of the import job.
    JobStatus (string) -- The status of the import job. Valid values: CREATED, INITIALIZING, PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or more pieces failed to import.
    TotalFailures (integer) -- The number of endpoints that failed to import; for example, because of syntax errors.
    TotalPieces (integer) -- The total number of pieces that must be imported to finish the job. Each piece is an approximately equal portion of the endpoints to import.
    TotalProcessed (integer) -- The number of endpoints that were processed by the import job.
    Type (string) -- The job type. Will be Import.
    
    
    
    
    NextToken (string) -- The string that you use in a subsequent request to get the next page of results in a paginated response.
    
    
    
    
    
    """
    pass

def get_segment_version(ApplicationId=None, SegmentId=None, Version=None):
    """
    Returns information about a segment version.
    See also: AWS API Documentation
    
    
    :example: response = client.get_segment_version(
        ApplicationId='string',
        SegmentId='string',
        Version='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type SegmentId: string
    :param SegmentId: [REQUIRED] The unique ID of the segment.

    :type Version: string
    :param Version: [REQUIRED] The segment version.

    :rtype: dict
    :return: {
        'SegmentResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Channel': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'GPSPoint': {
                        'Coordinates': {
                            'Latitude': 123.0,
                            'Longitude': 123.0
                        },
                        'RangeInKilometers': 123.0
                    }
                },
                'Metrics': {
                    'string': {
                        'ComparisonOperator': 'string',
                        'Value': 123.0
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Id': 'string',
            'ImportDefinition': {
                'ChannelCounts': {
                    'string': 123
                },
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RoleArn': 'string',
                'S3Url': 'string',
                'Size': 123
            },
            'LastModifiedDate': 'string',
            'Name': 'string',
            'SegmentGroups': {
                'Groups': [
                    {
                        'Dimensions': [
                            {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Behavior': {
                                    'Recency': {
                                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                        'RecencyType': 'ACTIVE'|'INACTIVE'
                                    }
                                },
                                'Demographic': {
                                    'AppVersion': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Channel': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'DeviceType': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Make': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Model': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Platform': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Location': {
                                    'Country': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'GPSPoint': {
                                        'Coordinates': {
                                            'Latitude': 123.0,
                                            'Longitude': 123.0
                                        },
                                        'RangeInKilometers': 123.0
                                    }
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                },
                                'UserAttributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                }
                            },
                        ],
                        'SourceSegments': [
                            {
                                'Id': 'string',
                                'Version': 123
                            },
                        ],
                        'SourceType': 'ALL'|'ANY'|'NONE',
                        'Type': 'ALL'|'ANY'|'NONE'
                    },
                ],
                'Include': 'ALL'|'ANY'|'NONE'
            },
            'SegmentType': 'DIMENSIONAL'|'IMPORT',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application that the segment applies to.
    CreationDate (string) -- The date and time when the segment was created.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- The number of channel types in the imported segment.
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- The URL of the S3 bucket that the segment was imported from.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date and time when the segment was last modified.
    Name (string) -- The name of the segment.
    SegmentGroups (dict) -- A segment group, which consists of zero or more source segments, plus dimensions that are applied to those source segments.
    Groups (list) -- A set of segment criteria to evaluate.
    (dict) -- Segment group definition.
    Dimensions (list) -- List of dimensions to include or exclude.
    (dict) -- Segment dimensions
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    
    SourceSegments (list) -- The base segment that you build your segment on. The source segment defines the starting "universe" of endpoints. When you add dimensions to the segment, it filters the source segment based on the dimensions that you specify. You can specify more than one dimensional segment. You can only specify one imported segment. NOTE: If you specify an imported segment for this attribute, the segment size estimate that appears in the Amazon Pinpoint console shows the size of the imported segment, without any filters applied to it.
    (dict) -- Segment reference.
    Id (string) -- A unique identifier for the segment.
    Version (integer) -- If specified contains a specific version of the segment included.
    
    
    
    
    SourceType (string) -- Specify how to handle multiple source segments. For example, if you specify three source segments, should the resulting segment be based on any or all of the segments? Acceptable values: ANY or ALL.
    Type (string) -- Specify how to handle multiple segment dimensions. For example, if you specify three dimensions, should the resulting segment include endpoints that are matched by all, any, or none of the dimensions? Acceptable values: ALL, ANY, or NONE.
    
    
    
    
    Include (string) -- Specify how to handle multiple segment groups. For example, if the segment includes three segment groups, should the resulting segment include endpoints that are matched by all, any, or none of the segment groups you created. Acceptable values: ALL, ANY, or NONE.
    
    
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def get_segment_versions(ApplicationId=None, PageSize=None, SegmentId=None, Token=None):
    """
    Returns information about your segment versions.
    See also: AWS API Documentation
    
    
    :example: response = client.get_segment_versions(
        ApplicationId='string',
        PageSize='string',
        SegmentId='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type SegmentId: string
    :param SegmentId: [REQUIRED] The unique ID of the segment.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'SegmentsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CreationDate': 'string',
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'Behavior': {
                            'Recency': {
                                'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                'RecencyType': 'ACTIVE'|'INACTIVE'
                            }
                        },
                        'Demographic': {
                            'AppVersion': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Channel': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'DeviceType': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Make': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Model': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Platform': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'Location': {
                            'Country': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'GPSPoint': {
                                'Coordinates': {
                                    'Latitude': 123.0,
                                    'Longitude': 123.0
                                },
                                'RangeInKilometers': 123.0
                            }
                        },
                        'Metrics': {
                            'string': {
                                'ComparisonOperator': 'string',
                                'Value': 123.0
                            }
                        },
                        'UserAttributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        }
                    },
                    'Id': 'string',
                    'ImportDefinition': {
                        'ChannelCounts': {
                            'string': 123
                        },
                        'ExternalId': 'string',
                        'Format': 'CSV'|'JSON',
                        'RoleArn': 'string',
                        'S3Url': 'string',
                        'Size': 123
                    },
                    'LastModifiedDate': 'string',
                    'Name': 'string',
                    'SegmentGroups': {
                        'Groups': [
                            {
                                'Dimensions': [
                                    {
                                        'Attributes': {
                                            'string': {
                                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            }
                                        },
                                        'Behavior': {
                                            'Recency': {
                                                'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                                'RecencyType': 'ACTIVE'|'INACTIVE'
                                            }
                                        },
                                        'Demographic': {
                                            'AppVersion': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'Channel': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'DeviceType': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'Make': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'Model': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'Platform': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            }
                                        },
                                        'Location': {
                                            'Country': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'GPSPoint': {
                                                'Coordinates': {
                                                    'Latitude': 123.0,
                                                    'Longitude': 123.0
                                                },
                                                'RangeInKilometers': 123.0
                                            }
                                        },
                                        'Metrics': {
                                            'string': {
                                                'ComparisonOperator': 'string',
                                                'Value': 123.0
                                            }
                                        },
                                        'UserAttributes': {
                                            'string': {
                                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            }
                                        }
                                    },
                                ],
                                'SourceSegments': [
                                    {
                                        'Id': 'string',
                                        'Version': 123
                                    },
                                ],
                                'SourceType': 'ALL'|'ANY'|'NONE',
                                'Type': 'ALL'|'ANY'|'NONE'
                            },
                        ],
                        'Include': 'ALL'|'ANY'|'NONE'
                    },
                    'SegmentType': 'DIMENSIONAL'|'IMPORT',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentsResponse (dict) -- Segments in your account.
    Item (list) -- The list of segments.
    (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application that the segment applies to.
    CreationDate (string) -- The date and time when the segment was created.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- The number of channel types in the imported segment.
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- The URL of the S3 bucket that the segment was imported from.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date and time when the segment was last modified.
    Name (string) -- The name of the segment.
    SegmentGroups (dict) -- A segment group, which consists of zero or more source segments, plus dimensions that are applied to those source segments.
    Groups (list) -- A set of segment criteria to evaluate.
    (dict) -- Segment group definition.
    Dimensions (list) -- List of dimensions to include or exclude.
    (dict) -- Segment dimensions
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    
    SourceSegments (list) -- The base segment that you build your segment on. The source segment defines the starting "universe" of endpoints. When you add dimensions to the segment, it filters the source segment based on the dimensions that you specify. You can specify more than one dimensional segment. You can only specify one imported segment. NOTE: If you specify an imported segment for this attribute, the segment size estimate that appears in the Amazon Pinpoint console shows the size of the imported segment, without any filters applied to it.
    (dict) -- Segment reference.
    Id (string) -- A unique identifier for the segment.
    Version (integer) -- If specified contains a specific version of the segment included.
    
    
    
    
    SourceType (string) -- Specify how to handle multiple source segments. For example, if you specify three source segments, should the resulting segment be based on any or all of the segments? Acceptable values: ANY or ALL.
    Type (string) -- Specify how to handle multiple segment dimensions. For example, if you specify three dimensions, should the resulting segment include endpoints that are matched by all, any, or none of the dimensions? Acceptable values: ALL, ANY, or NONE.
    
    
    
    
    Include (string) -- Specify how to handle multiple segment groups. For example, if the segment includes three segment groups, should the resulting segment include endpoints that are matched by all, any, or none of the segment groups you created. Acceptable values: ALL, ANY, or NONE.
    
    
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    NextToken (string) -- An identifier used to retrieve the next page of results. The token is null if no additional pages exist.
    
    
    
    
    
    """
    pass

def get_segments(ApplicationId=None, PageSize=None, Token=None):
    """
    Used to get information about your segments.
    See also: AWS API Documentation
    
    
    :example: response = client.get_segments(
        ApplicationId='string',
        PageSize='string',
        Token='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type PageSize: string
    :param PageSize: The number of entries you want on each page in the response.

    :type Token: string
    :param Token: The NextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'SegmentsResponse': {
            'Item': [
                {
                    'ApplicationId': 'string',
                    'CreationDate': 'string',
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'Behavior': {
                            'Recency': {
                                'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                'RecencyType': 'ACTIVE'|'INACTIVE'
                            }
                        },
                        'Demographic': {
                            'AppVersion': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Channel': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'DeviceType': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Make': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Model': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'Platform': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'Location': {
                            'Country': {
                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            },
                            'GPSPoint': {
                                'Coordinates': {
                                    'Latitude': 123.0,
                                    'Longitude': 123.0
                                },
                                'RangeInKilometers': 123.0
                            }
                        },
                        'Metrics': {
                            'string': {
                                'ComparisonOperator': 'string',
                                'Value': 123.0
                            }
                        },
                        'UserAttributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        }
                    },
                    'Id': 'string',
                    'ImportDefinition': {
                        'ChannelCounts': {
                            'string': 123
                        },
                        'ExternalId': 'string',
                        'Format': 'CSV'|'JSON',
                        'RoleArn': 'string',
                        'S3Url': 'string',
                        'Size': 123
                    },
                    'LastModifiedDate': 'string',
                    'Name': 'string',
                    'SegmentGroups': {
                        'Groups': [
                            {
                                'Dimensions': [
                                    {
                                        'Attributes': {
                                            'string': {
                                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            }
                                        },
                                        'Behavior': {
                                            'Recency': {
                                                'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                                'RecencyType': 'ACTIVE'|'INACTIVE'
                                            }
                                        },
                                        'Demographic': {
                                            'AppVersion': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'Channel': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'DeviceType': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'Make': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'Model': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'Platform': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            }
                                        },
                                        'Location': {
                                            'Country': {
                                                'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            },
                                            'GPSPoint': {
                                                'Coordinates': {
                                                    'Latitude': 123.0,
                                                    'Longitude': 123.0
                                                },
                                                'RangeInKilometers': 123.0
                                            }
                                        },
                                        'Metrics': {
                                            'string': {
                                                'ComparisonOperator': 'string',
                                                'Value': 123.0
                                            }
                                        },
                                        'UserAttributes': {
                                            'string': {
                                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                                'Values': [
                                                    'string',
                                                ]
                                            }
                                        }
                                    },
                                ],
                                'SourceSegments': [
                                    {
                                        'Id': 'string',
                                        'Version': 123
                                    },
                                ],
                                'SourceType': 'ALL'|'ANY'|'NONE',
                                'Type': 'ALL'|'ANY'|'NONE'
                            },
                        ],
                        'Include': 'ALL'|'ANY'|'NONE'
                    },
                    'SegmentType': 'DIMENSIONAL'|'IMPORT',
                    'Version': 123
                },
            ],
            'NextToken': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentsResponse (dict) -- Segments in your account.
    Item (list) -- The list of segments.
    (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application that the segment applies to.
    CreationDate (string) -- The date and time when the segment was created.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- The number of channel types in the imported segment.
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- The URL of the S3 bucket that the segment was imported from.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date and time when the segment was last modified.
    Name (string) -- The name of the segment.
    SegmentGroups (dict) -- A segment group, which consists of zero or more source segments, plus dimensions that are applied to those source segments.
    Groups (list) -- A set of segment criteria to evaluate.
    (dict) -- Segment group definition.
    Dimensions (list) -- List of dimensions to include or exclude.
    (dict) -- Segment dimensions
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    
    SourceSegments (list) -- The base segment that you build your segment on. The source segment defines the starting "universe" of endpoints. When you add dimensions to the segment, it filters the source segment based on the dimensions that you specify. You can specify more than one dimensional segment. You can only specify one imported segment. NOTE: If you specify an imported segment for this attribute, the segment size estimate that appears in the Amazon Pinpoint console shows the size of the imported segment, without any filters applied to it.
    (dict) -- Segment reference.
    Id (string) -- A unique identifier for the segment.
    Version (integer) -- If specified contains a specific version of the segment included.
    
    
    
    
    SourceType (string) -- Specify how to handle multiple source segments. For example, if you specify three source segments, should the resulting segment be based on any or all of the segments? Acceptable values: ANY or ALL.
    Type (string) -- Specify how to handle multiple segment dimensions. For example, if you specify three dimensions, should the resulting segment include endpoints that are matched by all, any, or none of the dimensions? Acceptable values: ALL, ANY, or NONE.
    
    
    
    
    Include (string) -- Specify how to handle multiple segment groups. For example, if the segment includes three segment groups, should the resulting segment include endpoints that are matched by all, any, or none of the segment groups you created. Acceptable values: ALL, ANY, or NONE.
    
    
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    NextToken (string) -- An identifier used to retrieve the next page of results. The token is null if no additional pages exist.
    
    
    
    
    
    """
    pass

def get_sms_channel(ApplicationId=None):
    """
    Get an SMS channel.
    See also: AWS API Documentation
    
    
    :example: response = client.get_sms_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'SMSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'PromotionalMessagesPerSecond': 123,
            'SenderId': 'string',
            'ShortCode': 'string',
            'TransactionalMessagesPerSecond': 123,
            'Version': 123
        }
    }
    
    
    """
    pass

def get_user_endpoints(ApplicationId=None, UserId=None):
    """
    Returns information about the endpoints that are associated with a User ID.
    See also: AWS API Documentation
    
    
    :example: response = client.get_user_endpoints(
        ApplicationId='string',
        UserId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type UserId: string
    :param UserId: [REQUIRED] The unique ID of the user.

    :rtype: dict
    :return: {
        'EndpointsResponse': {
            'Item': [
                {
                    'Address': 'string',
                    'ApplicationId': 'string',
                    'Attributes': {
                        'string': [
                            'string',
                        ]
                    },
                    'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'VOICE'|'EMAIL'|'BAIDU'|'CUSTOM',
                    'CohortId': 'string',
                    'CreationDate': 'string',
                    'Demographic': {
                        'AppVersion': 'string',
                        'Locale': 'string',
                        'Make': 'string',
                        'Model': 'string',
                        'ModelVersion': 'string',
                        'Platform': 'string',
                        'PlatformVersion': 'string',
                        'Timezone': 'string'
                    },
                    'EffectiveDate': 'string',
                    'EndpointStatus': 'string',
                    'Id': 'string',
                    'Location': {
                        'City': 'string',
                        'Country': 'string',
                        'Latitude': 123.0,
                        'Longitude': 123.0,
                        'PostalCode': 'string',
                        'Region': 'string'
                    },
                    'Metrics': {
                        'string': 123.0
                    },
                    'OptOut': 'string',
                    'RequestId': 'string',
                    'User': {
                        'UserAttributes': {
                            'string': [
                                'string',
                            ]
                        },
                        'UserId': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    EndpointsResponse (dict) -- List of endpoints
    Item (list) -- The list of endpoints.
    (dict) -- Endpoint response
    Address (string) -- The address of the endpoint as provided by your push provider. For example, the DeviceToken or RegistrationId.
    ApplicationId (string) -- The ID of the application that is associated with the endpoint.
    Attributes (dict) -- Custom attributes that describe the endpoint by associating a name with an array of values. For example, an attribute named "interests" might have the following values: ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    CohortId (string) -- A number from 0-99 that represents the cohort the endpoint is assigned to. Endpoints are grouped into cohorts randomly, and each cohort contains approximately 1 percent of the endpoints for an app. Amazon Pinpoint assigns cohorts to the holdout or treatment allocations for a campaign.
    CreationDate (string) -- The date and time when the endpoint was created, shown in ISO 8601 format.
    Demographic (dict) -- The endpoint demographic attributes.
    AppVersion (string) -- The version of the application associated with the endpoint.
    Locale (string) -- The endpoint locale in the following format: The ISO 639-1 alpha-2 code, followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
    Make (string) -- The manufacturer of the endpoint device, such as Apple or Samsung.
    Model (string) -- The model name or number of the endpoint device, such as iPhone.
    ModelVersion (string) -- The model version of the endpoint device.
    Platform (string) -- The platform of the endpoint device, such as iOS or Android.
    PlatformVersion (string) -- The platform version of the endpoint device.
    Timezone (string) -- The timezone of the endpoint. Specified as a tz database value, such as Americas/Los_Angeles.
    
    
    EffectiveDate (string) -- The date and time when the endpoint was last updated, shown in ISO 8601 format.
    EndpointStatus (string) -- Unused.
    Id (string) -- The unique ID that you assigned to the endpoint. The ID should be a globally unique identifier (GUID) to ensure that it doesn't conflict with other endpoint IDs associated with the application.
    Location (dict) -- The endpoint location attributes.
    City (string) -- The city where the endpoint is located.
    Country (string) -- The two-letter code for the country or region of the endpoint. Specified as an ISO 3166-1 alpha-2 code, such as "US" for the United States.
    Latitude (float) -- The latitude of the endpoint location, rounded to one decimal place.
    Longitude (float) -- The longitude of the endpoint location, rounded to one decimal place.
    PostalCode (string) -- The postal code or zip code of the endpoint.
    Region (string) -- The region of the endpoint location. For example, in the United States, this corresponds to a state.
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint.
    (string) --
    (float) --
    
    
    
    
    OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
    RequestId (string) -- The unique ID for the most recent request to update the endpoint.
    User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
    UserAttributes (dict) -- Custom attributes that describe the user by associating a name with an array of values. For example, an attribute named "interests" might have the following values: ["science", "politics", "travel"]. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    UserId (string) -- The unique ID of the user.
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def get_voice_channel(ApplicationId=None):
    """
    Get a Voice Channel
    See also: AWS API Documentation
    
    
    :example: response = client.get_voice_channel(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'VoiceChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
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

def phone_number_validate(NumberValidateRequest=None):
    """
    Returns information about the specified phone number.
    See also: AWS API Documentation
    
    
    :example: response = client.phone_number_validate(
        NumberValidateRequest={
            'IsoCountryCode': 'string',
            'PhoneNumber': 'string'
        }
    )
    
    
    :type NumberValidateRequest: dict
    :param NumberValidateRequest: [REQUIRED] Phone Number Validate request.
            IsoCountryCode (string) -- (Optional) The two-character ISO country code for the country or region where the phone number was originally registered.
            PhoneNumber (string) -- The phone number to get information about. The phone number that you provide should include a country code. If the number doesn't include a valid country code, the operation might result in an error.
            

    :rtype: dict
    :return: {
        'NumberValidateResponse': {
            'Carrier': 'string',
            'City': 'string',
            'CleansedPhoneNumberE164': 'string',
            'CleansedPhoneNumberNational': 'string',
            'Country': 'string',
            'CountryCodeIso2': 'string',
            'CountryCodeNumeric': 'string',
            'County': 'string',
            'OriginalCountryCodeIso2': 'string',
            'OriginalPhoneNumber': 'string',
            'PhoneType': 'string',
            'PhoneTypeCode': 123,
            'Timezone': 'string',
            'ZipCode': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    NumberValidateResponse (dict) -- Phone Number Validate response.
    Carrier (string) -- The carrier or servive provider that the phone number is currently registered with.
    City (string) -- The city where the phone number was originally registered.
    CleansedPhoneNumberE164 (string) -- The cleansed phone number, shown in E.164 format.
    CleansedPhoneNumberNational (string) -- The cleansed phone number, shown in the local phone number format.
    Country (string) -- The country or region where the phone number was originally registered.
    CountryCodeIso2 (string) -- The two-character ISO code for the country or region where the phone number was originally registered.
    CountryCodeNumeric (string) -- The numeric code for the country or region where the phone number was originally registered.
    County (string) -- The county where the phone number was originally registered.
    OriginalCountryCodeIso2 (string) -- The two-character code (in ISO 3166-1 alpha-2 format) for the country or region in the request body.
    OriginalPhoneNumber (string) -- The phone number that you included in the request body.
    PhoneType (string) -- A description of the phone type. Possible values are MOBILE, LANDLINE, VOIP, INVALID, PREPAID, and OTHER.
    PhoneTypeCode (integer) -- The phone type, represented by an integer. Possible values include 0 (MOBILE), 1 (LANDLINE), 2 (VOIP), 3 (INVALID), 4 (OTHER), and 5 (PREPAID).
    Timezone (string) -- The time zone for the location where the phone number was originally registered.
    ZipCode (string) -- The postal code for the location where the phone number was originally registered.
    
    
    
    
    
    """
    pass

def put_event_stream(ApplicationId=None, WriteEventStream=None):
    """
    Use to create or update the event stream for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.put_event_stream(
        ApplicationId='string',
        WriteEventStream={
            'DestinationStreamArn': 'string',
            'RoleArn': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type WriteEventStream: dict
    :param WriteEventStream: [REQUIRED] Request to save an EventStream.
            DestinationStreamArn (string) -- The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events. Firehose ARN: arn:aws:firehose:REGION:ACCOUNT_ID:deliverystream/STREAM_NAME Kinesis ARN: arn:aws:kinesis:REGION:ACCOUNT_ID:stream/STREAM_NAME
            RoleArn (string) -- The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
            

    :rtype: dict
    :return: {
        'EventStream': {
            'ApplicationId': 'string',
            'DestinationStreamArn': 'string',
            'ExternalId': 'string',
            'LastModifiedDate': 'string',
            'LastUpdatedBy': 'string',
            'RoleArn': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    EventStream (dict) -- Model for an event publishing subscription export.
    ApplicationId (string) -- The ID of the application from which events should be published.
    DestinationStreamArn (string) -- The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events. Firehose ARN: arn:aws:firehose:REGION:ACCOUNT_ID:deliverystream/STREAM_NAME Kinesis ARN: arn:aws:kinesis:REGION:ACCOUNT_ID:stream/STREAM_NAME
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    LastModifiedDate (string) -- The date the event stream was last updated in ISO 8601 format.
    LastUpdatedBy (string) -- The IAM user who last modified the event stream.
    RoleArn (string) -- The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
    
    
    
    
    
    """
    pass

def put_events(ApplicationId=None, EventsRequest=None):
    """
    Use to record events for endpoints. This method creates events and creates or updates the endpoints that those events are associated with.
    See also: AWS API Documentation
    
    
    :example: response = client.put_events(
        ApplicationId='string',
        EventsRequest={
            'BatchItem': {
                'string': {
                    'Endpoint': {
                        'Address': 'string',
                        'Attributes': {
                            'string': [
                                'string',
                            ]
                        },
                        'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'VOICE'|'EMAIL'|'BAIDU'|'CUSTOM',
                        'Demographic': {
                            'AppVersion': 'string',
                            'Locale': 'string',
                            'Make': 'string',
                            'Model': 'string',
                            'ModelVersion': 'string',
                            'Platform': 'string',
                            'PlatformVersion': 'string',
                            'Timezone': 'string'
                        },
                        'EffectiveDate': 'string',
                        'EndpointStatus': 'string',
                        'Location': {
                            'City': 'string',
                            'Country': 'string',
                            'Latitude': 123.0,
                            'Longitude': 123.0,
                            'PostalCode': 'string',
                            'Region': 'string'
                        },
                        'Metrics': {
                            'string': 123.0
                        },
                        'OptOut': 'string',
                        'RequestId': 'string',
                        'User': {
                            'UserAttributes': {
                                'string': [
                                    'string',
                                ]
                            },
                            'UserId': 'string'
                        }
                    },
                    'Events': {
                        'string': {
                            'Attributes': {
                                'string': 'string'
                            },
                            'ClientSdkVersion': 'string',
                            'EventType': 'string',
                            'Metrics': {
                                'string': 123.0
                            },
                            'Session': {
                                'Duration': 123,
                                'Id': 'string',
                                'StartTimestamp': 'string',
                                'StopTimestamp': 'string'
                            },
                            'Timestamp': 'string'
                        }
                    }
                }
            }
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type EventsRequest: dict
    :param EventsRequest: [REQUIRED] A set of events to process.
            BatchItem (dict) -- A batch of events to process. Each BatchItem consists of an endpoint ID as the key, and an EventsBatch object as the value.
            (string) --
            (dict) -- A batch of PublicEndpoints and Events to process.
            Endpoint (dict) -- The PublicEndpoint attached to the EndpointId from the request.
            Address (string) -- The unique identifier for the recipient. For example, an address could be a device token, email address, or mobile phone number.
            Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create a segment.
            (string) --
            (list) --
            (string) --
            
            ChannelType (string) -- The channel type. Valid values: APNS, GCM
            Demographic (dict) -- The endpoint demographic attributes.
            AppVersion (string) -- The version of the application associated with the endpoint.
            Locale (string) -- The endpoint locale in the following format: The ISO 639-1 alpha-2 code, followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
            Make (string) -- The manufacturer of the endpoint device, such as Apple or Samsung.
            Model (string) -- The model name or number of the endpoint device, such as iPhone.
            ModelVersion (string) -- The model version of the endpoint device.
            Platform (string) -- The platform of the endpoint device, such as iOS or Android.
            PlatformVersion (string) -- The platform version of the endpoint device.
            Timezone (string) -- The timezone of the endpoint. Specified as a tz database value, such as Americas/Los_Angeles.
            EffectiveDate (string) -- The date and time when the endpoint was last updated, in ISO 8601 format.
            EndpointStatus (string) -- The status of the endpoint. If the update fails, the value is INACTIVE. If the endpoint is updated successfully, the value is ACTIVE.
            Location (dict) -- The endpoint location attributes.
            City (string) -- The city where the endpoint is located.
            Country (string) -- The two-letter code for the country or region of the endpoint. Specified as an ISO 3166-1 alpha-2 code, such as 'US' for the United States.
            Latitude (float) -- The latitude of the endpoint location, rounded to one decimal place.
            Longitude (float) -- The longitude of the endpoint location, rounded to one decimal place.
            PostalCode (string) -- The postal code or zip code of the endpoint.
            Region (string) -- The region of the endpoint location. For example, in the United States, this corresponds to a state.
            Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint.
            (string) --
            (float) --
            
            OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
            RequestId (string) -- A unique identifier that is generated each time the endpoint is updated.
            User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
            UserAttributes (dict) -- Custom attributes that describe the user by associating a name with an array of values. For example, an attribute named 'interests' might have the following values: ['science', 'politics', 'travel']. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
            (string) --
            (list) --
            (string) --
            
            UserId (string) -- The unique ID of the user.
            
            Events (dict) -- An object that contains a set of events associated with the endpoint.
            (string) --
            (dict) -- Model for creating or updating events.
            Attributes (dict) -- Custom attributes that are associated with the event you're adding or updating.
            (string) --
            (string) --
            
            ClientSdkVersion (string) -- The version of the SDK that's running on the client device.
            EventType (string) -- The name of the custom event that you're recording.
            Metrics (dict) -- Custom metrics related to the event.
            (string) --
            (float) --
            
            Session (dict) -- Information about the session in which the event occurred.
            Duration (integer) -- The duration of the session, in milliseconds.
            Id (string) -- A unique identifier for the session.
            StartTimestamp (string) -- The date and time when the session began.
            StopTimestamp (string) -- The date and time when the session ended.
            Timestamp (string) -- The date and time when the event occurred, in ISO 8601 format.
            
            
            
            

    :rtype: dict
    :return: {
        'EventsResponse': {
            'Results': {
                'string': {
                    'EndpointItemResponse': {
                        'Message': 'string',
                        'StatusCode': 123
                    },
                    'EventsItemResponse': {
                        'string': {
                            'Message': 'string',
                            'StatusCode': 123
                        }
                    }
                }
            }
        }
    }
    
    
    :returns: 
    (dict) -- 202 response
    EventsResponse (dict) -- Custom messages associated with events.
    Results (dict) -- A map that contains a multipart response for each endpoint. Each item in this object uses the endpoint ID as the key, and the item response as the value. If no item response exists, the value can also be one of the following: 202 (if the request was processed successfully) or 400 (if the payload was invalid, or required fields were missing).
    (string) --
    (dict) -- The response that's provided after registering the endpoint.
    EndpointItemResponse (dict) -- The response received after the endpoint was accepted.
    Message (string) -- A custom message associated with the registration of an endpoint when issuing a response.
    StatusCode (integer) -- The status code associated with the merging of an endpoint when issuing a response.
    
    
    EventsItemResponse (dict) -- A multipart response object that contains a key and value for each event ID in the request. In each object, the event ID is the key, and an EventItemResponse object is the value.
    (string) --
    (dict) -- A complex object that holds the status code and message as a result of processing an event.
    Message (string) -- A custom message that is associated with the processing of an event.
    StatusCode (integer) -- The status returned in the response as a result of processing the event. Possible values: 400 (for invalid events) and 202 (for events that were accepted).
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def remove_attributes(ApplicationId=None, AttributeType=None, UpdateAttributesRequest=None):
    """
    Used to remove the attributes for an app
    See also: AWS API Documentation
    
    
    :example: response = client.remove_attributes(
        ApplicationId='string',
        AttributeType='string',
        UpdateAttributesRequest={
            'Blacklist': [
                'string',
            ]
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type AttributeType: string
    :param AttributeType: [REQUIRED] Type of attribute. Can be endpoint-custom-attributes, endpoint-custom-metrics, endpoint-user-attributes.

    :type UpdateAttributesRequest: dict
    :param UpdateAttributesRequest: [REQUIRED] Update attributes request
            Blacklist (list) -- The GLOB wildcard for removing the attributes in the application
            (string) --
            

    :rtype: dict
    :return: {
        'AttributesResource': {
            'ApplicationId': 'string',
            'AttributeType': 'string',
            'Attributes': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    AttributesResource (dict) -- Attributes.
    ApplicationId (string) -- The unique ID for the application.
    AttributeType (string) -- The attribute type for the application.
    Attributes (list) -- The attributes for the application.
    (string) --
    
    
    
    
    
    
    
    """
    pass

def send_messages(ApplicationId=None, MessageRequest=None):
    """
    Used to send a direct message.
    See also: AWS API Documentation
    
    
    :example: response = client.send_messages(
        ApplicationId='string',
        MessageRequest={
            'Addresses': {
                'string': {
                    'BodyOverride': 'string',
                    'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'VOICE'|'EMAIL'|'BAIDU'|'CUSTOM',
                    'Context': {
                        'string': 'string'
                    },
                    'RawContent': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TitleOverride': 'string'
                }
            },
            'Context': {
                'string': 'string'
            },
            'Endpoints': {
                'string': {
                    'BodyOverride': 'string',
                    'Context': {
                        'string': 'string'
                    },
                    'RawContent': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TitleOverride': 'string'
                }
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ConsolidationKey': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'ExpiresAfter': 'string',
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'MD5': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Badge': 123,
                    'Body': 'string',
                    'Category': 'string',
                    'CollapseId': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'MediaUrl': 'string',
                    'PreferredAuthenticationMethod': 'string',
                    'Priority': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'ThreadId': 'string',
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Body': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'DefaultPushNotificationMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'SilentPush': True|False,
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FeedbackForwardingAddress': 'string',
                    'FromAddress': 'string',
                    'RawEmail': {
                        'Data': b'bytes'
                    },
                    'ReplyToAddresses': [
                        'string',
                    ],
                    'SimpleEmail': {
                        'HtmlPart': {
                            'Charset': 'string',
                            'Data': 'string'
                        },
                        'Subject': {
                            'Charset': 'string',
                            'Data': 'string'
                        },
                        'TextPart': {
                            'Charset': 'string',
                            'Data': 'string'
                        }
                    },
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'CollapseKey': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'Priority': 'string',
                    'RawContent': 'string',
                    'RestrictedPackageName': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'Keyword': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'OriginationNumber': 'string',
                    'SenderId': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'VoiceMessage': {
                    'Body': 'string',
                    'LanguageCode': 'string',
                    'OriginationNumber': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'VoiceId': 'string'
                }
            },
            'TraceId': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type MessageRequest: dict
    :param MessageRequest: [REQUIRED] Send message request.
            Addresses (dict) -- A map of key-value pairs, where each key is an address and each value is an AddressConfiguration object. An address can be a push notification token, a phone number, or an email address.
            (string) --
            (dict) -- Address configuration.
            BodyOverride (string) -- Body override. If specified will override default body.
            ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
            Context (dict) -- A map of custom attributes to attributes to be attached to the message for this address. This payload is added to the push notification's 'data.pinpoint' object or added to the email/sms delivery receipt event attributes.
            (string) --
            (string) --
            
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            Substitutions (dict) -- A map of substitution values for the message to be merged with the DefaultMessage's substitutions. Substitutions on this map take precedence over the all other substitutions.
            (string) --
            (list) --
            (string) --
            
            TitleOverride (string) -- Title override. If specified will override default title if applicable.
            
            Context (dict) -- A map of custom attributes to attributes to be attached to the message. This payload is added to the push notification's 'data.pinpoint' object or added to the email/sms delivery receipt event attributes.
            (string) --
            (string) --
            
            Endpoints (dict) -- A map of key-value pairs, where each key is an endpoint ID and each value is an EndpointSendConfiguration object. Within an EndpointSendConfiguration object, you can tailor the message for an endpoint by specifying message overrides or substitutions.
            (string) --
            (dict) -- Endpoint send configuration.
            BodyOverride (string) -- Body override. If specified will override default body.
            Context (dict) -- A map of custom attributes to attributes to be attached to the message for this address. This payload is added to the push notification's 'data.pinpoint' object or added to the email/sms delivery receipt event attributes.
            (string) --
            (string) --
            
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            Substitutions (dict) -- A map of substitution values for the message to be merged with the DefaultMessage's substitutions. Substitutions on this map take precedence over the all other substitutions.
            (string) --
            (list) --
            (string) --
            
            TitleOverride (string) -- Title override. If specified will override default title if applicable.
            
            MessageConfiguration (dict) -- Message configuration.
            ADMMessage (dict) -- The message to ADM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification.
            ConsolidationKey (string) -- Optional. Arbitrary string used to indicate multiple messages are logically the same and that ADM is allowed to drop previously enqueued messages in favor of this one.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            ExpiresAfter (string) -- Optional. Number of seconds ADM should retain the message if the device is offline
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            MD5 (string) -- Optional. Base-64-encoded MD5 checksum of the data parameter. Used to verify data integrity
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message to APNS channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Badge (integer) -- Include this key when you want the system to modify the badge of your app icon. If this key is not included in the dictionary, the badge is not changed. To remove the badge, set the value of this key to 0.
            Body (string) -- The message body of the notification.
            Category (string) -- Provide this key with a string value that represents the notification's type. This value corresponds to the value in the identifier property of one of your app's registered categories.
            CollapseId (string) -- An ID that, if assigned to multiple messages, causes APNs to coalesce the messages into a single push notification instead of delivering each message individually. The value must not exceed 64 bytes. Amazon Pinpoint uses this value to set the apns-collapse-id request header when it sends the message to APNs.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            PreferredAuthenticationMethod (string) -- The preferred authentication method, either 'CERTIFICATE' or 'TOKEN'
            Priority (string) -- The message priority. Amazon Pinpoint uses this value to set the apns-priority request header when it sends the message to APNs. Accepts the following values: '5' - Low priority. Messages might be delayed, delivered in groups, and throttled. '10' - High priority. Messages are sent immediately. High priority messages must cause an alert, sound, or badge on the receiving device. The default value is '10'. The equivalent values for FCM or GCM messages are 'normal' and 'high'. Amazon Pinpoint accepts these values for APNs messages and converts them. For more information about the apns-priority parameter, see Communicating with APNs in the APNs Local and Remote Notification Programming Guide.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Sound (string) -- Include this key when you want the system to play a sound. The value of this key is the name of a sound file in your app's main bundle or in the Library/Sounds folder of your app's data container. If the sound file cannot be found, or if you specify defaultfor the value, the system plays the default alert sound.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            ThreadId (string) -- Provide this key with a string value that represents the app-specific identifier for grouping notifications. If you provide a Notification Content app extension, you can use this value to group your notifications together.
            TimeToLive (integer) -- The length of time (in seconds) that APNs stores and attempts to deliver the message. If the value is 0, APNs does not store the message or attempt to deliver it more than once. Amazon Pinpoint uses this value to set the apns-expiration request header when it sends the message to APNs.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message to Baidu GCM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept in Baidu storage if the device is offline. The and the default value and the maximum time to live supported is 7 days (604800 seconds)
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Body (string) -- The message body of the notification, the email body or the text message.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            
            DefaultPushNotificationMessage (dict) -- The default push notification message for all push channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            SilentPush (boolean) -- Indicates if the message should display on the recipient's device. You can use silent pushes for remote configuration or to deliver messages to in-app notification centers.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            EmailMessage (dict) -- The message to Email channels. Overrides the default message.
            Body (string) -- The body of the email message.
            FeedbackForwardingAddress (string) -- The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled.
            FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
            RawEmail (dict) -- An email represented as a raw MIME message.
            Data (bytes) -- The raw email message itself. Then entire message must be base64-encoded.
            ReplyToAddresses (list) -- The reply-to email address(es) for the email. If the recipient replies to the email, each reply-to address will receive the reply.
            (string) --
            SimpleEmail (dict) -- An email composed of a subject, a text part and a html part.
            HtmlPart (dict) -- The content of the message, in HTML format. Use this for email clients that can process HTML. You can include clickable links, formatted text, and much more in an HTML message.
            Charset (string) -- The character set of the content.
            Data (string) -- The textual data of the content.
            Subject (dict) -- The subject of the message: A short summary of the content, which will appear in the recipient's inbox.
            Charset (string) -- The character set of the content.
            Data (string) -- The textual data of the content.
            TextPart (dict) -- The content of the message, in text format. Use this for text-based email clients, or clients on high-latency networks (such as mobile devices).
            Charset (string) -- The character set of the content.
            Data (string) -- The textual data of the content.
            
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            
            GCMMessage (dict) -- The message to GCM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification.
            CollapseKey (string) -- This parameter identifies a group of messages (e.g., with collapse_key: 'Updates Available') that can be collapsed, so that only the last message gets sent when delivery can be resumed. This is intended to avoid sending too many of the same messages when the device comes back online or becomes active.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            Priority (string) -- The message priority. Amazon Pinpoint uses this value to set the FCM or GCM priority parameter when it sends the message. Accepts the following values: 'Normal' - Messages might be delayed. Delivery is optimized for battery usage on the receiving device. Use normal priority unless immediate delivery is required. 'High' - Messages are sent immediately and might wake a sleeping device. The equivalent values for APNs messages are '5' and '10'. Amazon Pinpoint accepts these values here and converts them. For more information, see About FCM Messages in the Firebase documentation.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            RestrictedPackageName (string) -- This parameter specifies the package name of the application where the registration tokens must match in order to receive the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            TimeToLive (integer) -- The length of time (in seconds) that FCM or GCM stores and attempts to deliver the message. If unspecified, the value defaults to the maximum, which is 2,419,200 seconds (28 days). Amazon Pinpoint uses this value to set the FCM or GCM time_to_live parameter.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The message to SMS channels. Overrides the default message.
            Body (string) -- The body of the SMS message.
            Keyword (string) -- The SMS program name that you provided to AWS Support when you requested your dedicated number.
            MessageType (string) -- Is this a transaction priority message or lower priority.
            OriginationNumber (string) -- The phone number that the SMS message originates from. Specify one of the dedicated long codes or short codes that you requested from AWS Support and that is assigned to your account. If this attribute is not specified, Amazon Pinpoint randomly assigns a long code.
            SenderId (string) -- The sender ID that is shown as the message sender on the recipient's device. Support for sender IDs varies by country or region.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            
            VoiceMessage (dict) -- The message to Voice channels. Overrides the default message.
            Body (string) -- The message body of the notification, the email body or the text message.
            LanguageCode (string) -- Language of sent message
            OriginationNumber (string) -- Is the number from the pool or messaging service to send from.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            VoiceId (string) -- Voice ID of sent message.
            
            TraceId (string) -- A unique ID that you can use to trace a message. This ID is visible to recipients.
            

    :rtype: dict
    :return: {
        'MessageResponse': {
            'ApplicationId': 'string',
            'EndpointResult': {
                'string': {
                    'Address': 'string',
                    'DeliveryStatus': 'SUCCESSFUL'|'THROTTLED'|'TEMPORARY_FAILURE'|'PERMANENT_FAILURE'|'UNKNOWN_FAILURE'|'OPT_OUT'|'DUPLICATE',
                    'MessageId': 'string',
                    'StatusCode': 123,
                    'StatusMessage': 'string',
                    'UpdatedToken': 'string'
                }
            },
            'RequestId': 'string',
            'Result': {
                'string': {
                    'DeliveryStatus': 'SUCCESSFUL'|'THROTTLED'|'TEMPORARY_FAILURE'|'PERMANENT_FAILURE'|'UNKNOWN_FAILURE'|'OPT_OUT'|'DUPLICATE',
                    'MessageId': 'string',
                    'StatusCode': 123,
                    'StatusMessage': 'string',
                    'UpdatedToken': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    MessageResponse (dict) -- Send message response.
    ApplicationId (string) -- Application id of the message.
    EndpointResult (dict) -- A map containing a multi part response for each address, with the endpointId as the key and the result as the value.
    (string) --
    (dict) -- The result from sending a message to an endpoint.
    Address (string) -- Address that endpoint message was delivered to.
    DeliveryStatus (string) -- The delivery status of the message. Possible values: SUCCESS - The message was successfully delivered to the endpoint. TRANSIENT_FAILURE - A temporary error occurred. Amazon Pinpoint will attempt to deliver the message again later. FAILURE_PERMANENT - An error occurred when delivering the message to the endpoint. Amazon Pinpoint won't attempt to send the message again. TIMEOUT - The message couldn't be sent within the timeout period. QUIET_TIME - The local time for the endpoint was within the QuietTime for the campaign or app. DAILY_CAP - The endpoint has received the maximum number of messages it can receive within a 24-hour period. HOLDOUT - The endpoint was in a hold out treatment for the campaign. THROTTLED - Amazon Pinpoint throttled sending to this endpoint. EXPIRED - The endpoint address is expired. CAMPAIGN_CAP - The endpoint received the maximum number of messages allowed by the campaign. SERVICE_FAILURE - A service-level failure prevented Amazon Pinpoint from delivering the message. UNKNOWN - An unknown error occurred.
    MessageId (string) -- Unique message identifier associated with the message that was sent.
    StatusCode (integer) -- Downstream service status code.
    StatusMessage (string) -- Status message for message delivery.
    UpdatedToken (string) -- If token was updated as part of delivery. (This is GCM Specific)
    
    
    
    
    
    
    RequestId (string) -- Original request Id for which this message was delivered.
    Result (dict) -- A map containing a multi part response for each address, with the address as the key(Email address, phone number or push token) and the result as the value.
    (string) --
    (dict) -- The result from sending a message to an address.
    DeliveryStatus (string) -- The delivery status of the message. Possible values: SUCCESS - The message was successfully delivered to the endpoint. TRANSIENT_FAILURE - A temporary error occurred. Amazon Pinpoint will attempt to deliver the message again later. FAILURE_PERMANENT - An error occurred when delivering the message to the endpoint. Amazon Pinpoint won't attempt to send the message again. TIMEOUT - The message couldn't be sent within the timeout period. QUIET_TIME - The local time for the endpoint was within the QuietTime for the campaign or app. DAILY_CAP - The endpoint has received the maximum number of messages it can receive within a 24-hour period. HOLDOUT - The endpoint was in a hold out treatment for the campaign. THROTTLED - Amazon Pinpoint throttled sending to this endpoint. EXPIRED - The endpoint address is expired. CAMPAIGN_CAP - The endpoint received the maximum number of messages allowed by the campaign. SERVICE_FAILURE - A service-level failure prevented Amazon Pinpoint from delivering the message. UNKNOWN - An unknown error occurred.
    MessageId (string) -- Unique message identifier associated with the message that was sent.
    StatusCode (integer) -- Downstream service status code.
    StatusMessage (string) -- Status message for message delivery.
    UpdatedToken (string) -- If token was updated as part of delivery. (This is GCM Specific)
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def send_users_messages(ApplicationId=None, SendUsersMessageRequest=None):
    """
    Used to send a message to a list of users.
    See also: AWS API Documentation
    
    
    :example: response = client.send_users_messages(
        ApplicationId='string',
        SendUsersMessageRequest={
            'Context': {
                'string': 'string'
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ConsolidationKey': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'ExpiresAfter': 'string',
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'MD5': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Badge': 123,
                    'Body': 'string',
                    'Category': 'string',
                    'CollapseId': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'MediaUrl': 'string',
                    'PreferredAuthenticationMethod': 'string',
                    'Priority': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'ThreadId': 'string',
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Body': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'DefaultPushNotificationMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'SilentPush': True|False,
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FeedbackForwardingAddress': 'string',
                    'FromAddress': 'string',
                    'RawEmail': {
                        'Data': b'bytes'
                    },
                    'ReplyToAddresses': [
                        'string',
                    ],
                    'SimpleEmail': {
                        'HtmlPart': {
                            'Charset': 'string',
                            'Data': 'string'
                        },
                        'Subject': {
                            'Charset': 'string',
                            'Data': 'string'
                        },
                        'TextPart': {
                            'Charset': 'string',
                            'Data': 'string'
                        }
                    },
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'CollapseKey': 'string',
                    'Data': {
                        'string': 'string'
                    },
                    'IconReference': 'string',
                    'ImageIconUrl': 'string',
                    'ImageUrl': 'string',
                    'Priority': 'string',
                    'RawContent': 'string',
                    'RestrictedPackageName': 'string',
                    'SilentPush': True|False,
                    'SmallImageIconUrl': 'string',
                    'Sound': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'Keyword': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'OriginationNumber': 'string',
                    'SenderId': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'VoiceMessage': {
                    'Body': 'string',
                    'LanguageCode': 'string',
                    'OriginationNumber': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'VoiceId': 'string'
                }
            },
            'TraceId': 'string',
            'Users': {
                'string': {
                    'BodyOverride': 'string',
                    'Context': {
                        'string': 'string'
                    },
                    'RawContent': 'string',
                    'Substitutions': {
                        'string': [
                            'string',
                        ]
                    },
                    'TitleOverride': 'string'
                }
            }
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type SendUsersMessageRequest: dict
    :param SendUsersMessageRequest: [REQUIRED] Send message request.
            Context (dict) -- A map of custom attribute-value pairs. Amazon Pinpoint adds these attributes to the data.pinpoint object in the body of the push notification payload. Amazon Pinpoint also provides these attributes in the events that it generates for users-messages deliveries.
            (string) --
            (string) --
            
            MessageConfiguration (dict) -- Message definitions for the default message and any messages that are tailored for specific channels.
            ADMMessage (dict) -- The message to ADM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification.
            ConsolidationKey (string) -- Optional. Arbitrary string used to indicate multiple messages are logically the same and that ADM is allowed to drop previously enqueued messages in favor of this one.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            ExpiresAfter (string) -- Optional. Number of seconds ADM should retain the message if the device is offline
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            MD5 (string) -- Optional. Base-64-encoded MD5 checksum of the data parameter. Used to verify data integrity
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message to APNS channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Badge (integer) -- Include this key when you want the system to modify the badge of your app icon. If this key is not included in the dictionary, the badge is not changed. To remove the badge, set the value of this key to 0.
            Body (string) -- The message body of the notification.
            Category (string) -- Provide this key with a string value that represents the notification's type. This value corresponds to the value in the identifier property of one of your app's registered categories.
            CollapseId (string) -- An ID that, if assigned to multiple messages, causes APNs to coalesce the messages into a single push notification instead of delivering each message individually. The value must not exceed 64 bytes. Amazon Pinpoint uses this value to set the apns-collapse-id request header when it sends the message to APNs.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            PreferredAuthenticationMethod (string) -- The preferred authentication method, either 'CERTIFICATE' or 'TOKEN'
            Priority (string) -- The message priority. Amazon Pinpoint uses this value to set the apns-priority request header when it sends the message to APNs. Accepts the following values: '5' - Low priority. Messages might be delayed, delivered in groups, and throttled. '10' - High priority. Messages are sent immediately. High priority messages must cause an alert, sound, or badge on the receiving device. The default value is '10'. The equivalent values for FCM or GCM messages are 'normal' and 'high'. Amazon Pinpoint accepts these values for APNs messages and converts them. For more information about the apns-priority parameter, see Communicating with APNs in the APNs Local and Remote Notification Programming Guide.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            Sound (string) -- Include this key when you want the system to play a sound. The value of this key is the name of a sound file in your app's main bundle or in the Library/Sounds folder of your app's data container. If the sound file cannot be found, or if you specify defaultfor the value, the system plays the default alert sound.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            ThreadId (string) -- Provide this key with a string value that represents the app-specific identifier for grouping notifications. If you provide a Notification Content app extension, you can use this value to group your notifications together.
            TimeToLive (integer) -- The length of time (in seconds) that APNs stores and attempts to deliver the message. If the value is 0, APNs does not store the message or attempt to deliver it more than once. Amazon Pinpoint uses this value to set the apns-expiration request header when it sends the message to APNs.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message to Baidu GCM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept in Baidu storage if the device is offline. The and the default value and the maximum time to live supported is 7 days (604800 seconds)
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Body (string) -- The message body of the notification, the email body or the text message.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            
            DefaultPushNotificationMessage (dict) -- The default push notification message for all push channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            SilentPush (boolean) -- Indicates if the message should display on the recipient's device. You can use silent pushes for remote configuration or to deliver messages to in-app notification centers.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            EmailMessage (dict) -- The message to Email channels. Overrides the default message.
            Body (string) -- The body of the email message.
            FeedbackForwardingAddress (string) -- The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled.
            FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
            RawEmail (dict) -- An email represented as a raw MIME message.
            Data (bytes) -- The raw email message itself. Then entire message must be base64-encoded.
            ReplyToAddresses (list) -- The reply-to email address(es) for the email. If the recipient replies to the email, each reply-to address will receive the reply.
            (string) --
            SimpleEmail (dict) -- An email composed of a subject, a text part and a html part.
            HtmlPart (dict) -- The content of the message, in HTML format. Use this for email clients that can process HTML. You can include clickable links, formatted text, and much more in an HTML message.
            Charset (string) -- The character set of the content.
            Data (string) -- The textual data of the content.
            Subject (dict) -- The subject of the message: A short summary of the content, which will appear in the recipient's inbox.
            Charset (string) -- The character set of the content.
            Data (string) -- The textual data of the content.
            TextPart (dict) -- The content of the message, in text format. Use this for text-based email clients, or clients on high-latency networks (such as mobile devices).
            Charset (string) -- The character set of the content.
            Data (string) -- The textual data of the content.
            
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            
            GCMMessage (dict) -- The message to GCM channels. Overrides the default push notification message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
            Body (string) -- The message body of the notification.
            CollapseKey (string) -- This parameter identifies a group of messages (e.g., with collapse_key: 'Updates Available') that can be collapsed, so that only the last message gets sent when delivery can be resumed. This is intended to avoid sending too many of the same messages when the device comes back online or becomes active.
            Data (dict) -- The data payload used for a silent push. This payload is added to the notifications' data.pinpoint.jsonBody' object
            (string) --
            (string) --
            
            IconReference (string) -- The icon image name of the asset saved in your application.
            ImageIconUrl (string) -- The URL that points to an image used as the large icon to the notification content view.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            Priority (string) -- The message priority. Amazon Pinpoint uses this value to set the FCM or GCM priority parameter when it sends the message. Accepts the following values: 'Normal' - Messages might be delayed. Delivery is optimized for battery usage on the receiving device. Use normal priority unless immediate delivery is required. 'High' - Messages are sent immediately and might wake a sleeping device. The equivalent values for APNs messages are '5' and '10'. Amazon Pinpoint accepts these values here and converts them. For more information, see About FCM Messages in the Firebase documentation.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            RestrictedPackageName (string) -- This parameter specifies the package name of the application where the registration tokens must match in order to receive the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            SmallImageIconUrl (string) -- The URL that points to an image used as the small icon for the notification which will be used to represent the notification in the status bar and content view
            Sound (string) -- Indicates a sound to play when the device receives the notification. Supports default, or the filename of a sound resource bundled in the app. Android sound files must reside in /res/raw/
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            TimeToLive (integer) -- The length of time (in seconds) that FCM or GCM stores and attempts to deliver the message. If unspecified, the value defaults to the maximum, which is 2,419,200 seconds (28 days). Amazon Pinpoint uses this value to set the FCM or GCM time_to_live parameter.
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The message to SMS channels. Overrides the default message.
            Body (string) -- The body of the SMS message.
            Keyword (string) -- The SMS program name that you provided to AWS Support when you requested your dedicated number.
            MessageType (string) -- Is this a transaction priority message or lower priority.
            OriginationNumber (string) -- The phone number that the SMS message originates from. Specify one of the dedicated long codes or short codes that you requested from AWS Support and that is assigned to your account. If this attribute is not specified, Amazon Pinpoint randomly assigns a long code.
            SenderId (string) -- The sender ID that is shown as the message sender on the recipient's device. Support for sender IDs varies by country or region.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            
            VoiceMessage (dict) -- The message to Voice channels. Overrides the default message.
            Body (string) -- The message body of the notification, the email body or the text message.
            LanguageCode (string) -- Language of sent message
            OriginationNumber (string) -- Is the number from the pool or messaging service to send from.
            Substitutions (dict) -- Default message substitutions. Can be overridden by individual address substitutions.
            (string) --
            (list) --
            (string) --
            
            VoiceId (string) -- Voice ID of sent message.
            
            TraceId (string) -- A unique ID that you can use to trace a message. This ID is visible to recipients.
            Users (dict) -- A map that associates user IDs with EndpointSendConfiguration objects. Within an EndpointSendConfiguration object, you can tailor the message for a user by specifying message overrides or substitutions.
            (string) --
            (dict) -- Endpoint send configuration.
            BodyOverride (string) -- Body override. If specified will override default body.
            Context (dict) -- A map of custom attributes to attributes to be attached to the message for this address. This payload is added to the push notification's 'data.pinpoint' object or added to the email/sms delivery receipt event attributes.
            (string) --
            (string) --
            
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            Substitutions (dict) -- A map of substitution values for the message to be merged with the DefaultMessage's substitutions. Substitutions on this map take precedence over the all other substitutions.
            (string) --
            (list) --
            (string) --
            
            TitleOverride (string) -- Title override. If specified will override default title if applicable.
            
            

    :rtype: dict
    :return: {
        'SendUsersMessageResponse': {
            'ApplicationId': 'string',
            'RequestId': 'string',
            'Result': {
                'string': {
                    'string': {
                        'Address': 'string',
                        'DeliveryStatus': 'SUCCESSFUL'|'THROTTLED'|'TEMPORARY_FAILURE'|'PERMANENT_FAILURE'|'UNKNOWN_FAILURE'|'OPT_OUT'|'DUPLICATE',
                        'MessageId': 'string',
                        'StatusCode': 123,
                        'StatusMessage': 'string',
                        'UpdatedToken': 'string'
                    }
                }
            }
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SendUsersMessageResponse (dict) -- User send message response.
    ApplicationId (string) -- The unique ID of the Amazon Pinpoint project used to send the message.
    RequestId (string) -- The unique ID assigned to the users-messages request.
    Result (dict) -- An object that shows the endpoints that were messaged for each user. The object provides a list of user IDs. For each user ID, it provides the endpoint IDs that were messaged. For each endpoint ID, it provides an EndpointMessageResult object.
    (string) --
    (dict) --
    (string) --
    (dict) -- The result from sending a message to an endpoint.
    Address (string) -- Address that endpoint message was delivered to.
    DeliveryStatus (string) -- The delivery status of the message. Possible values: SUCCESS - The message was successfully delivered to the endpoint. TRANSIENT_FAILURE - A temporary error occurred. Amazon Pinpoint will attempt to deliver the message again later. FAILURE_PERMANENT - An error occurred when delivering the message to the endpoint. Amazon Pinpoint won't attempt to send the message again. TIMEOUT - The message couldn't be sent within the timeout period. QUIET_TIME - The local time for the endpoint was within the QuietTime for the campaign or app. DAILY_CAP - The endpoint has received the maximum number of messages it can receive within a 24-hour period. HOLDOUT - The endpoint was in a hold out treatment for the campaign. THROTTLED - Amazon Pinpoint throttled sending to this endpoint. EXPIRED - The endpoint address is expired. CAMPAIGN_CAP - The endpoint received the maximum number of messages allowed by the campaign. SERVICE_FAILURE - A service-level failure prevented Amazon Pinpoint from delivering the message. UNKNOWN - An unknown error occurred.
    MessageId (string) -- Unique message identifier associated with the message that was sent.
    StatusCode (integer) -- Downstream service status code.
    StatusMessage (string) -- Status message for message delivery.
    UpdatedToken (string) -- If token was updated as part of delivery. (This is GCM Specific)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def update_adm_channel(ADMChannelRequest=None, ApplicationId=None):
    """
    Update an ADM channel.
    See also: AWS API Documentation
    
    
    :example: response = client.update_adm_channel(
        ADMChannelRequest={
            'ClientId': 'string',
            'ClientSecret': 'string',
            'Enabled': True|False
        },
        ApplicationId='string'
    )
    
    
    :type ADMChannelRequest: dict
    :param ADMChannelRequest: [REQUIRED] Amazon Device Messaging channel definition.
            ClientId (string) -- The Client ID that you obtained from the Amazon App Distribution Portal.
            ClientSecret (string) -- The Client Secret that you obtained from the Amazon App Distribution Portal.
            Enabled (boolean) -- Indicates whether or not the channel is enabled for sending messages.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'ADMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ADMChannelResponse (dict) -- Amazon Device Messaging channel definition.
    ApplicationId (string) -- The ID of the application to which the channel applies.
    CreationDate (string) -- The date and time when this channel was created.
    Enabled (boolean) -- Indicates whether or not the channel is enabled for sending messages.
    HasCredential (boolean) -- Not used. Retained for backwards compatibility.
    Id (string) -- (Deprecated) An identifier for the channel. Retained for backwards compatibility.
    IsArchived (boolean) -- Indicates whether or not the channel is archived.
    LastModifiedBy (string) -- The user who last updated this channel.
    LastModifiedDate (string) -- The date and time when this channel was last modified.
    Platform (string) -- The platform type. For this channel, the value is always "ADM."
    Version (integer) -- The channel version.
    
    
    
    
    
    """
    pass

def update_apns_channel(APNSChannelRequest=None, ApplicationId=None):
    """
    Use to update the APNs channel for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.update_apns_channel(
        APNSChannelRequest={
            'BundleId': 'string',
            'Certificate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'PrivateKey': 'string',
            'TeamId': 'string',
            'TokenKey': 'string',
            'TokenKeyId': 'string'
        },
        ApplicationId='string'
    )
    
    
    :type APNSChannelRequest: dict
    :param APNSChannelRequest: [REQUIRED] Apple Push Notification Service channel definition.
            BundleId (string) -- The bundle id used for APNs Tokens.
            Certificate (string) -- The distribution certificate from Apple.
            DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            PrivateKey (string) -- The certificate private key.
            TeamId (string) -- The team id used for APNs Tokens.
            TokenKey (string) -- The token key used for APNs Tokens.
            TokenKeyId (string) -- The token key used for APNs Tokens.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    APNSChannelResponse (dict) -- Apple Distribution Push Notification Service channel definition.
    ApplicationId (string) -- The ID of the application that the channel applies to.
    CreationDate (string) -- The date and time when this channel was created.
    DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Not used. Retained for backwards compatibility.
    HasTokenKey (boolean) -- Indicates whether the channel is configured with a key for APNs token authentication. Provide a token key by setting the TokenKey attribute.
    Id (string) -- (Deprecated) An identifier for the channel. Retained for backwards compatibility.
    IsArchived (boolean) -- Indicates whether or not the channel is archived.
    LastModifiedBy (string) -- The user who last updated this channel.
    LastModifiedDate (string) -- The date and time when this channel was last modified.
    Platform (string) -- The platform type. For this channel, the value is always "ADM."
    Version (integer) -- The channel version.
    
    
    
    
    
    """
    pass

def update_apns_sandbox_channel(APNSSandboxChannelRequest=None, ApplicationId=None):
    """
    Update an APNS sandbox channel.
    See also: AWS API Documentation
    
    
    :example: response = client.update_apns_sandbox_channel(
        APNSSandboxChannelRequest={
            'BundleId': 'string',
            'Certificate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'PrivateKey': 'string',
            'TeamId': 'string',
            'TokenKey': 'string',
            'TokenKeyId': 'string'
        },
        ApplicationId='string'
    )
    
    
    :type APNSSandboxChannelRequest: dict
    :param APNSSandboxChannelRequest: [REQUIRED] Apple Development Push Notification Service channel definition.
            BundleId (string) -- The bundle id used for APNs Tokens.
            Certificate (string) -- The distribution certificate from Apple.
            DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            PrivateKey (string) -- The certificate private key.
            TeamId (string) -- The team id used for APNs Tokens.
            TokenKey (string) -- The token key used for APNs Tokens.
            TokenKeyId (string) -- The token key used for APNs Tokens.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    APNSSandboxChannelResponse (dict) -- Apple Development Push Notification Service channel definition.
    ApplicationId (string) -- The ID of the application to which the channel applies.
    CreationDate (string) -- When was this segment created
    DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Not used. Retained for backwards compatibility.
    HasTokenKey (boolean) -- Indicates whether the channel is configured with a key for APNs token authentication. Provide a token key by setting the TokenKey attribute.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be APNS_SANDBOX.
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_apns_voip_channel(APNSVoipChannelRequest=None, ApplicationId=None):
    """
    Update an APNS VoIP channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_apns_voip_channel(
        APNSVoipChannelRequest={
            'BundleId': 'string',
            'Certificate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'PrivateKey': 'string',
            'TeamId': 'string',
            'TokenKey': 'string',
            'TokenKeyId': 'string'
        },
        ApplicationId='string'
    )
    
    
    :type APNSVoipChannelRequest: dict
    :param APNSVoipChannelRequest: [REQUIRED] Apple VoIP Push Notification Service channel definition.
            BundleId (string) -- The bundle id used for APNs Tokens.
            Certificate (string) -- The distribution certificate from Apple.
            DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            PrivateKey (string) -- The certificate private key.
            TeamId (string) -- The team id used for APNs Tokens.
            TokenKey (string) -- The token key used for APNs Tokens.
            TokenKeyId (string) -- The token key used for APNs Tokens.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSVoipChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    APNSVoipChannelResponse (dict) -- Apple VoIP Push Notification Service channel definition.
    ApplicationId (string) -- Application id
    CreationDate (string) -- When was this segment created
    DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Not used. Retained for backwards compatibility.
    HasTokenKey (boolean) -- If the channel is registered with a token key for authentication.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who made the last change
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be APNS.
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_apns_voip_sandbox_channel(APNSVoipSandboxChannelRequest=None, ApplicationId=None):
    """
    Update an APNS VoIP sandbox channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_apns_voip_sandbox_channel(
        APNSVoipSandboxChannelRequest={
            'BundleId': 'string',
            'Certificate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'PrivateKey': 'string',
            'TeamId': 'string',
            'TokenKey': 'string',
            'TokenKeyId': 'string'
        },
        ApplicationId='string'
    )
    
    
    :type APNSVoipSandboxChannelRequest: dict
    :param APNSVoipSandboxChannelRequest: [REQUIRED] Apple VoIP Developer Push Notification Service channel definition.
            BundleId (string) -- The bundle id used for APNs Tokens.
            Certificate (string) -- The distribution certificate from Apple.
            DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            PrivateKey (string) -- The certificate private key.
            TeamId (string) -- The team id used for APNs Tokens.
            TokenKey (string) -- The token key used for APNs Tokens.
            TokenKeyId (string) -- The token key used for APNs Tokens.
            

    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :rtype: dict
    :return: {
        'APNSVoipSandboxChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultAuthenticationMethod': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'HasTokenKey': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    APNSVoipSandboxChannelResponse (dict) -- Apple VoIP Developer Push Notification Service channel definition.
    ApplicationId (string) -- Application id
    CreationDate (string) -- When was this segment created
    DefaultAuthenticationMethod (string) -- The default authentication method used for APNs.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Not used. Retained for backwards compatibility.
    HasTokenKey (boolean) -- If the channel is registered with a token key for authentication.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who made the last change
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be APNS.
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_application_settings(ApplicationId=None, WriteApplicationSettingsRequest=None):
    """
    Used to update the settings for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.update_application_settings(
        ApplicationId='string',
        WriteApplicationSettingsRequest={
            'CampaignHook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'CloudWatchMetricsEnabled': True|False,
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'QuietTime': {
                'End': 'string',
                'Start': 'string'
            }
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type WriteApplicationSettingsRequest: dict
    :param WriteApplicationSettingsRequest: [REQUIRED] Creating application setting request
            CampaignHook (dict) -- Default campaign hook information.
            LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
            Mode (string) -- What mode Lambda should be invoked in.
            WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
            CloudWatchMetricsEnabled (boolean) -- The CloudWatchMetrics settings for the app.
            Limits (dict) -- The limits that apply to each campaign in the project by default. Campaigns can also have their own limits, which override the settings at the project level.
            Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
            MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
            MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
            Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
            QuietTime (dict) -- The default quiet time for the app. Campaigns in the app don't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your app. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up an app to use quiet time, campaigns in that app don't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the app (or campaign, if applicable). - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the app (or campaign, if applicable). Individual campaigns within the app can have their own quiet time settings, which override the quiet time settings at the app level.
            End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
            Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
            

    :rtype: dict
    :return: {
        'ApplicationSettingsResource': {
            'ApplicationId': 'string',
            'CampaignHook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'QuietTime': {
                'End': 'string',
                'Start': 'string'
            }
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    ApplicationSettingsResource (dict) -- Application settings.
    ApplicationId (string) -- The unique ID for the application.
    CampaignHook (dict) -- Default campaign hook.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    LastModifiedDate (string) -- The date that the settings were last updated in ISO 8601 format.
    Limits (dict) -- The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own.
    Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
    
    
    QuietTime (dict) -- The default quiet time for the app. Campaigns in the app don't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your app. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up an app to use quiet time, campaigns in that app don't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the app (or campaign, if applicable). - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the app (or campaign, if applicable). Individual campaigns within the app can have their own quiet time settings, which override the quiet time settings at the app level.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    
    
    
    
    
    """
    pass

def update_baidu_channel(ApplicationId=None, BaiduChannelRequest=None):
    """
    Update a BAIDU GCM channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_baidu_channel(
        ApplicationId='string',
        BaiduChannelRequest={
            'ApiKey': 'string',
            'Enabled': True|False,
            'SecretKey': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type BaiduChannelRequest: dict
    :param BaiduChannelRequest: [REQUIRED] Baidu Cloud Push credentials
            ApiKey (string) -- Platform credential API key from Baidu.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            SecretKey (string) -- Platform credential Secret key from Baidu.
            

    :rtype: dict
    :return: {
        'BaiduChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    BaiduChannelResponse (dict) -- Baidu Cloud Messaging channel definition
    ApplicationId (string) -- Application id
    CreationDate (string) -- When was this segment created
    Credential (string) -- The Baidu API key from Baidu.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Not used. Retained for backwards compatibility.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who made the last change
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be BAIDU
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_campaign(ApplicationId=None, CampaignId=None, WriteCampaignRequest=None):
    """
    Use to update a campaign.
    See also: AWS API Documentation
    
    
    :example: response = client.update_campaign(
        ApplicationId='string',
        CampaignId='string',
        WriteCampaignRequest={
            'AdditionalTreatments': [
                {
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'EventFilter': {
                            'Dimensions': {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'EventType': {
                                    'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                }
                            },
                            'FilterType': 'SYSTEM'|'ENDPOINT'
                        },
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'Description': 'string',
            'HoldoutPercent': 123,
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'IsPaused': True|False,
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'EventFilter': {
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'EventType': {
                            'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                            'Values': [
                                'string',
                            ]
                        },
                        'Metrics': {
                            'string': {
                                'ComparisonOperator': 'string',
                                'Value': 123.0
                            }
                        }
                    },
                    'FilterType': 'SYSTEM'|'ENDPOINT'
                },
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'TreatmentDescription': 'string',
            'TreatmentName': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type CampaignId: string
    :param CampaignId: [REQUIRED] The unique ID of the campaign.

    :type WriteCampaignRequest: dict
    :param WriteCampaignRequest: [REQUIRED] Used to create a campaign.
            AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
            (dict) -- Used to create a campaign treatment.
            MessageConfiguration (dict) -- The message configuration settings.
            ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            EmailMessage (dict) -- The email message configuration.
            Body (string) -- The email text body.
            FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
            HtmlBody (string) -- The email html body.
            Title (string) -- The email title (Or subject).
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The SMS message configuration.
            Body (string) -- The SMS text body.
            MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
            SenderId (string) -- Sender ID of sent message.
            
            Schedule (dict) -- The campaign schedule.
            EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
            EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
            Dimensions (dict) -- An object that defines the dimensions for the event filter.
            Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
            (string) --
            (dict) -- Custom metric dimension
            ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
            Value (float) -- The value to be compared.
            
            
            FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
            Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
            IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
            QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
            End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
            Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
            StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
            Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
            SizePercent (integer) -- The allocated percentage of users for this treatment.
            TreatmentDescription (string) -- A custom description for the treatment.
            TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
            
            Description (string) -- A description of the campaign.
            HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
            Hook (dict) -- Campaign hook information.
            LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
            Mode (string) -- What mode Lambda should be invoked in.
            WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
            IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
            Limits (dict) -- The campaign limits settings.
            Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
            MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
            MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
            Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
            MessageConfiguration (dict) -- The message configuration settings.
            ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            DefaultMessage (dict) -- The default message for all channels.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            EmailMessage (dict) -- The email message configuration.
            Body (string) -- The email text body.
            FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
            HtmlBody (string) -- The email html body.
            Title (string) -- The email title (Or subject).
            GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
            Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
            Body (string) -- The message body. Can include up to 140 characters.
            ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
            ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
            ImageUrl (string) -- The URL that points to an image used in the push notification.
            JsonBody (string) -- The JSON payload used for a silent push.
            MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
            RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
            SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
            TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
            Title (string) -- The message title that displays above the message on the user's device.
            Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
            SMSMessage (dict) -- The SMS message configuration.
            Body (string) -- The SMS text body.
            MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
            SenderId (string) -- Sender ID of sent message.
            
            Name (string) -- The custom name of the campaign.
            Schedule (dict) -- The campaign schedule.
            EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
            EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
            Dimensions (dict) -- An object that defines the dimensions for the event filter.
            Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
            (string) --
            (dict) -- Custom metric dimension
            ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
            Value (float) -- The value to be compared.
            
            
            FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
            Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
            IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
            QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
            End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
            Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
            StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
            Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
            SegmentId (string) -- The ID of the segment to which the campaign sends messages.
            SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
            TreatmentDescription (string) -- A custom description for the treatment.
            TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
            

    :rtype: dict
    :return: {
        'CampaignResponse': {
            'AdditionalTreatments': [
                {
                    'Id': 'string',
                    'MessageConfiguration': {
                        'ADMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'APNSMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'BaiduMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'DefaultMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'EmailMessage': {
                            'Body': 'string',
                            'FromAddress': 'string',
                            'HtmlBody': 'string',
                            'Title': 'string'
                        },
                        'GCMMessage': {
                            'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                            'Body': 'string',
                            'ImageIconUrl': 'string',
                            'ImageSmallIconUrl': 'string',
                            'ImageUrl': 'string',
                            'JsonBody': 'string',
                            'MediaUrl': 'string',
                            'RawContent': 'string',
                            'SilentPush': True|False,
                            'TimeToLive': 123,
                            'Title': 'string',
                            'Url': 'string'
                        },
                        'SMSMessage': {
                            'Body': 'string',
                            'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                            'SenderId': 'string'
                        }
                    },
                    'Schedule': {
                        'EndTime': 'string',
                        'EventFilter': {
                            'Dimensions': {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'EventType': {
                                    'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                }
                            },
                            'FilterType': 'SYSTEM'|'ENDPOINT'
                        },
                        'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                        'IsLocalTime': True|False,
                        'QuietTime': {
                            'End': 'string',
                            'Start': 'string'
                        },
                        'StartTime': 'string',
                        'Timezone': 'string'
                    },
                    'SizePercent': 123,
                    'State': {
                        'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
                    },
                    'TreatmentDescription': 'string',
                    'TreatmentName': 'string'
                },
            ],
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'DefaultState': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
            },
            'Description': 'string',
            'HoldoutPercent': 123,
            'Hook': {
                'LambdaFunctionName': 'string',
                'Mode': 'DELIVERY'|'FILTER',
                'WebUrl': 'string'
            },
            'Id': 'string',
            'IsPaused': True|False,
            'LastModifiedDate': 'string',
            'Limits': {
                'Daily': 123,
                'MaximumDuration': 123,
                'MessagesPerSecond': 123,
                'Total': 123
            },
            'MessageConfiguration': {
                'ADMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'APNSMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'BaiduMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'DefaultMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'EmailMessage': {
                    'Body': 'string',
                    'FromAddress': 'string',
                    'HtmlBody': 'string',
                    'Title': 'string'
                },
                'GCMMessage': {
                    'Action': 'OPEN_APP'|'DEEP_LINK'|'URL',
                    'Body': 'string',
                    'ImageIconUrl': 'string',
                    'ImageSmallIconUrl': 'string',
                    'ImageUrl': 'string',
                    'JsonBody': 'string',
                    'MediaUrl': 'string',
                    'RawContent': 'string',
                    'SilentPush': True|False,
                    'TimeToLive': 123,
                    'Title': 'string',
                    'Url': 'string'
                },
                'SMSMessage': {
                    'Body': 'string',
                    'MessageType': 'TRANSACTIONAL'|'PROMOTIONAL',
                    'SenderId': 'string'
                }
            },
            'Name': 'string',
            'Schedule': {
                'EndTime': 'string',
                'EventFilter': {
                    'Dimensions': {
                        'Attributes': {
                            'string': {
                                'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                'Values': [
                                    'string',
                                ]
                            }
                        },
                        'EventType': {
                            'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                            'Values': [
                                'string',
                            ]
                        },
                        'Metrics': {
                            'string': {
                                'ComparisonOperator': 'string',
                                'Value': 123.0
                            }
                        }
                    },
                    'FilterType': 'SYSTEM'|'ENDPOINT'
                },
                'Frequency': 'ONCE'|'HOURLY'|'DAILY'|'WEEKLY'|'MONTHLY'|'EVENT',
                'IsLocalTime': True|False,
                'QuietTime': {
                    'End': 'string',
                    'Start': 'string'
                },
                'StartTime': 'string',
                'Timezone': 'string'
            },
            'SegmentId': 'string',
            'SegmentVersion': 123,
            'State': {
                'CampaignStatus': 'SCHEDULED'|'EXECUTING'|'PENDING_NEXT_RUN'|'COMPLETED'|'PAUSED'|'DELETED'
            },
            'TreatmentDescription': 'string',
            'TreatmentName': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    CampaignResponse (dict) -- Campaign definition
    AdditionalTreatments (list) -- Treatments that are defined in addition to the default treatment.
    (dict) -- Treatment resource
    Id (string) -- The unique treatment ID.
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SizePercent (integer) -- The allocated percentage of users for this treatment.
    State (dict) -- The treatment status.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    
    
    
    
    ApplicationId (string) -- The ID of the application to which the campaign applies.
    CreationDate (string) -- The date the campaign was created in ISO 8601 format.
    DefaultState (dict) -- The status of the campaign's default treatment. Only present for A/B test campaigns.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    Description (string) -- A description of the campaign.
    HoldoutPercent (integer) -- The allocated percentage of end users who will not receive messages from this campaign.
    Hook (dict) -- Campaign hook information.
    LambdaFunctionName (string) -- Lambda function name or arn to be called for delivery
    Mode (string) -- What mode Lambda should be invoked in.
    WebUrl (string) -- Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request
    
    
    Id (string) -- The unique campaign ID.
    IsPaused (boolean) -- Indicates whether the campaign is paused. A paused campaign does not send messages unless you resume it by setting IsPaused to false.
    LastModifiedDate (string) -- The date the campaign was last updated in ISO 8601 format.
    Limits (dict) -- The campaign limits settings.
    Daily (integer) -- The maximum number of messages that each campaign can send to a single endpoint in a 24-hour period.
    MaximumDuration (integer) -- The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
    MessagesPerSecond (integer) -- The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
    Total (integer) -- The maximum number of messages that an individual campaign can send to a single endpoint over the course of the campaign.
    
    
    MessageConfiguration (dict) -- The message configuration settings.
    ADMMessage (dict) -- The message that the campaign delivers to ADM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    APNSMessage (dict) -- The message that the campaign delivers to APNS channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    BaiduMessage (dict) -- The message that the campaign delivers to Baidu channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    DefaultMessage (dict) -- The default message for all channels.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    EmailMessage (dict) -- The email message configuration.
    Body (string) -- The email text body.
    FromAddress (string) -- The email address used to send the email from. Defaults to use FromAddress specified in the Email Channel.
    HtmlBody (string) -- The email html body.
    Title (string) -- The email title (Or subject).
    
    
    GCMMessage (dict) -- The message that the campaign delivers to GCM channels. Overrides the default message.
    Action (string) -- The action that occurs if the user taps a push notification delivered by the campaign: OPEN_APP - Your app launches, or it becomes the foreground app if it has been sent to the background. This is the default action. DEEP_LINK - Uses deep linking features in iOS and Android to open your app and display a designated user interface within the app. URL - The default mobile browser on the user's device launches and opens a web page at the URL you specify.
    Body (string) -- The message body. Can include up to 140 characters.
    ImageIconUrl (string) -- The URL that points to the icon image for the push notification icon, for example, the app icon.
    ImageSmallIconUrl (string) -- The URL that points to the small icon image for the push notification icon, for example, the app icon.
    ImageUrl (string) -- The URL that points to an image used in the push notification.
    JsonBody (string) -- The JSON payload used for a silent push.
    MediaUrl (string) -- A URL that refers to the location of an image or video that you want to display in the push notification.
    RawContent (string) -- The Raw JSON formatted string to be used as the payload. This value overrides the message.
    SilentPush (boolean) -- Indicates if the message should display on the users device. Silent pushes can be used for Remote Configuration and Phone Home use cases.
    TimeToLive (integer) -- This parameter specifies how long (in seconds) the message should be kept if the service is unable to deliver the notification the first time. If the value is 0, it treats the notification as if it expires immediately and does not store the notification or attempt to redeliver it. This value is converted to the expiration field when sent to the service. It only applies to APNs and GCM
    Title (string) -- The message title that displays above the message on the user's device.
    Url (string) -- The URL to open in the user's mobile browser. Used if the value for Action is URL.
    
    
    SMSMessage (dict) -- The SMS message configuration.
    Body (string) -- The SMS text body.
    MessageType (string) -- Is this is a transactional SMS message, otherwise a promotional message.
    SenderId (string) -- Sender ID of sent message.
    
    
    
    
    Name (string) -- The custom name of the campaign.
    Schedule (dict) -- The campaign schedule.
    EndTime (string) -- The scheduled time that the campaign ends in ISO 8601 format.
    EventFilter (dict) -- Defines the type of events that can trigger the campaign. Used when the Frequency is set to EVENT.
    Dimensions (dict) -- An object that defines the dimensions for the event filter.
    Attributes (dict) -- Custom attributes that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    EventType (dict) -- The name of the event that causes the campaign to be sent. This can be a standard event type that Amazon Pinpoint generates, such as _session.start, or a custom event that's specific to your app.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint. You can use these attributes as selection criteria when you create an event filter.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    
    
    FilterType (string) -- The type of event that causes the campaign to be sent. Possible values: SYSTEM - Send the campaign when a system event occurs. See the System resource for more information. ENDPOINT - Send the campaign when an endpoint event occurs. See the Event resource for more information.
    
    
    Frequency (string) -- How often the campaign delivers messages. Valid values: ONCE HOURLY DAILY WEEKLY MONTHLY EVENT
    IsLocalTime (boolean) -- Indicates whether the campaign schedule takes effect according to each user's local time.
    QuietTime (dict) -- The default quiet time for the campaign. The campaign doesn't send messages to endpoints during the quiet time. Note: Make sure that your endpoints include the Demographics.Timezone attribute if you plan to enable a quiet time for your campaign. If your endpoints don't include this attribute, they'll receive the messages that you send them, even if quiet time is enabled. When you set up a campaign to use quiet time, the campaign doesn't send messages during the time range you specified, as long as all of the following are true: - The endpoint includes a valid Demographic.Timezone attribute. - The current time in the endpoint's time zone is later than or equal to the time specified in the QuietTime.Start attribute for the campaign. - The current time in the endpoint's time zone is earlier than or equal to the time specified in the QuietTime.End attribute for the campaign.
    End (string) -- The time at which quiet time should end. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    Start (string) -- The time at which quiet time should begin. The value that you specify has to be in HH:mm format, where HH is the hour in 24-hour format (with a leading zero, if applicable), and mm is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.
    
    
    StartTime (string) -- The scheduled time that the campaign begins in ISO 8601 format.
    Timezone (string) -- The starting UTC offset for the schedule if the value for isLocalTime is true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30 UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30 UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06 UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    
    
    SegmentId (string) -- The ID of the segment to which the campaign sends messages.
    SegmentVersion (integer) -- The version of the segment to which the campaign sends messages.
    State (dict) -- The campaign status. An A/B test campaign will have a status of COMPLETED only when all treatments have a status of COMPLETED.
    CampaignStatus (string) -- The status of the campaign, or the status of a treatment that belongs to an A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN, COMPLETED, PAUSED
    
    
    TreatmentDescription (string) -- A custom description for the treatment.
    TreatmentName (string) -- The custom name of a variation of the campaign used for A/B testing.
    Version (integer) -- The campaign version number.
    
    
    
    
    
    """
    pass

def update_email_channel(ApplicationId=None, EmailChannelRequest=None):
    """
    Update an email channel.
    See also: AWS API Documentation
    
    
    :example: response = client.update_email_channel(
        ApplicationId='string',
        EmailChannelRequest={
            'ConfigurationSet': 'string',
            'Enabled': True|False,
            'FromAddress': 'string',
            'Identity': 'string',
            'RoleArn': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type EmailChannelRequest: dict
    :param EmailChannelRequest: [REQUIRED] Email Channel Request
            ConfigurationSet (string) -- The configuration set that you want to use when you send email using the Pinpoint Email API.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            FromAddress (string) -- The email address used to send emails from.
            Identity (string) -- The ARN of an identity verified with SES.
            RoleArn (string) -- The ARN of an IAM Role used to submit events to Mobile Analytics' event ingestion service
            

    :rtype: dict
    :return: {
        'EmailChannelResponse': {
            'ApplicationId': 'string',
            'ConfigurationSet': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'FromAddress': 'string',
            'HasCredential': True|False,
            'Id': 'string',
            'Identity': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'MessagesPerSecond': 123,
            'Platform': 'string',
            'RoleArn': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    EmailChannelResponse (dict) -- Email Channel Response.
    ApplicationId (string) -- The unique ID of the application to which the email channel belongs.
    ConfigurationSet (string) -- The configuration set that you want to use when you send email using the Pinpoint Email API.
    CreationDate (string) -- The date that the settings were last updated in ISO 8601 format.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    FromAddress (string) -- The email address used to send emails from.
    HasCredential (boolean) -- Not used. Retained for backwards compatibility.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    Identity (string) -- The ARN of an identity verified with SES.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    MessagesPerSecond (integer) -- Messages per second that can be sent
    Platform (string) -- Platform type. Will be "EMAIL"
    RoleArn (string) -- The ARN of an IAM Role used to submit events to Mobile Analytics' event ingestion service
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_endpoint(ApplicationId=None, EndpointId=None, EndpointRequest=None):
    """
    Creates or updates an endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.update_endpoint(
        ApplicationId='string',
        EndpointId='string',
        EndpointRequest={
            'Address': 'string',
            'Attributes': {
                'string': [
                    'string',
                ]
            },
            'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'VOICE'|'EMAIL'|'BAIDU'|'CUSTOM',
            'Demographic': {
                'AppVersion': 'string',
                'Locale': 'string',
                'Make': 'string',
                'Model': 'string',
                'ModelVersion': 'string',
                'Platform': 'string',
                'PlatformVersion': 'string',
                'Timezone': 'string'
            },
            'EffectiveDate': 'string',
            'EndpointStatus': 'string',
            'Location': {
                'City': 'string',
                'Country': 'string',
                'Latitude': 123.0,
                'Longitude': 123.0,
                'PostalCode': 'string',
                'Region': 'string'
            },
            'Metrics': {
                'string': 123.0
            },
            'OptOut': 'string',
            'RequestId': 'string',
            'User': {
                'UserAttributes': {
                    'string': [
                        'string',
                    ]
                },
                'UserId': 'string'
            }
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type EndpointId: string
    :param EndpointId: [REQUIRED] The unique ID of the endpoint.

    :type EndpointRequest: dict
    :param EndpointRequest: [REQUIRED] An endpoint update request.
            Address (string) -- The destination for messages that you send to this endpoint. The address varies by channel. For mobile push channels, use the token provided by the push notification service, such as the APNs device token or the FCM registration token. For the SMS channel, use a phone number in E.164 format, such as +12065550100. For the email channel, use an email address.
            Attributes (dict) -- Custom attributes that describe the endpoint by associating a name with an array of values. For example, an attribute named 'interests' might have the values ['science', 'politics', 'travel']. You can use these attributes as selection criteria when you create a segment of users to engage with a messaging campaign. The following characters are not recommended in attribute names: # : ? /. The Amazon Pinpoint console does not display attributes that include these characters in the name. This limitation does not apply to attribute values.
            (string) --
            (list) --
            (string) --
            
            ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
            Demographic (dict) -- Demographic attributes for the endpoint.
            AppVersion (string) -- The version of the application associated with the endpoint.
            Locale (string) -- The endpoint locale in the following format: The ISO 639-1 alpha-2 code, followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
            Make (string) -- The manufacturer of the endpoint device, such as Apple or Samsung.
            Model (string) -- The model name or number of the endpoint device, such as iPhone.
            ModelVersion (string) -- The model version of the endpoint device.
            Platform (string) -- The platform of the endpoint device, such as iOS or Android.
            PlatformVersion (string) -- The platform version of the endpoint device.
            Timezone (string) -- The timezone of the endpoint. Specified as a tz database value, such as Americas/Los_Angeles.
            EffectiveDate (string) -- The date and time when the endpoint was updated, shown in ISO 8601 format.
            EndpointStatus (string) -- Unused.
            Location (dict) -- The endpoint location attributes.
            City (string) -- The city where the endpoint is located.
            Country (string) -- The two-letter code for the country or region of the endpoint. Specified as an ISO 3166-1 alpha-2 code, such as 'US' for the United States.
            Latitude (float) -- The latitude of the endpoint location, rounded to one decimal place.
            Longitude (float) -- The longitude of the endpoint location, rounded to one decimal place.
            PostalCode (string) -- The postal code or zip code of the endpoint.
            Region (string) -- The region of the endpoint location. For example, in the United States, this corresponds to a state.
            Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint.
            (string) --
            (float) --
            
            OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
            RequestId (string) -- The unique ID for the most recent request to update the endpoint.
            User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
            UserAttributes (dict) -- Custom attributes that describe the user by associating a name with an array of values. For example, an attribute named 'interests' might have the following values: ['science', 'politics', 'travel']. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
            (string) --
            (list) --
            (string) --
            
            UserId (string) -- The unique ID of the user.
            

    :rtype: dict
    :return: {
        'MessageBody': {
            'Message': 'string',
            'RequestID': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 202 response
    MessageBody (dict) -- Simple message object.
    Message (string) -- The error message that's returned from the API.
    RequestID (string) -- The unique message body ID.
    
    
    
    
    
    """
    pass

def update_endpoints_batch(ApplicationId=None, EndpointBatchRequest=None):
    """
    Use to update a batch of endpoints.
    See also: AWS API Documentation
    
    
    :example: response = client.update_endpoints_batch(
        ApplicationId='string',
        EndpointBatchRequest={
            'Item': [
                {
                    'Address': 'string',
                    'Attributes': {
                        'string': [
                            'string',
                        ]
                    },
                    'ChannelType': 'GCM'|'APNS'|'APNS_SANDBOX'|'APNS_VOIP'|'APNS_VOIP_SANDBOX'|'ADM'|'SMS'|'VOICE'|'EMAIL'|'BAIDU'|'CUSTOM',
                    'Demographic': {
                        'AppVersion': 'string',
                        'Locale': 'string',
                        'Make': 'string',
                        'Model': 'string',
                        'ModelVersion': 'string',
                        'Platform': 'string',
                        'PlatformVersion': 'string',
                        'Timezone': 'string'
                    },
                    'EffectiveDate': 'string',
                    'EndpointStatus': 'string',
                    'Id': 'string',
                    'Location': {
                        'City': 'string',
                        'Country': 'string',
                        'Latitude': 123.0,
                        'Longitude': 123.0,
                        'PostalCode': 'string',
                        'Region': 'string'
                    },
                    'Metrics': {
                        'string': 123.0
                    },
                    'OptOut': 'string',
                    'RequestId': 'string',
                    'User': {
                        'UserAttributes': {
                            'string': [
                                'string',
                            ]
                        },
                        'UserId': 'string'
                    }
                },
            ]
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type EndpointBatchRequest: dict
    :param EndpointBatchRequest: [REQUIRED] Endpoint batch update request.
            Item (list) -- List of items to update. Maximum 100 items
            (dict) -- Endpoint update request
            Address (string) -- The destination for messages that you send to this endpoint. The address varies by channel. For mobile push channels, use the token provided by the push notification service, such as the APNs device token or the FCM registration token. For the SMS channel, use a phone number in E.164 format, such as +12065550100. For the email channel, use an email address.
            Attributes (dict) -- Custom attributes that describe the endpoint by associating a name with an array of values. For example, an attribute named 'interests' might have the values ['science', 'politics', 'travel']. You can use these attributes as selection criteria when you create a segment of users to engage with a messaging campaign. The following characters are not recommended in attribute names: # : ? /. The Amazon Pinpoint console does not display attributes that include these characters in the name. This limitation does not apply to attribute values.
            (string) --
            (list) --
            (string) --
            
            ChannelType (string) -- The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP | APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
            Demographic (dict) -- The endpoint demographic attributes.
            AppVersion (string) -- The version of the application associated with the endpoint.
            Locale (string) -- The endpoint locale in the following format: The ISO 639-1 alpha-2 code, followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
            Make (string) -- The manufacturer of the endpoint device, such as Apple or Samsung.
            Model (string) -- The model name or number of the endpoint device, such as iPhone.
            ModelVersion (string) -- The model version of the endpoint device.
            Platform (string) -- The platform of the endpoint device, such as iOS or Android.
            PlatformVersion (string) -- The platform version of the endpoint device.
            Timezone (string) -- The timezone of the endpoint. Specified as a tz database value, such as Americas/Los_Angeles.
            EffectiveDate (string) -- The last time the endpoint was updated. Provided in ISO 8601 format.
            EndpointStatus (string) -- Unused.
            Id (string) -- The unique Id for the Endpoint in the batch.
            Location (dict) -- The endpoint location attributes.
            City (string) -- The city where the endpoint is located.
            Country (string) -- The two-letter code for the country or region of the endpoint. Specified as an ISO 3166-1 alpha-2 code, such as 'US' for the United States.
            Latitude (float) -- The latitude of the endpoint location, rounded to one decimal place.
            Longitude (float) -- The longitude of the endpoint location, rounded to one decimal place.
            PostalCode (string) -- The postal code or zip code of the endpoint.
            Region (string) -- The region of the endpoint location. For example, in the United States, this corresponds to a state.
            Metrics (dict) -- Custom metrics that your app reports to Amazon Pinpoint.
            (string) --
            (float) --
            
            OptOut (string) -- Indicates whether a user has opted out of receiving messages with one of the following values: ALL - User has opted out of all messages. NONE - Users has not opted out and receives all messages.
            RequestId (string) -- The unique ID for the most recent request to update the endpoint.
            User (dict) -- Custom user-specific attributes that your app reports to Amazon Pinpoint.
            UserAttributes (dict) -- Custom attributes that describe the user by associating a name with an array of values. For example, an attribute named 'interests' might have the following values: ['science', 'politics', 'travel']. You can use these attributes as selection criteria when you create segments. The Amazon Pinpoint console can't display attribute names that include the following characters: hash/pound sign (#), colon (:), question mark (?), backslash (), and forward slash (/). For this reason, you should avoid using these characters in the names of custom attributes.
            (string) --
            (list) --
            (string) --
            
            UserId (string) -- The unique ID of the user.
            
            

    :rtype: dict
    :return: {
        'MessageBody': {
            'Message': 'string',
            'RequestID': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- 202 response
    MessageBody (dict) -- Simple message object.
    Message (string) -- The error message that's returned from the API.
    RequestID (string) -- The unique message body ID.
    
    
    
    
    
    """
    pass

def update_gcm_channel(ApplicationId=None, GCMChannelRequest=None):
    """
    Use to update the GCM channel for an app.
    See also: AWS API Documentation
    
    
    :example: response = client.update_gcm_channel(
        ApplicationId='string',
        GCMChannelRequest={
            'ApiKey': 'string',
            'Enabled': True|False
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type GCMChannelRequest: dict
    :param GCMChannelRequest: [REQUIRED] Google Cloud Messaging credentials
            ApiKey (string) -- Platform credential API key from Google.
            Enabled (boolean) -- If the channel is enabled for sending messages.
            

    :rtype: dict
    :return: {
        'GCMChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Credential': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    GCMChannelResponse (dict) -- Google Cloud Messaging channel definition
    ApplicationId (string) -- The ID of the application to which the channel applies.
    CreationDate (string) -- When was this segment created
    Credential (string) -- The GCM API key from Google.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Not used. Retained for backwards compatibility.
    Id (string) -- Channel ID. Not used. Present only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- The platform type. Will be GCM
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_segment(ApplicationId=None, SegmentId=None, WriteSegmentRequest=None):
    """
    Used to update a segment.
    See also: AWS API Documentation
    
    
    :example: response = client.update_segment(
        ApplicationId='string',
        SegmentId='string',
        WriteSegmentRequest={
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Channel': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'GPSPoint': {
                        'Coordinates': {
                            'Latitude': 123.0,
                            'Longitude': 123.0
                        },
                        'RangeInKilometers': 123.0
                    }
                },
                'Metrics': {
                    'string': {
                        'ComparisonOperator': 'string',
                        'Value': 123.0
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Name': 'string',
            'SegmentGroups': {
                'Groups': [
                    {
                        'Dimensions': [
                            {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Behavior': {
                                    'Recency': {
                                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                        'RecencyType': 'ACTIVE'|'INACTIVE'
                                    }
                                },
                                'Demographic': {
                                    'AppVersion': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Channel': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'DeviceType': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Make': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Model': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Platform': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Location': {
                                    'Country': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'GPSPoint': {
                                        'Coordinates': {
                                            'Latitude': 123.0,
                                            'Longitude': 123.0
                                        },
                                        'RangeInKilometers': 123.0
                                    }
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                },
                                'UserAttributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                }
                            },
                        ],
                        'SourceSegments': [
                            {
                                'Id': 'string',
                                'Version': 123
                            },
                        ],
                        'SourceType': 'ALL'|'ANY'|'NONE',
                        'Type': 'ALL'|'ANY'|'NONE'
                    },
                ],
                'Include': 'ALL'|'ANY'|'NONE'
            }
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type SegmentId: string
    :param SegmentId: [REQUIRED] The unique ID of the segment.

    :type WriteSegmentRequest: dict
    :param WriteSegmentRequest: [REQUIRED] Segment definition.
            Dimensions (dict) -- The segment dimensions attributes.
            Attributes (dict) -- Custom segment attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Behavior (dict) -- The segment behaviors attributes.
            Recency (dict) -- The recency of use.
            Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
            RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
            
            Demographic (dict) -- The segment demographics attributes.
            AppVersion (dict) -- The app version criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Channel (dict) -- The channel criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            DeviceType (dict) -- The device type criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Make (dict) -- The device make criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Model (dict) -- The device model criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Platform (dict) -- The device platform criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Location (dict) -- The segment location attributes.
            Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            GPSPoint (dict) -- The GPS Point dimension.
            Coordinates (dict) -- Coordinate to measure distance from.
            Latitude (float) -- Latitude
            Longitude (float) -- Longitude
            RangeInKilometers (float) -- Range in kilometers from the coordinate.
            
            Metrics (dict) -- Custom segment metrics.
            (string) --
            (dict) -- Custom metric dimension
            ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
            Value (float) -- The value to be compared.
            
            UserAttributes (dict) -- Custom segment user attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Name (string) -- The name of segment
            SegmentGroups (dict) -- A segment group, which consists of zero or more source segments, plus dimensions that are applied to those source segments. Your request can only include one segment group. Your request can include either a SegmentGroups object or a Dimensions object, but not both.
            Groups (list) -- A set of segment criteria to evaluate.
            (dict) -- Segment group definition.
            Dimensions (list) -- List of dimensions to include or exclude.
            (dict) -- Segment dimensions
            Attributes (dict) -- Custom segment attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            Behavior (dict) -- The segment behaviors attributes.
            Recency (dict) -- The recency of use.
            Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
            RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
            
            Demographic (dict) -- The segment demographics attributes.
            AppVersion (dict) -- The app version criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Channel (dict) -- The channel criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            DeviceType (dict) -- The device type criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Make (dict) -- The device make criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Model (dict) -- The device model criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Platform (dict) -- The device platform criteria for the segment.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            Location (dict) -- The segment location attributes.
            Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
            DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            GPSPoint (dict) -- The GPS Point dimension.
            Coordinates (dict) -- Coordinate to measure distance from.
            Latitude (float) -- Latitude
            Longitude (float) -- Longitude
            RangeInKilometers (float) -- Range in kilometers from the coordinate.
            
            Metrics (dict) -- Custom segment metrics.
            (string) --
            (dict) -- Custom metric dimension
            ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
            Value (float) -- The value to be compared.
            
            UserAttributes (dict) -- Custom segment user attributes.
            (string) --
            (dict) -- Custom attibute dimension
            AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
            Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
            (string) --
            
            
            
            SourceSegments (list) -- The base segment that you build your segment on. The source segment defines the starting 'universe' of endpoints. When you add dimensions to the segment, it filters the source segment based on the dimensions that you specify. You can specify more than one dimensional segment. You can only specify one imported segment. NOTE: If you specify an imported segment for this attribute, the segment size estimate that appears in the Amazon Pinpoint console shows the size of the imported segment, without any filters applied to it.
            (dict) -- Segment reference.
            Id (string) -- A unique identifier for the segment.
            Version (integer) -- If specified contains a specific version of the segment included.
            
            SourceType (string) -- Specify how to handle multiple source segments. For example, if you specify three source segments, should the resulting segment be based on any or all of the segments? Acceptable values: ANY or ALL.
            Type (string) -- Specify how to handle multiple segment dimensions. For example, if you specify three dimensions, should the resulting segment include endpoints that are matched by all, any, or none of the dimensions? Acceptable values: ALL, ANY, or NONE.
            
            Include (string) -- Specify how to handle multiple segment groups. For example, if the segment includes three segment groups, should the resulting segment include endpoints that are matched by all, any, or none of the segment groups you created. Acceptable values: ALL, ANY, or NONE.
            

    :rtype: dict
    :return: {
        'SegmentResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Dimensions': {
                'Attributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Behavior': {
                    'Recency': {
                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                        'RecencyType': 'ACTIVE'|'INACTIVE'
                    }
                },
                'Demographic': {
                    'AppVersion': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Channel': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'DeviceType': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Make': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Model': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'Platform': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Location': {
                    'Country': {
                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    },
                    'GPSPoint': {
                        'Coordinates': {
                            'Latitude': 123.0,
                            'Longitude': 123.0
                        },
                        'RangeInKilometers': 123.0
                    }
                },
                'Metrics': {
                    'string': {
                        'ComparisonOperator': 'string',
                        'Value': 123.0
                    }
                },
                'UserAttributes': {
                    'string': {
                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'Id': 'string',
            'ImportDefinition': {
                'ChannelCounts': {
                    'string': 123
                },
                'ExternalId': 'string',
                'Format': 'CSV'|'JSON',
                'RoleArn': 'string',
                'S3Url': 'string',
                'Size': 123
            },
            'LastModifiedDate': 'string',
            'Name': 'string',
            'SegmentGroups': {
                'Groups': [
                    {
                        'Dimensions': [
                            {
                                'Attributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Behavior': {
                                    'Recency': {
                                        'Duration': 'HR_24'|'DAY_7'|'DAY_14'|'DAY_30',
                                        'RecencyType': 'ACTIVE'|'INACTIVE'
                                    }
                                },
                                'Demographic': {
                                    'AppVersion': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Channel': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'DeviceType': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Make': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Model': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'Platform': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                },
                                'Location': {
                                    'Country': {
                                        'DimensionType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    },
                                    'GPSPoint': {
                                        'Coordinates': {
                                            'Latitude': 123.0,
                                            'Longitude': 123.0
                                        },
                                        'RangeInKilometers': 123.0
                                    }
                                },
                                'Metrics': {
                                    'string': {
                                        'ComparisonOperator': 'string',
                                        'Value': 123.0
                                    }
                                },
                                'UserAttributes': {
                                    'string': {
                                        'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
                                        'Values': [
                                            'string',
                                        ]
                                    }
                                }
                            },
                        ],
                        'SourceSegments': [
                            {
                                'Id': 'string',
                                'Version': 123
                            },
                        ],
                        'SourceType': 'ALL'|'ANY'|'NONE',
                        'Type': 'ALL'|'ANY'|'NONE'
                    },
                ],
                'Include': 'ALL'|'ANY'|'NONE'
            },
            'SegmentType': 'DIMENSIONAL'|'IMPORT',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SegmentResponse (dict) -- Segment definition.
    ApplicationId (string) -- The ID of the application that the segment applies to.
    CreationDate (string) -- The date and time when the segment was created.
    Dimensions (dict) -- The segment dimensions attributes.
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    Id (string) -- The unique segment ID.
    ImportDefinition (dict) -- The import job settings.
    ChannelCounts (dict) -- The number of channel types in the imported segment.
    (string) --
    (integer) --
    
    
    
    
    ExternalId (string) -- (Deprecated) Your AWS account ID, which you assigned to the ExternalID key in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This requirement is removed, and external IDs are not recommended for IAM roles assumed by Amazon Pinpoint.
    Format (string) -- The format of the endpoint files that were imported to create this segment. Valid values: CSV, JSON
    RoleArn (string) -- The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint access to the endpoints in Amazon S3.
    S3Url (string) -- The URL of the S3 bucket that the segment was imported from.
    Size (integer) -- The number of endpoints that were successfully imported to create this segment.
    
    
    LastModifiedDate (string) -- The date and time when the segment was last modified.
    Name (string) -- The name of the segment.
    SegmentGroups (dict) -- A segment group, which consists of zero or more source segments, plus dimensions that are applied to those source segments.
    Groups (list) -- A set of segment criteria to evaluate.
    (dict) -- Segment group definition.
    Dimensions (list) -- List of dimensions to include or exclude.
    (dict) -- Segment dimensions
    Attributes (dict) -- Custom segment attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    Behavior (dict) -- The segment behaviors attributes.
    Recency (dict) -- The recency of use.
    Duration (string) -- The length of time during which users have been active or inactive with your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    RecencyType (string) -- The recency dimension type: ACTIVE - Users who have used your app within the specified duration are included in the segment. INACTIVE - Users who have not used your app within the specified duration are included in the segment.
    
    
    
    
    Demographic (dict) -- The segment demographics attributes.
    AppVersion (dict) -- The app version criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Channel (dict) -- The channel criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    DeviceType (dict) -- The device type criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Make (dict) -- The device make criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Model (dict) -- The device model criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    Platform (dict) -- The device platform criteria for the segment.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    Location (dict) -- The segment location attributes.
    Country (dict) -- The country or region, in ISO 3166-1 alpha-2 format.
    DimensionType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    GPSPoint (dict) -- The GPS Point dimension.
    Coordinates (dict) -- Coordinate to measure distance from.
    Latitude (float) -- Latitude
    Longitude (float) -- Longitude
    
    
    RangeInKilometers (float) -- Range in kilometers from the coordinate.
    
    
    
    
    Metrics (dict) -- Custom segment metrics.
    (string) --
    (dict) -- Custom metric dimension
    ComparisonOperator (string) -- The operator that you're using to compare metric values. Possible values: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, or EQUAL
    Value (float) -- The value to be compared.
    
    
    
    
    
    
    UserAttributes (dict) -- Custom segment user attributes.
    (string) --
    (dict) -- Custom attibute dimension
    AttributeType (string) -- The type of dimension: INCLUSIVE - Endpoints that match the criteria are included in the segment. EXCLUSIVE - Endpoints that match the criteria are excluded from the segment.
    Values (list) -- The criteria values for the segment dimension. Endpoints with matching attribute values are included or excluded from the segment, depending on the setting for Type.
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    
    SourceSegments (list) -- The base segment that you build your segment on. The source segment defines the starting "universe" of endpoints. When you add dimensions to the segment, it filters the source segment based on the dimensions that you specify. You can specify more than one dimensional segment. You can only specify one imported segment. NOTE: If you specify an imported segment for this attribute, the segment size estimate that appears in the Amazon Pinpoint console shows the size of the imported segment, without any filters applied to it.
    (dict) -- Segment reference.
    Id (string) -- A unique identifier for the segment.
    Version (integer) -- If specified contains a specific version of the segment included.
    
    
    
    
    SourceType (string) -- Specify how to handle multiple source segments. For example, if you specify three source segments, should the resulting segment be based on any or all of the segments? Acceptable values: ANY or ALL.
    Type (string) -- Specify how to handle multiple segment dimensions. For example, if you specify three dimensions, should the resulting segment include endpoints that are matched by all, any, or none of the dimensions? Acceptable values: ALL, ANY, or NONE.
    
    
    
    
    Include (string) -- Specify how to handle multiple segment groups. For example, if the segment includes three segment groups, should the resulting segment include endpoints that are matched by all, any, or none of the segment groups you created. Acceptable values: ALL, ANY, or NONE.
    
    
    SegmentType (string) -- The segment type: DIMENSIONAL - A dynamic segment built from selection criteria based on endpoint data reported by your app. You create this type of segment by using the segment builder in the Amazon Pinpoint console or by making a POST request to the segments resource. IMPORT - A static segment built from an imported set of endpoint definitions. You create this type of segment by importing a segment in the Amazon Pinpoint console or by making a POST request to the jobs/import resource.
    Version (integer) -- The segment version number.
    
    
    
    
    
    """
    pass

def update_sms_channel(ApplicationId=None, SMSChannelRequest=None):
    """
    Update an SMS channel.
    See also: AWS API Documentation
    
    
    :example: response = client.update_sms_channel(
        ApplicationId='string',
        SMSChannelRequest={
            'Enabled': True|False,
            'SenderId': 'string',
            'ShortCode': 'string'
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type SMSChannelRequest: dict
    :param SMSChannelRequest: [REQUIRED] SMS Channel Request
            Enabled (boolean) -- If the channel is enabled for sending messages.
            SenderId (string) -- Sender identifier of your messages.
            ShortCode (string) -- ShortCode registered with phone provider.
            

    :rtype: dict
    :return: {
        'SMSChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'PromotionalMessagesPerSecond': 123,
            'SenderId': 'string',
            'ShortCode': 'string',
            'TransactionalMessagesPerSecond': 123,
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    SMSChannelResponse (dict) -- SMS Channel Response.
    ApplicationId (string) -- The unique ID of the application to which the SMS channel belongs.
    CreationDate (string) -- The date that the settings were last updated in ISO 8601 format.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) -- Not used. Retained for backwards compatibility.
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who last updated this entry
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- Platform type. Will be "SMS"
    PromotionalMessagesPerSecond (integer) -- Promotional messages per second that can be sent
    SenderId (string) -- Sender identifier of your messages.
    ShortCode (string) -- The short code registered with the phone provider.
    TransactionalMessagesPerSecond (integer) -- Transactional messages per second that can be sent
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

def update_voice_channel(ApplicationId=None, VoiceChannelRequest=None):
    """
    Update an Voice channel
    See also: AWS API Documentation
    
    
    :example: response = client.update_voice_channel(
        ApplicationId='string',
        VoiceChannelRequest={
            'Enabled': True|False
        }
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED] The unique ID of your Amazon Pinpoint application.

    :type VoiceChannelRequest: dict
    :param VoiceChannelRequest: [REQUIRED] Voice Channel Request
            Enabled (boolean) -- If the channel is enabled for sending messages.
            

    :rtype: dict
    :return: {
        'VoiceChannelResponse': {
            'ApplicationId': 'string',
            'CreationDate': 'string',
            'Enabled': True|False,
            'HasCredential': True|False,
            'Id': 'string',
            'IsArchived': True|False,
            'LastModifiedBy': 'string',
            'LastModifiedDate': 'string',
            'Platform': 'string',
            'Version': 123
        }
    }
    
    
    :returns: 
    (dict) -- 200 response
    VoiceChannelResponse (dict) -- Voice Channel Response.
    ApplicationId (string) -- Application id
    CreationDate (string) -- The date that the settings were last updated in ISO 8601 format.
    Enabled (boolean) -- If the channel is enabled for sending messages.
    HasCredential (boolean) --
    Id (string) -- Channel ID. Not used, only for backwards compatibility.
    IsArchived (boolean) -- Is this channel archived
    LastModifiedBy (string) -- Who made the last change
    LastModifiedDate (string) -- Last date this was updated
    Platform (string) -- Platform type. Will be "Voice"
    Version (integer) -- Version of channel
    
    
    
    
    
    """
    pass

