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

def create_configuration_set(ConfigurationSetName=None, TrackingOptions=None, DeliveryOptions=None, ReputationOptions=None, SendingOptions=None):
    """
    Create a configuration set. Configuration sets are groups of rules that you can apply to the emails you send using Amazon Pinpoint. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
    See also: AWS API Documentation
    
    
    :example: response = client.create_configuration_set(
        ConfigurationSetName='string',
        TrackingOptions={
            'CustomRedirectDomain': 'string'
        },
        DeliveryOptions={
            'SendingPoolName': 'string'
        },
        ReputationOptions={
            'ReputationMetricsEnabled': True|False,
            'LastFreshStart': datetime(2015, 1, 1)
        },
        SendingOptions={
            'SendingEnabled': True|False
        }
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: The name of the configuration set.

    :type TrackingOptions: dict
    :param TrackingOptions: An object that defines the open and click tracking options for emails that you send using the configuration set.
            CustomRedirectDomain (string) -- [REQUIRED]The domain that you want to use for tracking open and click events.
            

    :type DeliveryOptions: dict
    :param DeliveryOptions: An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.
            SendingPoolName (string) --The name of the dedicated IP pool that you want to associate with the configuration set.
            

    :type ReputationOptions: dict
    :param ReputationOptions: An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.
            ReputationMetricsEnabled (boolean) --If true , tracking of reputation metrics is enabled for the configuration set. If false , tracking of reputation metrics is disabled for the configuration set.
            LastFreshStart (datetime) --The date and time (in Unix time) when the reputation metrics were last given a fresh start. When your account is given a fresh start, your reputation metrics are calculated starting from the date of the fresh start.
            

    :type SendingOptions: dict
    :param SendingOptions: An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.
            SendingEnabled (boolean) --If true , email sending is enabled for the configuration set. If false , email sending is disabled for the configuration set.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_configuration_set_event_destination(ConfigurationSetName=None, EventDestinationName=None, EventDestination=None):
    """
    Create an event destination. In Amazon Pinpoint, events include message sends, deliveries, opens, clicks, bounces, and complaints. Event destinations are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
    A single configuration set can include more than one event destination.
    See also: AWS API Documentation
    
    
    :example: response = client.create_configuration_set_event_destination(
        ConfigurationSetName='string',
        EventDestinationName='string',
        EventDestination={
            'Enabled': True|False,
            'MatchingEventTypes': [
                'SEND'|'REJECT'|'BOUNCE'|'COMPLAINT'|'DELIVERY'|'OPEN'|'CLICK'|'RENDERING_FAILURE',
            ],
            'KinesisFirehoseDestination': {
                'IamRoleArn': 'string',
                'DeliveryStreamArn': 'string'
            },
            'CloudWatchDestination': {
                'DimensionConfigurations': [
                    {
                        'DimensionName': 'string',
                        'DimensionValueSource': 'MESSAGE_TAG'|'EMAIL_HEADER'|'LINK_TAG',
                        'DefaultDimensionValue': 'string'
                    },
                ]
            },
            'SnsDestination': {
                'TopicArn': 'string'
            },
            'PinpointDestination': {
                'ApplicationArn': 'string'
            }
        }
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that you want to add an event destination to.
            

    :type EventDestinationName: string
    :param EventDestinationName: [REQUIRED]
            A name that identifies the event destination within the configuration set.
            

    :type EventDestination: dict
    :param EventDestination: [REQUIRED]
            An object that defines the event destination.
            Enabled (boolean) --If true , the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this EventDestinationDefinition .
            If false , the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.
            MatchingEventTypes (list) --An array that specifies which events Amazon Pinpoint should send to the destinations in this EventDestinationDefinition .
            (string) --An email sending event type. For example, email sends, opens, and bounces are all email events.
            KinesisFirehoseDestination (dict) --An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.
            IamRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email events to the Amazon Kinesis Data Firehose stream.
            DeliveryStreamArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon Pinpoint sends email events to.
            CloudWatchDestination (dict) --An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.
            DimensionConfigurations (list) -- [REQUIRED]An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.
            (dict) --An object that defines the dimension configuration to use when you send Amazon Pinpoint email events to Amazon CloudWatch.
            DimensionName (string) -- [REQUIRED]The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:
            It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            It can contain no more than 256 characters.
            DimensionValueSource (string) -- [REQUIRED]The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose messageTag . If you want Amazon Pinpoint to use your own email headers, choose emailHeader . If you want Amazon Pinpoint to use link tags, choose linkTags .
            DefaultDimensionValue (string) -- [REQUIRED]The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria:
            It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            It can contain no more than 256 characters.
            
            
            SnsDestination (dict) --An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notification when certain email events occur.
            TopicArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            PinpointDestination (dict) --An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
            ApplicationArn (string) --The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_dedicated_ip_pool(PoolName=None):
    """
    Create a new pool of dedicated IP addresses. A pool can include one or more dedicated IP addresses that are associated with your Amazon Pinpoint account. You can associate a pool with a configuration set. When you send an email that uses that configuration set, Amazon Pinpoint sends it using only the IP addresses in the associated pool.
    See also: AWS API Documentation
    
    
    :example: response = client.create_dedicated_ip_pool(
        PoolName='string'
    )
    
    
    :type PoolName: string
    :param PoolName: [REQUIRED]
            The name of the dedicated IP pool.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_deliverability_test_report(ReportName=None, FromEmailAddress=None, Content=None):
    """
    Create a new predictive inbox placement test. Predictive inbox placement tests can help you predict how your messages will be handled by various email providers around the world. When you perform a predictive inbox placement test, you provide a sample message that contains the content that you plan to send to your customers. Amazon Pinpoint then sends that message to special email addresses spread across several major email providers. After about 24 hours, the test is complete, and you can use the GetDeliverabilityTestReport operation to view the results of the test.
    See also: AWS API Documentation
    
    
    :example: response = client.create_deliverability_test_report(
        ReportName='string',
        FromEmailAddress='string',
        Content={
            'Simple': {
                'Subject': {
                    'Data': 'string',
                    'Charset': 'string'
                },
                'Body': {
                    'Text': {
                        'Data': 'string',
                        'Charset': 'string'
                    },
                    'Html': {
                        'Data': 'string',
                        'Charset': 'string'
                    }
                }
            },
            'Raw': {
                'Data': b'bytes'
            }
        }
    )
    
    
    :type ReportName: string
    :param ReportName: A unique name that helps you to identify the predictive inbox placement test when you retrieve the results.

    :type FromEmailAddress: string
    :param FromEmailAddress: [REQUIRED]
            The email address that the predictive inbox placement test email was sent from.
            

    :type Content: dict
    :param Content: [REQUIRED]
            The HTML body of the message that you sent when you performed the predictive inbox placement test.
            Simple (dict) --The simple email message. The message consists of a subject and a message body.
            Subject (dict) -- [REQUIRED]The subject line of the email. The subject line can only contain 7-bit ASCII characters. However, you can specify non-ASCII characters in the subject line by using encoded-word syntax, as described in RFC 2047 .
            Data (string) -- [REQUIRED]The content of the message itself.
            Charset (string) --The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify UTF-8 , ISO-8859-1 , or Shift_JIS .
            Body (dict) -- [REQUIRED]The body of the message. You can specify an HTML version of the message, a text-only version of the message, or both.
            Text (dict) --An object that represents the version of the message that is displayed in email clients that don't support HTML, or clients where the recipient has disabled HTML rendering.
            Data (string) -- [REQUIRED]The content of the message itself.
            Charset (string) --The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify UTF-8 , ISO-8859-1 , or Shift_JIS .
            Html (dict) --An object that represents the version of the message that is displayed in email clients that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.
            Data (string) -- [REQUIRED]The content of the message itself.
            Charset (string) --The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify UTF-8 , ISO-8859-1 , or Shift_JIS .
            
            Raw (dict) --The raw email message. The message has to meet the following criteria:
            The message has to contain a header and a body, separated by one blank line.
            All of the required header fields must be present in the message.
            Each part of a multipart MIME message must be formatted properly.
            If you include attachments, they must be in a file format that Amazon Pinpoint supports.
            The entire message must be Base64 encoded.
            If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.
            The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in RFC 5321 .
            Data (bytes) -- [REQUIRED]The raw email message. The message has to meet the following criteria:
            The message has to contain a header and a body, separated by one blank line.
            All of the required header fields must be present in the message.
            Each part of a multipart MIME message must be formatted properly.
            Attachments must be in a file format that Amazon Pinpoint supports.
            The entire message must be Base64 encoded.
            If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.
            The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in RFC 5321 .
            
            

    :rtype: dict
    :return: {
        'ReportId': 'string',
        'DeliverabilityTestStatus': 'IN_PROGRESS'|'COMPLETED'
    }
    
    
    """
    pass

def create_email_identity(EmailIdentity=None):
    """
    Verifies an email identity for use with Amazon Pinpoint. In Amazon Pinpoint, an identity is an email address or domain that you use when you send email. Before you can use an identity to send email with Amazon Pinpoint, you first have to verify it. By verifying an address, you demonstrate that you're the owner of the address, and that you've given Amazon Pinpoint permission to send email from the address.
    When you verify an email address, Amazon Pinpoint sends an email to the address. Your email address is verified as soon as you follow the link in the verification email.
    When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon Pinpoint detects these records in the DNS configuration for your domain. It usually takes around 72 hours to complete the domain verification process.
    See also: AWS API Documentation
    
    
    :example: response = client.create_email_identity(
        EmailIdentity='string'
    )
    
    
    :type EmailIdentity: string
    :param EmailIdentity: [REQUIRED]
            The email address or domain that you want to verify.
            

    :rtype: dict
    :return: {
        'IdentityType': 'EMAIL_ADDRESS'|'DOMAIN'|'MANAGED_DOMAIN',
        'VerifiedForSendingStatus': True|False,
        'DkimAttributes': {
            'SigningEnabled': True|False,
            'Status': 'PENDING'|'SUCCESS'|'FAILED'|'TEMPORARY_FAILURE'|'NOT_STARTED',
            'Tokens': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_configuration_set(ConfigurationSetName=None):
    """
    Delete an existing configuration set.
    In Amazon Pinpoint, configuration sets are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_configuration_set(
        ConfigurationSetName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_configuration_set_event_destination(ConfigurationSetName=None, EventDestinationName=None):
    """
    Delete an event destination.
    In Amazon Pinpoint, events include message sends, deliveries, opens, clicks, bounces, and complaints. Event destinations are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_configuration_set_event_destination(
        ConfigurationSetName='string',
        EventDestinationName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that contains the event destination that you want to delete.
            

    :type EventDestinationName: string
    :param EventDestinationName: [REQUIRED]
            The name of the event destination that you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_dedicated_ip_pool(PoolName=None):
    """
    Delete a dedicated IP pool.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_dedicated_ip_pool(
        PoolName='string'
    )
    
    
    :type PoolName: string
    :param PoolName: [REQUIRED]
            The name of the dedicated IP pool that you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_email_identity(EmailIdentity=None):
    """
    Deletes an email identity that you previously verified for use with Amazon Pinpoint. An identity can be either an email address or a domain name.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_email_identity(
        EmailIdentity='string'
    )
    
    
    :type EmailIdentity: string
    :param EmailIdentity: [REQUIRED]
            The identity (that is, the email address or domain) that you want to delete from your Amazon Pinpoint account.
            

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

def get_account():
    """
    Obtain information about the email-sending status and capabilities of your Amazon Pinpoint account in the current AWS Region.
    See also: AWS API Documentation
    
    
    :example: response = client.get_account()
    
    
    :rtype: dict
    :return: {
        'SendQuota': {
            'Max24HourSend': 123.0,
            'MaxSendRate': 123.0,
            'SentLast24Hours': 123.0
        },
        'SendingEnabled': True|False,
        'DedicatedIpAutoWarmupEnabled': True|False,
        'EnforcementStatus': 'string',
        'ProductionAccessEnabled': True|False
    }
    
    
    """
    pass

def get_blacklist_reports(BlacklistItemNames=None):
    """
    Retrieve a list of the blacklists that your dedicated IP addresses appear on.
    See also: AWS API Documentation
    
    
    :example: response = client.get_blacklist_reports(
        BlacklistItemNames=[
            'string',
        ]
    )
    
    
    :type BlacklistItemNames: list
    :param BlacklistItemNames: [REQUIRED]
            A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon Pinpoint or Amazon SES.
            (string) --An IP address that you want to obtain blacklist information for.
            

    :rtype: dict
    :return: {
        'BlacklistReport': {
            'string': [
                {
                    'RblName': 'string',
                    'ListingTime': datetime(2015, 1, 1),
                    'Description': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def get_configuration_set(ConfigurationSetName=None):
    """
    Get information about an existing configuration set, including the dedicated IP pool that it's associated with, whether or not it's enabled for sending email, and more.
    In Amazon Pinpoint, configuration sets are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
    See also: AWS API Documentation
    
    
    :example: response = client.get_configuration_set(
        ConfigurationSetName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that you want to obtain more information about.
            

    :rtype: dict
    :return: {
        'ConfigurationSetName': 'string',
        'TrackingOptions': {
            'CustomRedirectDomain': 'string'
        },
        'DeliveryOptions': {
            'SendingPoolName': 'string'
        },
        'ReputationOptions': {
            'ReputationMetricsEnabled': True|False,
            'LastFreshStart': datetime(2015, 1, 1)
        },
        'SendingOptions': {
            'SendingEnabled': True|False
        }
    }
    
    
    """
    pass

def get_configuration_set_event_destinations(ConfigurationSetName=None):
    """
    Retrieve a list of event destinations that are associated with a configuration set.
    In Amazon Pinpoint, events include message sends, deliveries, opens, clicks, bounces, and complaints. Event destinations are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
    See also: AWS API Documentation
    
    
    :example: response = client.get_configuration_set_event_destinations(
        ConfigurationSetName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that contains the event destination.
            

    :rtype: dict
    :return: {
        'EventDestinations': [
            {
                'Name': 'string',
                'Enabled': True|False,
                'MatchingEventTypes': [
                    'SEND'|'REJECT'|'BOUNCE'|'COMPLAINT'|'DELIVERY'|'OPEN'|'CLICK'|'RENDERING_FAILURE',
                ],
                'KinesisFirehoseDestination': {
                    'IamRoleArn': 'string',
                    'DeliveryStreamArn': 'string'
                },
                'CloudWatchDestination': {
                    'DimensionConfigurations': [
                        {
                            'DimensionName': 'string',
                            'DimensionValueSource': 'MESSAGE_TAG'|'EMAIL_HEADER'|'LINK_TAG',
                            'DefaultDimensionValue': 'string'
                        },
                    ]
                },
                'SnsDestination': {
                    'TopicArn': 'string'
                },
                'PinpointDestination': {
                    'ApplicationArn': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    It can contain no more than 256 characters.
    
    """
    pass

def get_dedicated_ip(Ip=None):
    """
    Get information about a dedicated IP address, including the name of the dedicated IP pool that it's associated with, as well information about the automatic warm-up process for the address.
    See also: AWS API Documentation
    
    
    :example: response = client.get_dedicated_ip(
        Ip='string'
    )
    
    
    :type Ip: string
    :param Ip: [REQUIRED]
            The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that's assocaited with your Amazon Pinpoint account.
            

    :rtype: dict
    :return: {
        'DedicatedIp': {
            'Ip': 'string',
            'WarmupStatus': 'IN_PROGRESS'|'DONE',
            'WarmupPercentage': 123,
            'PoolName': 'string'
        }
    }
    
    
    """
    pass

def get_dedicated_ips(PoolName=None, NextToken=None, PageSize=None):
    """
    List the dedicated IP addresses that are associated with your Amazon Pinpoint account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_dedicated_ips(
        PoolName='string',
        NextToken='string',
        PageSize=123
    )
    
    
    :type PoolName: string
    :param PoolName: The name of the IP pool that the dedicated IP address is associated with.

    :type NextToken: string
    :param NextToken: A token returned from a previous call to GetDedicatedIps to indicate the position of the dedicated IP pool in the list of IP pools.

    :type PageSize: integer
    :param PageSize: The number of results to show in a single call to GetDedicatedIpsRequest . If the number of results is larger than the number you specified in this parameter, then the response includes a NextToken element, which you can use to obtain additional results.

    :rtype: dict
    :return: {
        'DedicatedIps': [
            {
                'Ip': 'string',
                'WarmupStatus': 'IN_PROGRESS'|'DONE',
                'WarmupPercentage': 123,
                'PoolName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    IN_PROGRESS  The IP address isn't ready to use because the dedicated IP warm-up process is ongoing.
    DONE  The dedicated IP warm-up process is complete, and the IP address is ready to use.
    
    """
    pass

def get_deliverability_dashboard_options():
    """
    Show the status of the Deliverability dashboard. When the Deliverability dashboard is enabled, you gain access to reputation metrics for the domains that you use to send email using Amazon Pinpoint. You also gain the ability to perform predictive inbox placement tests.
    When you use the Deliverability dashboard, you pay a monthly charge of USD$1,250.00, in addition to any other fees that you accrue by using Amazon Pinpoint. If you enable the Deliverability dashboard after the first day of a calendar month, AWS prorates the monthly charge based on how many days have elapsed in the current calendar month.
    See also: AWS API Documentation
    
    
    :example: response = client.get_deliverability_dashboard_options()
    
    
    :rtype: dict
    :return: {
        'DashboardEnabled': True|False
    }
    
    
    """
    pass

def get_deliverability_test_report(ReportId=None):
    """
    Retrieve the results of a predictive inbox placement test.
    See also: AWS API Documentation
    
    
    :example: response = client.get_deliverability_test_report(
        ReportId='string'
    )
    
    
    :type ReportId: string
    :param ReportId: [REQUIRED]
            A unique string that identifies the predictive inbox placement test.
            

    :rtype: dict
    :return: {
        'DeliverabilityTestReport': {
            'ReportId': 'string',
            'ReportName': 'string',
            'Subject': 'string',
            'FromEmailAddress': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'DeliverabilityTestStatus': 'IN_PROGRESS'|'COMPLETED'
        },
        'OverallPlacement': {
            'InboxPercentage': 123.0,
            'SpamPercentage': 123.0,
            'MissingPercentage': 123.0,
            'SpfPercentage': 123.0,
            'DkimPercentage': 123.0
        },
        'IspPlacements': [
            {
                'IspName': 'string',
                'PlacementStatistics': {
                    'InboxPercentage': 123.0,
                    'SpamPercentage': 123.0,
                    'MissingPercentage': 123.0,
                    'SpfPercentage': 123.0,
                    'DkimPercentage': 123.0
                }
            },
        ],
        'Message': 'string'
    }
    
    
    """
    pass

def get_domain_statistics_report(Domain=None, StartDate=None, EndDate=None):
    """
    Retrieve inbox placement and engagement rates for the domains that you use to send email.
    See also: AWS API Documentation
    
    
    :example: response = client.get_domain_statistics_report(
        Domain='string',
        StartDate=datetime(2015, 1, 1),
        EndDate=datetime(2015, 1, 1)
    )
    
    
    :type Domain: string
    :param Domain: [REQUIRED]
            The domain that you want to obtain deliverability metrics for.
            

    :type StartDate: datetime
    :param StartDate: [REQUIRED]
            The first day (in Unix time) that you want to obtain domain deliverability metrics for.
            

    :type EndDate: datetime
    :param EndDate: [REQUIRED]
            The last day (in Unix time) that you want to obtain domain deliverability metrics for. The EndDate that you specify has to be less than or equal to 30 days after the StartDate .
            

    :rtype: dict
    :return: {
        'OverallVolume': {
            'VolumeStatistics': {
                'InboxRawCount': 123,
                'SpamRawCount': 123,
                'ProjectedInbox': 123,
                'ProjectedSpam': 123
            },
            'ReadRatePercent': 123.0,
            'DomainIspPlacements': [
                {
                    'IspName': 'string',
                    'InboxRawCount': 123,
                    'SpamRawCount': 123,
                    'InboxPercentage': 123.0,
                    'SpamPercentage': 123.0
                },
            ]
        },
        'DailyVolumes': [
            {
                'StartDate': datetime(2015, 1, 1),
                'VolumeStatistics': {
                    'InboxRawCount': 123,
                    'SpamRawCount': 123,
                    'ProjectedInbox': 123,
                    'ProjectedSpam': 123
                },
                'DomainIspPlacements': [
                    {
                        'IspName': 'string',
                        'InboxRawCount': 123,
                        'SpamRawCount': 123,
                        'InboxPercentage': 123.0,
                        'SpamPercentage': 123.0
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def get_email_identity(EmailIdentity=None):
    """
    Provides information about a specific identity associated with your Amazon Pinpoint account, including the identity's verification status, its DKIM authentication status, and its custom Mail-From settings.
    See also: AWS API Documentation
    
    
    :example: response = client.get_email_identity(
        EmailIdentity='string'
    )
    
    
    :type EmailIdentity: string
    :param EmailIdentity: [REQUIRED]
            The email identity that you want to retrieve details for.
            

    :rtype: dict
    :return: {
        'IdentityType': 'EMAIL_ADDRESS'|'DOMAIN'|'MANAGED_DOMAIN',
        'FeedbackForwardingStatus': True|False,
        'VerifiedForSendingStatus': True|False,
        'DkimAttributes': {
            'SigningEnabled': True|False,
            'Status': 'PENDING'|'SUCCESS'|'FAILED'|'TEMPORARY_FAILURE'|'NOT_STARTED',
            'Tokens': [
                'string',
            ]
        },
        'MailFromAttributes': {
            'MailFromDomain': 'string',
            'MailFromDomainStatus': 'PENDING'|'SUCCESS'|'FAILED'|'TEMPORARY_FAILURE',
            'BehaviorOnMxFailure': 'USE_DEFAULT_VALUE'|'REJECT_MESSAGE'
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter
    """
    pass

def list_configuration_sets(NextToken=None, PageSize=None):
    """
    List all of the configuration sets associated with your Amazon Pinpoint account in the current region.
    In Amazon Pinpoint, configuration sets are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
    See also: AWS API Documentation
    
    
    :example: response = client.list_configuration_sets(
        NextToken='string',
        PageSize=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token returned from a previous call to ListConfigurationSets to indicate the position in the list of configuration sets.

    :type PageSize: integer
    :param PageSize: The number of results to show in a single call to ListConfigurationSets . If the number of results is larger than the number you specified in this parameter, then the response includes a NextToken element, which you can use to obtain additional results.

    :rtype: dict
    :return: {
        'ConfigurationSets': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_dedicated_ip_pools(NextToken=None, PageSize=None):
    """
    List all of the dedicated IP pools that exist in your Amazon Pinpoint account in the current AWS Region.
    See also: AWS API Documentation
    
    
    :example: response = client.list_dedicated_ip_pools(
        NextToken='string',
        PageSize=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token returned from a previous call to ListDedicatedIpPools to indicate the position in the list of dedicated IP pools.

    :type PageSize: integer
    :param PageSize: The number of results to show in a single call to ListDedicatedIpPools . If the number of results is larger than the number you specified in this parameter, then the response includes a NextToken element, which you can use to obtain additional results.

    :rtype: dict
    :return: {
        'DedicatedIpPools': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_deliverability_test_reports(NextToken=None, PageSize=None):
    """
    Show a list of the predictive inbox placement tests that you've performed, regardless of their statuses. For predictive inbox placement tests that are complete, you can use the GetDeliverabilityTestReport operation to view the results.
    See also: AWS API Documentation
    
    
    :example: response = client.list_deliverability_test_reports(
        NextToken='string',
        PageSize=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token returned from a previous call to ListDeliverabilityTestReports to indicate the position in the list of predictive inbox placement tests.

    :type PageSize: integer
    :param PageSize: The number of results to show in a single call to ListDeliverabilityTestReports . If the number of results is larger than the number you specified in this parameter, then the response includes a NextToken element, which you can use to obtain additional results.
            The value you specify has to be at least 0, and can be no more than 1000.
            

    :rtype: dict
    :return: {
        'DeliverabilityTestReports': [
            {
                'ReportId': 'string',
                'ReportName': 'string',
                'Subject': 'string',
                'FromEmailAddress': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'DeliverabilityTestStatus': 'IN_PROGRESS'|'COMPLETED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_email_identities(NextToken=None, PageSize=None):
    """
    Returns a list of all of the email identities that are associated with your Amazon Pinpoint account. An identity can be either an email address or a domain. This operation returns identities that are verified as well as those that aren't.
    See also: AWS API Documentation
    
    
    :example: response = client.list_email_identities(
        NextToken='string',
        PageSize=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token returned from a previous call to ListEmailIdentities to indicate the position in the list of identities.

    :type PageSize: integer
    :param PageSize: The number of results to show in a single call to ListEmailIdentities . If the number of results is larger than the number you specified in this parameter, then the response includes a NextToken element, which you can use to obtain additional results.
            The value you specify has to be at least 0, and can be no more than 1000.
            

    :rtype: dict
    :return: {
        'EmailIdentities': [
            {
                'IdentityType': 'EMAIL_ADDRESS'|'DOMAIN'|'MANAGED_DOMAIN',
                'IdentityName': 'string',
                'SendingEnabled': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    EMAIL_ADDRESS  The identity is an email address.
    DOMAIN  The identity is a domain.
    MANAGED_DOMAIN  The identity is a domain that is managed by AWS.
    
    """
    pass

def put_account_dedicated_ip_warmup_attributes(AutoWarmupEnabled=None):
    """
    Enable or disable the automatic warm-up feature for dedicated IP addresses.
    See also: AWS API Documentation
    
    
    :example: response = client.put_account_dedicated_ip_warmup_attributes(
        AutoWarmupEnabled=True|False
    )
    
    
    :type AutoWarmupEnabled: boolean
    :param AutoWarmupEnabled: Enables or disables the automatic warm-up feature for dedicated IP addresses that are associated with your Amazon Pinpoint account in the current AWS Region. Set to true to enable the automatic warm-up feature, or set to false to disable it.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_account_sending_attributes(SendingEnabled=None):
    """
    Enable or disable the ability of your account to send email.
    See also: AWS API Documentation
    
    
    :example: response = client.put_account_sending_attributes(
        SendingEnabled=True|False
    )
    
    
    :type SendingEnabled: boolean
    :param SendingEnabled: Enables or disables your account's ability to send email. Set to true to enable email sending, or set to false to disable email sending.
            Note
            If AWS paused your account's ability to send email, you can't use this operation to resume your account's ability to send email.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_configuration_set_delivery_options(ConfigurationSetName=None, SendingPoolName=None):
    """
    Associate a configuration set with a dedicated IP pool. You can use dedicated IP pools to create groups of dedicated IP addresses for sending specific types of email.
    See also: AWS API Documentation
    
    
    :example: response = client.put_configuration_set_delivery_options(
        ConfigurationSetName='string',
        SendingPoolName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that you want to associate with a dedicated IP pool.
            

    :type SendingPoolName: string
    :param SendingPoolName: The name of the dedicated IP pool that you want to associate with the configuration set.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_configuration_set_reputation_options(ConfigurationSetName=None, ReputationMetricsEnabled=None):
    """
    Enable or disable collection of reputation metrics for emails that you send using a particular configuration set in a specific AWS Region.
    See also: AWS API Documentation
    
    
    :example: response = client.put_configuration_set_reputation_options(
        ConfigurationSetName='string',
        ReputationMetricsEnabled=True|False
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that you want to enable or disable reputation metric tracking for.
            

    :type ReputationMetricsEnabled: boolean
    :param ReputationMetricsEnabled: If true , tracking of reputation metrics is enabled for the configuration set. If false , tracking of reputation metrics is disabled for the configuration set.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_configuration_set_sending_options(ConfigurationSetName=None, SendingEnabled=None):
    """
    Enable or disable email sending for messages that use a particular configuration set in a specific AWS Region.
    See also: AWS API Documentation
    
    
    :example: response = client.put_configuration_set_sending_options(
        ConfigurationSetName='string',
        SendingEnabled=True|False
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that you want to enable or disable email sending for.
            

    :type SendingEnabled: boolean
    :param SendingEnabled: If true , email sending is enabled for the configuration set. If false , email sending is disabled for the configuration set.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_configuration_set_tracking_options(ConfigurationSetName=None, CustomRedirectDomain=None):
    """
    Specify a custom domain to use for open and click tracking elements in email that you send using Amazon Pinpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.put_configuration_set_tracking_options(
        ConfigurationSetName='string',
        CustomRedirectDomain='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that you want to add a custom tracking domain to.
            

    :type CustomRedirectDomain: string
    :param CustomRedirectDomain: The domain that you want to use to track open and click events.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_dedicated_ip_in_pool(Ip=None, DestinationPoolName=None):
    """
    Move a dedicated IP address to an existing dedicated IP pool.
    See also: AWS API Documentation
    
    
    :example: response = client.put_dedicated_ip_in_pool(
        Ip='string',
        DestinationPoolName='string'
    )
    
    
    :type Ip: string
    :param Ip: [REQUIRED]
            The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that's associated with your Amazon Pinpoint account.
            

    :type DestinationPoolName: string
    :param DestinationPoolName: [REQUIRED]
            The name of the IP pool that you want to add the dedicated IP address to. You have to specify an IP pool that already exists.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_dedicated_ip_warmup_attributes(Ip=None, WarmupPercentage=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.put_dedicated_ip_warmup_attributes(
        Ip='string',
        WarmupPercentage=123
    )
    
    
    :type Ip: string
    :param Ip: [REQUIRED]
            The dedicated IP address that you want to update the warm-up attributes for.
            

    :type WarmupPercentage: integer
    :param WarmupPercentage: [REQUIRED]
            The warm-up percentage that you want to associate with the dedicated IP address.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_deliverability_dashboard_option(DashboardEnabled=None):
    """
    Enable or disable the Deliverability dashboard. When you enable the Deliverability dashboard, you gain access to reputation metrics for the domains that you use to send email using Amazon Pinpoint. You also gain the ability to perform predictive inbox placement tests.
    When you use the Deliverability dashboard, you pay a monthly charge of USD$1,250.00, in addition to any other fees that you accrue by using Amazon Pinpoint. If you enable the Deliverability dashboard after the first day of a calendar month, we prorate the monthly charge based on how many days have elapsed in the current calendar month.
    See also: AWS API Documentation
    
    
    :example: response = client.put_deliverability_dashboard_option(
        DashboardEnabled=True|False
    )
    
    
    :type DashboardEnabled: boolean
    :param DashboardEnabled: [REQUIRED]
            Indicates whether the Deliverability dashboard is enabled. If the value is true , then the dashboard is enabled.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_email_identity_dkim_attributes(EmailIdentity=None, SigningEnabled=None):
    """
    Used to enable or disable DKIM authentication for an email identity.
    See also: AWS API Documentation
    
    
    :example: response = client.put_email_identity_dkim_attributes(
        EmailIdentity='string',
        SigningEnabled=True|False
    )
    
    
    :type EmailIdentity: string
    :param EmailIdentity: [REQUIRED]
            The email identity that you want to change the DKIM settings for.
            

    :type SigningEnabled: boolean
    :param SigningEnabled: Sets the DKIM signing configuration for the identity.
            When you set this value true , then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. When you set this value to false , then the messages that Amazon Pinpoint sends from the identity aren't DKIM-signed.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_email_identity_feedback_attributes(EmailIdentity=None, EmailForwardingEnabled=None):
    """
    Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.
    When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.
    When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
    See also: AWS API Documentation
    
    
    :example: response = client.put_email_identity_feedback_attributes(
        EmailIdentity='string',
        EmailForwardingEnabled=True|False
    )
    
    
    :type EmailIdentity: string
    :param EmailIdentity: [REQUIRED]
            The email identity that you want to configure bounce and complaint feedback forwarding for.
            

    :type EmailForwardingEnabled: boolean
    :param EmailForwardingEnabled: Sets the feedback forwarding configuration for the identity.
            If the value is true , Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.
            When you set this value to false , Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_email_identity_mail_from_attributes(EmailIdentity=None, MailFromDomain=None, BehaviorOnMxFailure=None):
    """
    Used to enable or disable the custom Mail-From domain configuration for an email identity.
    See also: AWS API Documentation
    
    
    :example: response = client.put_email_identity_mail_from_attributes(
        EmailIdentity='string',
        MailFromDomain='string',
        BehaviorOnMxFailure='USE_DEFAULT_VALUE'|'REJECT_MESSAGE'
    )
    
    
    :type EmailIdentity: string
    :param EmailIdentity: [REQUIRED]
            The verified email identity that you want to set up the custom MAIL FROM domain for.
            

    :type MailFromDomain: string
    :param MailFromDomain: The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria:
            It has to be a subdomain of the verified identity.
            It can't be used to receive email.
            It can't be used in a 'From' address if the MAIL FROM domain is a destination for feedback forwarding emails.
            

    :type BehaviorOnMxFailure: string
    :param BehaviorOnMxFailure: The action that you want Amazon Pinpoint to take if it can't read the required MX record when you send an email. When you set this value to UseDefaultValue , Amazon Pinpoint uses amazonses.com as the MAIL FROM domain. When you set this value to RejectMessage , Amazon Pinpoint returns a MailFromDomainNotVerified error, and doesn't attempt to deliver the email.
            These behaviors are taken when the custom MAIL FROM domain configuration is in the Pending , Failed , and TemporaryFailure states.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def send_email(FromEmailAddress=None, Destination=None, ReplyToAddresses=None, FeedbackForwardingEmailAddress=None, Content=None, EmailTags=None, ConfigurationSetName=None):
    """
    Sends an email message. You can use the Amazon Pinpoint Email API to send two types of messages:
    See also: AWS API Documentation
    
    
    :example: response = client.send_email(
        FromEmailAddress='string',
        Destination={
            'ToAddresses': [
                'string',
            ],
            'CcAddresses': [
                'string',
            ],
            'BccAddresses': [
                'string',
            ]
        },
        ReplyToAddresses=[
            'string',
        ],
        FeedbackForwardingEmailAddress='string',
        Content={
            'Simple': {
                'Subject': {
                    'Data': 'string',
                    'Charset': 'string'
                },
                'Body': {
                    'Text': {
                        'Data': 'string',
                        'Charset': 'string'
                    },
                    'Html': {
                        'Data': 'string',
                        'Charset': 'string'
                    }
                }
            },
            'Raw': {
                'Data': b'bytes'
            }
        },
        EmailTags=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        ConfigurationSetName='string'
    )
    
    
    :type FromEmailAddress: string
    :param FromEmailAddress: The email address that you want to use as the 'From' address for the email. The address that you specify has to be verified.

    :type Destination: dict
    :param Destination: [REQUIRED]
            An object that contains the recipients of the email message.
            ToAddresses (list) --An array that contains the email addresses of the 'To' recipients for the email.
            (string) --
            CcAddresses (list) --An array that contains the email addresses of the 'CC' (carbon copy) recipients for the email.
            (string) --
            BccAddresses (list) --An array that contains the email addresses of the 'BCC' (blind carbon copy) recipients for the email.
            (string) --
            

    :type ReplyToAddresses: list
    :param ReplyToAddresses: The 'Reply-to' email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.
            (string) --
            

    :type FeedbackForwardingEmailAddress: string
    :param FeedbackForwardingEmailAddress: The address that Amazon Pinpoint should send bounce and complaint notifications to.

    :type Content: dict
    :param Content: [REQUIRED]
            An object that contains the body of the message. You can send either a Simple message or a Raw message.
            Simple (dict) --The simple email message. The message consists of a subject and a message body.
            Subject (dict) -- [REQUIRED]The subject line of the email. The subject line can only contain 7-bit ASCII characters. However, you can specify non-ASCII characters in the subject line by using encoded-word syntax, as described in RFC 2047 .
            Data (string) -- [REQUIRED]The content of the message itself.
            Charset (string) --The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify UTF-8 , ISO-8859-1 , or Shift_JIS .
            Body (dict) -- [REQUIRED]The body of the message. You can specify an HTML version of the message, a text-only version of the message, or both.
            Text (dict) --An object that represents the version of the message that is displayed in email clients that don't support HTML, or clients where the recipient has disabled HTML rendering.
            Data (string) -- [REQUIRED]The content of the message itself.
            Charset (string) --The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify UTF-8 , ISO-8859-1 , or Shift_JIS .
            Html (dict) --An object that represents the version of the message that is displayed in email clients that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.
            Data (string) -- [REQUIRED]The content of the message itself.
            Charset (string) --The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify UTF-8 , ISO-8859-1 , or Shift_JIS .
            
            Raw (dict) --The raw email message. The message has to meet the following criteria:
            The message has to contain a header and a body, separated by one blank line.
            All of the required header fields must be present in the message.
            Each part of a multipart MIME message must be formatted properly.
            If you include attachments, they must be in a file format that Amazon Pinpoint supports.
            The entire message must be Base64 encoded.
            If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.
            The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in RFC 5321 .
            Data (bytes) -- [REQUIRED]The raw email message. The message has to meet the following criteria:
            The message has to contain a header and a body, separated by one blank line.
            All of the required header fields must be present in the message.
            Each part of a multipart MIME message must be formatted properly.
            Attachments must be in a file format that Amazon Pinpoint supports.
            The entire message must be Base64 encoded.
            If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.
            The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in RFC 5321 .
            
            

    :type EmailTags: list
    :param EmailTags: A list of tags, in the form of name/value pairs, to apply to an email that you send using the SendEmail operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
            (dict) --Contains the name and value of a tag that you apply to an email. You can use message tags when you publish email sending events.
            Name (string) -- [REQUIRED]The name of the message tag. The message tag name has to meet the following criteria:
            It can only contain ASCII letters (a z, A Z), numbers (0 9), underscores (_), or dashes (-).
            It can contain no more than 256 characters.
            Value (string) -- [REQUIRED]The value of the message tag. The message tag value has to meet the following criteria:
            It can only contain ASCII letters (a z, A Z), numbers (0 9), underscores (_), or dashes (-).
            It can contain no more than 256 characters.
            
            

    :type ConfigurationSetName: string
    :param ConfigurationSetName: The name of the configuration set that you want to use when sending the email.

    :rtype: dict
    :return: {
        'MessageId': 'string'
    }
    
    
    :returns: 
    FromEmailAddress (string) -- The email address that you want to use as the "From" address for the email. The address that you specify has to be verified.
    Destination (dict) -- [REQUIRED]
    An object that contains the recipients of the email message.
    
    ToAddresses (list) --An array that contains the email addresses of the "To" recipients for the email.
    
    (string) --
    
    
    CcAddresses (list) --An array that contains the email addresses of the "CC" (carbon copy) recipients for the email.
    
    (string) --
    
    
    BccAddresses (list) --An array that contains the email addresses of the "BCC" (blind carbon copy) recipients for the email.
    
    (string) --
    
    
    
    
    ReplyToAddresses (list) -- The "Reply-to" email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.
    
    (string) --
    
    
    FeedbackForwardingEmailAddress (string) -- The address that Amazon Pinpoint should send bounce and complaint notifications to.
    Content (dict) -- [REQUIRED]
    An object that contains the body of the message. You can send either a Simple message or a Raw message.
    
    Simple (dict) --The simple email message. The message consists of a subject and a message body.
    
    Subject (dict) -- [REQUIRED]The subject line of the email. The subject line can only contain 7-bit ASCII characters. However, you can specify non-ASCII characters in the subject line by using encoded-word syntax, as described in RFC 2047 .
    
    Data (string) -- [REQUIRED]The content of the message itself.
    
    Charset (string) --The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify UTF-8 , ISO-8859-1 , or Shift_JIS .
    
    
    
    Body (dict) -- [REQUIRED]The body of the message. You can specify an HTML version of the message, a text-only version of the message, or both.
    
    Text (dict) --An object that represents the version of the message that is displayed in email clients that don't support HTML, or clients where the recipient has disabled HTML rendering.
    
    Data (string) -- [REQUIRED]The content of the message itself.
    
    Charset (string) --The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify UTF-8 , ISO-8859-1 , or Shift_JIS .
    
    
    
    Html (dict) --An object that represents the version of the message that is displayed in email clients that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.
    
    Data (string) -- [REQUIRED]The content of the message itself.
    
    Charset (string) --The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify UTF-8 , ISO-8859-1 , or Shift_JIS .
    
    
    
    
    
    
    
    Raw (dict) --The raw email message. The message has to meet the following criteria:
    
    The message has to contain a header and a body, separated by one blank line.
    All of the required header fields must be present in the message.
    Each part of a multipart MIME message must be formatted properly.
    If you include attachments, they must be in a file format that Amazon Pinpoint supports.
    The entire message must be Base64 encoded.
    If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.
    The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in RFC 5321 .
    
    
    Data (bytes) -- [REQUIRED]The raw email message. The message has to meet the following criteria:
    
    The message has to contain a header and a body, separated by one blank line.
    All of the required header fields must be present in the message.
    Each part of a multipart MIME message must be formatted properly.
    Attachments must be in a file format that Amazon Pinpoint supports.
    The entire message must be Base64 encoded.
    If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.
    The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in RFC 5321 .
    
    
    
    
    
    
    EmailTags (list) -- A list of tags, in the form of name/value pairs, to apply to an email that you send using the SendEmail operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
    
    (dict) --Contains the name and value of a tag that you apply to an email. You can use message tags when you publish email sending events.
    
    Name (string) -- [REQUIRED]The name of the message tag. The message tag name has to meet the following criteria:
    
    It can only contain ASCII letters (az, AZ), numbers (09), underscores (_), or dashes (-).
    It can contain no more than 256 characters.
    
    
    Value (string) -- [REQUIRED]The value of the message tag. The message tag value has to meet the following criteria:
    
    It can only contain ASCII letters (az, AZ), numbers (09), underscores (_), or dashes (-).
    It can contain no more than 256 characters.
    
    
    
    
    
    
    ConfigurationSetName (string) -- The name of the configuration set that you want to use when sending the email.
    
    """
    pass

def update_configuration_set_event_destination(ConfigurationSetName=None, EventDestinationName=None, EventDestination=None):
    """
    Update the configuration of an event destination for a configuration set.
    In Amazon Pinpoint, events include message sends, deliveries, opens, clicks, bounces, and complaints. Event destinations are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.
    See also: AWS API Documentation
    
    
    :example: response = client.update_configuration_set_event_destination(
        ConfigurationSetName='string',
        EventDestinationName='string',
        EventDestination={
            'Enabled': True|False,
            'MatchingEventTypes': [
                'SEND'|'REJECT'|'BOUNCE'|'COMPLAINT'|'DELIVERY'|'OPEN'|'CLICK'|'RENDERING_FAILURE',
            ],
            'KinesisFirehoseDestination': {
                'IamRoleArn': 'string',
                'DeliveryStreamArn': 'string'
            },
            'CloudWatchDestination': {
                'DimensionConfigurations': [
                    {
                        'DimensionName': 'string',
                        'DimensionValueSource': 'MESSAGE_TAG'|'EMAIL_HEADER'|'LINK_TAG',
                        'DefaultDimensionValue': 'string'
                    },
                ]
            },
            'SnsDestination': {
                'TopicArn': 'string'
            },
            'PinpointDestination': {
                'ApplicationArn': 'string'
            }
        }
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that contains the event destination that you want to modify.
            

    :type EventDestinationName: string
    :param EventDestinationName: [REQUIRED]
            The name of the event destination that you want to modify.
            

    :type EventDestination: dict
    :param EventDestination: [REQUIRED]
            An object that defines the event destination.
            Enabled (boolean) --If true , the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this EventDestinationDefinition .
            If false , the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.
            MatchingEventTypes (list) --An array that specifies which events Amazon Pinpoint should send to the destinations in this EventDestinationDefinition .
            (string) --An email sending event type. For example, email sends, opens, and bounces are all email events.
            KinesisFirehoseDestination (dict) --An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.
            IamRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email events to the Amazon Kinesis Data Firehose stream.
            DeliveryStreamArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon Pinpoint sends email events to.
            CloudWatchDestination (dict) --An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.
            DimensionConfigurations (list) -- [REQUIRED]An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.
            (dict) --An object that defines the dimension configuration to use when you send Amazon Pinpoint email events to Amazon CloudWatch.
            DimensionName (string) -- [REQUIRED]The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:
            It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            It can contain no more than 256 characters.
            DimensionValueSource (string) -- [REQUIRED]The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose messageTag . If you want Amazon Pinpoint to use your own email headers, choose emailHeader . If you want Amazon Pinpoint to use link tags, choose linkTags .
            DefaultDimensionValue (string) -- [REQUIRED]The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria:
            It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            It can contain no more than 256 characters.
            
            
            SnsDestination (dict) --An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notification when certain email events occur.
            TopicArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            PinpointDestination (dict) --An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
            ApplicationArn (string) --The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

