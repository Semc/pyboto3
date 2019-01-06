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

def approve_skill(SkillId=None):
    """
    Associates a skill with the organization under the customer's AWS account. If a skill is private, the user implicitly accepts access to this skill during enablement.
    See also: AWS API Documentation
    
    
    :example: response = client.approve_skill(
        SkillId='string'
    )
    
    
    :type SkillId: string
    :param SkillId: [REQUIRED]
            The unique identifier of the skill.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def associate_contact_with_address_book(ContactArn=None, AddressBookArn=None):
    """
    Associates a contact with a given address book.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_contact_with_address_book(
        ContactArn='string',
        AddressBookArn='string'
    )
    
    
    :type ContactArn: string
    :param ContactArn: [REQUIRED]
            The ARN of the contact to associate with an address book.
            

    :type AddressBookArn: string
    :param AddressBookArn: [REQUIRED]
            The ARN of the address book with which to associate the contact.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_device_with_room(DeviceArn=None, RoomArn=None):
    """
    Associates a device with a given room. This applies all the settings from the room profile to the device, and all the skills in any skill groups added to that room. This operation requires the device to be online, or else a manual sync is required.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_device_with_room(
        DeviceArn='string',
        RoomArn='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: The ARN of the device to associate to a room. Required.

    :type RoomArn: string
    :param RoomArn: The ARN of the room with which to associate the device. Required.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_skill_group_with_room(SkillGroupArn=None, RoomArn=None):
    """
    Associates a skill group with a given room. This enables all skills in the associated skill group on all devices in the room.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_skill_group_with_room(
        SkillGroupArn='string',
        RoomArn='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group to associate with a room. Required.

    :type RoomArn: string
    :param RoomArn: The ARN of the room with which to associate the skill group. Required.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_skill_with_skill_group(SkillGroupArn=None, SkillId=None):
    """
    Associates a skill with a skill group.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_skill_with_skill_group(
        SkillGroupArn='string',
        SkillId='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group to associate the skill to. Required.

    :type SkillId: string
    :param SkillId: [REQUIRED]
            The unique identifier of the skill.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_skill_with_users(OrganizationArn=None, SkillId=None):
    """
    Makes a private skill available for enrolled users to enable on their devices.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_skill_with_users(
        OrganizationArn='string',
        SkillId='string'
    )
    
    
    :type OrganizationArn: string
    :param OrganizationArn: The ARN of the organization.

    :type SkillId: string
    :param SkillId: [REQUIRED]
            The private skill ID you want to make available to enrolled users.>
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def create_address_book(Name=None, Description=None, ClientRequestToken=None):
    """
    Creates an address book with the specified details.
    See also: AWS API Documentation
    
    
    :example: response = client.create_address_book(
        Name='string',
        Description='string',
        ClientRequestToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the address book.
            

    :type Description: string
    :param Description: The description of the address book.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, user-specified identifier for the request that ensures idempotency.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'AddressBookArn': 'string'
    }
    
    
    """
    pass

def create_business_report_schedule(ScheduleName=None, S3BucketName=None, S3KeyPrefix=None, Format=None, ContentRange=None, Recurrence=None, ClientRequestToken=None):
    """
    Creates a recurring schedule for usage reports to deliver to the specified S3 location with a specified daily or weekly interval.
    See also: AWS API Documentation
    
    
    :example: response = client.create_business_report_schedule(
        ScheduleName='string',
        S3BucketName='string',
        S3KeyPrefix='string',
        Format='CSV'|'CSV_ZIP',
        ContentRange={
            'Interval': 'ONE_DAY'|'ONE_WEEK'
        },
        Recurrence={
            'StartDate': 'string'
        },
        ClientRequestToken='string'
    )
    
    
    :type ScheduleName: string
    :param ScheduleName: The name identifier of the schedule.

    :type S3BucketName: string
    :param S3BucketName: The S3 bucket name of the output reports.

    :type S3KeyPrefix: string
    :param S3KeyPrefix: The S3 key where the report is delivered.

    :type Format: string
    :param Format: [REQUIRED]
            The format of the generated report (individual CSV files or zipped files of individual files).
            

    :type ContentRange: dict
    :param ContentRange: [REQUIRED]
            The content range of the reports.
            Interval (string) --The interval of the content range.
            

    :type Recurrence: dict
    :param Recurrence: The recurrence of the reports.
            StartDate (string) --The start date.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: The client request token.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'ScheduleArn': 'string'
    }
    
    
    """
    pass

def create_conference_provider(ConferenceProviderName=None, ConferenceProviderType=None, IPDialIn=None, PSTNDialIn=None, MeetingSetting=None, ClientRequestToken=None):
    """
    Adds a new conference provider under the user's AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.create_conference_provider(
        ConferenceProviderName='string',
        ConferenceProviderType='CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'|'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
        IPDialIn={
            'Endpoint': 'string',
            'CommsProtocol': 'SIP'|'SIPS'|'H323'
        },
        PSTNDialIn={
            'CountryCode': 'string',
            'PhoneNumber': 'string',
            'OneClickIdDelay': 'string',
            'OneClickPinDelay': 'string'
        },
        MeetingSetting={
            'RequirePin': 'YES'|'NO'|'OPTIONAL'
        },
        ClientRequestToken='string'
    )
    
    
    :type ConferenceProviderName: string
    :param ConferenceProviderName: [REQUIRED]
            The name of the conference provider.
            

    :type ConferenceProviderType: string
    :param ConferenceProviderType: [REQUIRED]
            Represents a type within a list of predefined types.
            

    :type IPDialIn: dict
    :param IPDialIn: The IP endpoint and protocol for calling.
            Endpoint (string) -- [REQUIRED]The IP address.
            CommsProtocol (string) -- [REQUIRED]The protocol, including SIP, SIPS, and H323.
            

    :type PSTNDialIn: dict
    :param PSTNDialIn: The information for PSTN conferencing.
            CountryCode (string) -- [REQUIRED]The zip code.
            PhoneNumber (string) -- [REQUIRED]The phone number to call to join the conference.
            OneClickIdDelay (string) -- [REQUIRED]The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
            OneClickPinDelay (string) -- [REQUIRED]The delay duration before Alexa enters the conference pin with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
            

    :type MeetingSetting: dict
    :param MeetingSetting: [REQUIRED]
            The meeting settings for the conference provider.
            RequirePin (string) -- [REQUIRED]The values that indicate whether the pin is always required.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: The request token of the client.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'ConferenceProviderArn': 'string'
    }
    
    
    """
    pass

def create_contact(DisplayName=None, FirstName=None, LastName=None, PhoneNumber=None, ClientRequestToken=None):
    """
    Creates a contact with the specified details.
    See also: AWS API Documentation
    
    
    :example: response = client.create_contact(
        DisplayName='string',
        FirstName='string',
        LastName='string',
        PhoneNumber='string',
        ClientRequestToken='string'
    )
    
    
    :type DisplayName: string
    :param DisplayName: The name of the contact to display on the console.

    :type FirstName: string
    :param FirstName: [REQUIRED]
            The first name of the contact that is used to call the contact on the device.
            

    :type LastName: string
    :param LastName: The last name of the contact that is used to call the contact on the device.

    :type PhoneNumber: string
    :param PhoneNumber: The phone number of the contact in E.164 format.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, user-specified identifier for this request that ensures idempotency.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'ContactArn': 'string'
    }
    
    
    """
    pass

def create_profile(ProfileName=None, Timezone=None, Address=None, DistanceUnit=None, TemperatureUnit=None, WakeWord=None, ClientRequestToken=None, SetupModeDisabled=None, MaxVolumeLimit=None, PSTNEnabled=None):
    """
    Creates a new room profile with the specified details.
    See also: AWS API Documentation
    
    
    :example: response = client.create_profile(
        ProfileName='string',
        Timezone='string',
        Address='string',
        DistanceUnit='METRIC'|'IMPERIAL',
        TemperatureUnit='FAHRENHEIT'|'CELSIUS',
        WakeWord='ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
        ClientRequestToken='string',
        SetupModeDisabled=True|False,
        MaxVolumeLimit=123,
        PSTNEnabled=True|False
    )
    
    
    :type ProfileName: string
    :param ProfileName: [REQUIRED]
            The name of a room profile.
            

    :type Timezone: string
    :param Timezone: [REQUIRED]
            The time zone used by a room profile.
            

    :type Address: string
    :param Address: [REQUIRED]
            The valid address for the room.
            

    :type DistanceUnit: string
    :param DistanceUnit: [REQUIRED]
            The distance unit to be used by devices in the profile.
            

    :type TemperatureUnit: string
    :param TemperatureUnit: [REQUIRED]
            The temperature unit to be used by devices in the profile.
            

    :type WakeWord: string
    :param WakeWord: [REQUIRED]
            A wake word for Alexa, Echo, Amazon, or a computer.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: The user-specified token that is used during the creation of a profile.
            This field is autopopulated if not provided.
            

    :type SetupModeDisabled: boolean
    :param SetupModeDisabled: Whether room profile setup is enabled.

    :type MaxVolumeLimit: integer
    :param MaxVolumeLimit: The maximum volume limit for a room profile.

    :type PSTNEnabled: boolean
    :param PSTNEnabled: Whether PSTN calling is enabled.

    :rtype: dict
    :return: {
        'ProfileArn': 'string'
    }
    
    
    """
    pass

def create_room(RoomName=None, Description=None, ProfileArn=None, ProviderCalendarId=None, ClientRequestToken=None, Tags=None):
    """
    Creates a room with the specified details.
    See also: AWS API Documentation
    
    
    :example: response = client.create_room(
        RoomName='string',
        Description='string',
        ProfileArn='string',
        ProviderCalendarId='string',
        ClientRequestToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type RoomName: string
    :param RoomName: [REQUIRED]
            The name for the room.
            

    :type Description: string
    :param Description: The description for the room.

    :type ProfileArn: string
    :param ProfileArn: The profile ARN for the room.

    :type ProviderCalendarId: string
    :param ProviderCalendarId: The calendar ARN for the room.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, user-specified identifier for this request that ensures idempotency.
            This field is autopopulated if not provided.
            

    :type Tags: list
    :param Tags: The tags for the room.
            (dict) --A key-value pair that can be associated with a resource.
            Key (string) -- [REQUIRED]The key of a tag. Tag keys are case-sensitive.
            Value (string) -- [REQUIRED]The value of a tag. Tag values are case-sensitive and can be null.
            
            

    :rtype: dict
    :return: {
        'RoomArn': 'string'
    }
    
    
    """
    pass

def create_skill_group(SkillGroupName=None, Description=None, ClientRequestToken=None):
    """
    Creates a skill group with a specified name and description.
    See also: AWS API Documentation
    
    
    :example: response = client.create_skill_group(
        SkillGroupName='string',
        Description='string',
        ClientRequestToken='string'
    )
    
    
    :type SkillGroupName: string
    :param SkillGroupName: [REQUIRED]
            The name for the skill group.
            

    :type Description: string
    :param Description: The description for the skill group.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, user-specified identifier for this request that ensures idempotency.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'SkillGroupArn': 'string'
    }
    
    
    """
    pass

def create_user(UserId=None, FirstName=None, LastName=None, Email=None, ClientRequestToken=None, Tags=None):
    """
    Creates a user.
    See also: AWS API Documentation
    
    
    :example: response = client.create_user(
        UserId='string',
        FirstName='string',
        LastName='string',
        Email='string',
        ClientRequestToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]
            The ARN for the user.
            

    :type FirstName: string
    :param FirstName: The first name for the user.

    :type LastName: string
    :param LastName: The last name for the user.

    :type Email: string
    :param Email: The email address for the user.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, user-specified identifier for this request that ensures idempotency.
            This field is autopopulated if not provided.
            

    :type Tags: list
    :param Tags: The tags for the user.
            (dict) --A key-value pair that can be associated with a resource.
            Key (string) -- [REQUIRED]The key of a tag. Tag keys are case-sensitive.
            Value (string) -- [REQUIRED]The value of a tag. Tag values are case-sensitive and can be null.
            
            

    :rtype: dict
    :return: {
        'UserArn': 'string'
    }
    
    
    """
    pass

def delete_address_book(AddressBookArn=None):
    """
    Deletes an address book by the address book ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_address_book(
        AddressBookArn='string'
    )
    
    
    :type AddressBookArn: string
    :param AddressBookArn: [REQUIRED]
            The ARN of the address book to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_business_report_schedule(ScheduleArn=None):
    """
    Deletes the recurring report delivery schedule with the specified schedule ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_business_report_schedule(
        ScheduleArn='string'
    )
    
    
    :type ScheduleArn: string
    :param ScheduleArn: [REQUIRED]
            The ARN of the business report schedule.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_conference_provider(ConferenceProviderArn=None):
    """
    Deletes a conference provider.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_conference_provider(
        ConferenceProviderArn='string'
    )
    
    
    :type ConferenceProviderArn: string
    :param ConferenceProviderArn: [REQUIRED]
            The ARN of the conference provider.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_contact(ContactArn=None):
    """
    Deletes a contact by the contact ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_contact(
        ContactArn='string'
    )
    
    
    :type ContactArn: string
    :param ContactArn: [REQUIRED]
            The ARN of the contact to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_device(DeviceArn=None):
    """
    Removes a device from Alexa For Business.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_device(
        DeviceArn='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: [REQUIRED]
            The ARN of the device for which to request details.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_profile(ProfileArn=None):
    """
    Deletes a room profile by the profile ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_profile(
        ProfileArn='string'
    )
    
    
    :type ProfileArn: string
    :param ProfileArn: The ARN of the room profile to delete. Required.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_room(RoomArn=None):
    """
    Deletes a room by the room ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_room(
        RoomArn='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room to delete. Required.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_room_skill_parameter(RoomArn=None, SkillId=None, ParameterKey=None):
    """
    Deletes room skill parameter details by room, skill, and parameter key ID.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_room_skill_parameter(
        RoomArn='string',
        SkillId='string',
        ParameterKey='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room from which to remove the room skill parameter details.

    :type SkillId: string
    :param SkillId: [REQUIRED]
            The ID of the skill from which to remove the room skill parameter details.
            

    :type ParameterKey: string
    :param ParameterKey: [REQUIRED]
            The room skill parameter key for which to remove details.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_skill_authorization(SkillId=None, RoomArn=None):
    """
    Unlinks a third-party account from a skill.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_skill_authorization(
        SkillId='string',
        RoomArn='string'
    )
    
    
    :type SkillId: string
    :param SkillId: [REQUIRED]
            The unique identifier of a skill.
            

    :type RoomArn: string
    :param RoomArn: The room that the skill is authorized for.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_skill_group(SkillGroupArn=None):
    """
    Deletes a skill group by skill group ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_skill_group(
        SkillGroupArn='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group to delete. Required.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_user(UserArn=None, EnrollmentId=None):
    """
    Deletes a specified user by user ARN and enrollment ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user(
        UserArn='string',
        EnrollmentId='string'
    )
    
    
    :type UserArn: string
    :param UserArn: The ARN of the user to delete in the organization. Required.

    :type EnrollmentId: string
    :param EnrollmentId: [REQUIRED]
            The ARN of the user's enrollment in the organization. Required.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_contact_from_address_book(ContactArn=None, AddressBookArn=None):
    """
    Disassociates a contact from a given address book.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_contact_from_address_book(
        ContactArn='string',
        AddressBookArn='string'
    )
    
    
    :type ContactArn: string
    :param ContactArn: [REQUIRED]
            The ARN of the contact to disassociate from an address book.
            

    :type AddressBookArn: string
    :param AddressBookArn: [REQUIRED]
            The ARN of the address from which to disassociate the contact.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_device_from_room(DeviceArn=None):
    """
    Disassociates a device from its current room. The device continues to be connected to the Wi-Fi network and is still registered to the account. The device settings and skills are removed from the room.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_device_from_room(
        DeviceArn='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: The ARN of the device to disassociate from a room. Required.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def disassociate_skill_from_skill_group(SkillGroupArn=None, SkillId=None):
    """
    Disassociates a skill from a skill group.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_skill_from_skill_group(
        SkillGroupArn='string',
        SkillId='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The unique identifier of a skill. Required.

    :type SkillId: string
    :param SkillId: [REQUIRED]
            The ARN of a skill group to associate to a skill.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_skill_from_users(OrganizationArn=None, SkillId=None):
    """
    Makes a private skill unavailable for enrolled users and prevents them from enabling it on their devices.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_skill_from_users(
        OrganizationArn='string',
        SkillId='string'
    )
    
    
    :type OrganizationArn: string
    :param OrganizationArn: The ARN of the organization.

    :type SkillId: string
    :param SkillId: [REQUIRED]
            The private skill ID you want to make unavailable for enrolled users.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_skill_group_from_room(SkillGroupArn=None, RoomArn=None):
    """
    Disassociates a skill group from a specified room. This disables all skills in the skill group on all devices in the room.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_skill_group_from_room(
        SkillGroupArn='string',
        RoomArn='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group to disassociate from a room. Required.

    :type RoomArn: string
    :param RoomArn: The ARN of the room from which the skill group is to be disassociated. Required.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def forget_smart_home_appliances(RoomArn=None):
    """
    Forgets smart home appliances associated to a room.
    See also: AWS API Documentation
    
    
    :example: response = client.forget_smart_home_appliances(
        RoomArn='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: [REQUIRED]
            The room that the appliances are associated with.
            

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

def get_address_book(AddressBookArn=None):
    """
    Gets address the book details by the address book ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.get_address_book(
        AddressBookArn='string'
    )
    
    
    :type AddressBookArn: string
    :param AddressBookArn: [REQUIRED]
            The ARN of the address book for which to request details.
            

    :rtype: dict
    :return: {
        'AddressBook': {
            'AddressBookArn': 'string',
            'Name': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def get_conference_preference():
    """
    Retrieves the existing conference preferences.
    See also: AWS API Documentation
    
    
    :example: response = client.get_conference_preference()
    
    
    :rtype: dict
    :return: {
        'Preference': {
            'DefaultConferenceProviderArn': 'string'
        }
    }
    
    
    """
    pass

def get_conference_provider(ConferenceProviderArn=None):
    """
    Gets details about a specific conference provider.
    See also: AWS API Documentation
    
    
    :example: response = client.get_conference_provider(
        ConferenceProviderArn='string'
    )
    
    
    :type ConferenceProviderArn: string
    :param ConferenceProviderArn: [REQUIRED]
            The ARN of the newly created conference provider.
            

    :rtype: dict
    :return: {
        'ConferenceProvider': {
            'Arn': 'string',
            'Name': 'string',
            'Type': 'CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'|'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
            'IPDialIn': {
                'Endpoint': 'string',
                'CommsProtocol': 'SIP'|'SIPS'|'H323'
            },
            'PSTNDialIn': {
                'CountryCode': 'string',
                'PhoneNumber': 'string',
                'OneClickIdDelay': 'string',
                'OneClickPinDelay': 'string'
            },
            'MeetingSetting': {
                'RequirePin': 'YES'|'NO'|'OPTIONAL'
            }
        }
    }
    
    
    """
    pass

def get_contact(ContactArn=None):
    """
    Gets the contact details by the contact ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.get_contact(
        ContactArn='string'
    )
    
    
    :type ContactArn: string
    :param ContactArn: [REQUIRED]
            The ARN of the contact for which to request details.
            

    :rtype: dict
    :return: {
        'Contact': {
            'ContactArn': 'string',
            'DisplayName': 'string',
            'FirstName': 'string',
            'LastName': 'string',
            'PhoneNumber': 'string'
        }
    }
    
    
    """
    pass

def get_device(DeviceArn=None):
    """
    Gets the details of a device by device ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.get_device(
        DeviceArn='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: The ARN of the device for which to request details. Required.

    :rtype: dict
    :return: {
        'Device': {
            'DeviceArn': 'string',
            'DeviceSerialNumber': 'string',
            'DeviceType': 'string',
            'DeviceName': 'string',
            'SoftwareVersion': 'string',
            'MacAddress': 'string',
            'RoomArn': 'string',
            'DeviceStatus': 'READY'|'PENDING'|'WAS_OFFLINE'|'DEREGISTERED',
            'DeviceStatusInfo': {
                'DeviceStatusDetails': [
                    {
                        'Code': 'DEVICE_SOFTWARE_UPDATE_NEEDED'|'DEVICE_WAS_OFFLINE'
                    },
                ],
                'ConnectionStatus': 'ONLINE'|'OFFLINE'
            }
        }
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

def get_profile(ProfileArn=None):
    """
    Gets the details of a room profile by profile ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.get_profile(
        ProfileArn='string'
    )
    
    
    :type ProfileArn: string
    :param ProfileArn: The ARN of the room profile for which to request details. Required.

    :rtype: dict
    :return: {
        'Profile': {
            'ProfileArn': 'string',
            'ProfileName': 'string',
            'IsDefault': True|False,
            'Address': 'string',
            'Timezone': 'string',
            'DistanceUnit': 'METRIC'|'IMPERIAL',
            'TemperatureUnit': 'FAHRENHEIT'|'CELSIUS',
            'WakeWord': 'ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
            'SetupModeDisabled': True|False,
            'MaxVolumeLimit': 123,
            'PSTNEnabled': True|False,
            'AddressBookArn': 'string'
        }
    }
    
    
    """
    pass

def get_room(RoomArn=None):
    """
    Gets room details by room ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.get_room(
        RoomArn='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room for which to request details. Required.

    :rtype: dict
    :return: {
        'Room': {
            'RoomArn': 'string',
            'RoomName': 'string',
            'Description': 'string',
            'ProviderCalendarId': 'string',
            'ProfileArn': 'string'
        }
    }
    
    
    """
    pass

def get_room_skill_parameter(RoomArn=None, SkillId=None, ParameterKey=None):
    """
    Gets room skill parameter details by room, skill, and parameter key ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.get_room_skill_parameter(
        RoomArn='string',
        SkillId='string',
        ParameterKey='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room from which to get the room skill parameter details.

    :type SkillId: string
    :param SkillId: [REQUIRED]
            The ARN of the skill from which to get the room skill parameter details. Required.
            

    :type ParameterKey: string
    :param ParameterKey: [REQUIRED]
            The room skill parameter key for which to get details. Required.
            

    :rtype: dict
    :return: {
        'RoomSkillParameter': {
            'ParameterKey': 'string',
            'ParameterValue': 'string'
        }
    }
    
    
    """
    pass

def get_skill_group(SkillGroupArn=None):
    """
    Gets skill group details by skill group ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.get_skill_group(
        SkillGroupArn='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group for which to get details. Required.

    :rtype: dict
    :return: {
        'SkillGroup': {
            'SkillGroupArn': 'string',
            'SkillGroupName': 'string',
            'Description': 'string'
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

def list_business_report_schedules(NextToken=None, MaxResults=None):
    """
    Lists the details of the schedules that a user configured.
    See also: AWS API Documentation
    
    
    :example: response = client.list_business_report_schedules(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token used to list the remaining schedules from the previous API call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of schedules listed in the call.

    :rtype: dict
    :return: {
        'BusinessReportSchedules': [
            {
                'ScheduleArn': 'string',
                'ScheduleName': 'string',
                'S3BucketName': 'string',
                'S3KeyPrefix': 'string',
                'Format': 'CSV'|'CSV_ZIP',
                'ContentRange': {
                    'Interval': 'ONE_DAY'|'ONE_WEEK'
                },
                'Recurrence': {
                    'StartDate': 'string'
                },
                'LastBusinessReport': {
                    'Status': 'RUNNING'|'SUCCEEDED'|'FAILED',
                    'FailureCode': 'ACCESS_DENIED'|'NO_SUCH_BUCKET'|'INTERNAL_FAILURE',
                    'S3Location': {
                        'Path': 'string',
                        'BucketName': 'string'
                    },
                    'DeliveryTime': datetime(2015, 1, 1),
                    'DownloadUrl': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_conference_providers(NextToken=None, MaxResults=None):
    """
    Lists conference providers under a specific AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_conference_providers(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The tokens used for pagination.

    :type MaxResults: integer
    :param MaxResults: The maximum number of conference providers to be returned, per paginated calls.

    :rtype: dict
    :return: {
        'ConferenceProviders': [
            {
                'Arn': 'string',
                'Name': 'string',
                'Type': 'CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'|'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
                'IPDialIn': {
                    'Endpoint': 'string',
                    'CommsProtocol': 'SIP'|'SIPS'|'H323'
                },
                'PSTNDialIn': {
                    'CountryCode': 'string',
                    'PhoneNumber': 'string',
                    'OneClickIdDelay': 'string',
                    'OneClickPinDelay': 'string'
                },
                'MeetingSetting': {
                    'RequirePin': 'YES'|'NO'|'OPTIONAL'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_device_events(DeviceArn=None, EventType=None, NextToken=None, MaxResults=None):
    """
    Lists the device event history, including device connection status, for up to 30 days.
    See also: AWS API Documentation
    
    
    :example: response = client.list_device_events(
        DeviceArn='string',
        EventType='CONNECTION_STATUS'|'DEVICE_STATUS',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: [REQUIRED]
            The ARN of a device.
            

    :type EventType: string
    :param EventType: The event type to filter device events. If EventType isn't specified, this returns a list of all device events in reverse chronological order. If EventType is specified, this returns a list of device events for that EventType in reverse chronological order.

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response only includes results beyond the token, up to the value specified by MaxResults. When the end of results is reached, the response has a value of null.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. The default value is 50. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :rtype: dict
    :return: {
        'DeviceEvents': [
            {
                'Type': 'CONNECTION_STATUS'|'DEVICE_STATUS',
                'Value': 'string',
                'Timestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_skills(SkillGroupArn=None, EnablementType=None, SkillType=None, NextToken=None, MaxResults=None):
    """
    Lists all enabled skills in a specific skill group.
    See also: AWS API Documentation
    
    
    :example: response = client.list_skills(
        SkillGroupArn='string',
        EnablementType='ENABLED'|'PENDING',
        SkillType='PUBLIC'|'PRIVATE'|'ALL',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group for which to list enabled skills.

    :type EnablementType: string
    :param EnablementType: Whether the skill is enabled under the user's account, or if it requires linking to be used.

    :type SkillType: string
    :param SkillType: Whether the skill is publicly available or is a private skill.

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :rtype: dict
    :return: {
        'SkillSummaries': [
            {
                'SkillId': 'string',
                'SkillName': 'string',
                'SupportsLinking': True|False,
                'EnablementType': 'ENABLED'|'PENDING',
                'SkillType': 'PUBLIC'|'PRIVATE'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_skills_store_categories(NextToken=None, MaxResults=None):
    """
    Lists all categories in the Alexa skill store.
    See also: AWS API Documentation
    
    
    :example: response = client.list_skills_store_categories(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The tokens used for pagination.

    :type MaxResults: integer
    :param MaxResults: The maximum number of categories returned, per paginated calls.

    :rtype: dict
    :return: {
        'CategoryList': [
            {
                'CategoryId': 123,
                'CategoryName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_skills_store_skills_by_category(CategoryId=None, NextToken=None, MaxResults=None):
    """
    Lists all skills in the Alexa skill store by category.
    See also: AWS API Documentation
    
    
    :example: response = client.list_skills_store_skills_by_category(
        CategoryId=123,
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CategoryId: integer
    :param CategoryId: [REQUIRED]
            The category ID for which the skills are being retrieved from the skill store.
            

    :type NextToken: string
    :param NextToken: The tokens used for pagination.

    :type MaxResults: integer
    :param MaxResults: The maximum number of skills returned per paginated calls.

    :rtype: dict
    :return: {
        'SkillsStoreSkills': [
            {
                'SkillId': 'string',
                'SkillName': 'string',
                'ShortDescription': 'string',
                'IconUrl': 'string',
                'SampleUtterances': [
                    'string',
                ],
                'SkillDetails': {
                    'ProductDescription': 'string',
                    'InvocationPhrase': 'string',
                    'ReleaseDate': 'string',
                    'EndUserLicenseAgreement': 'string',
                    'GenericKeywords': [
                        'string',
                    ],
                    'BulletPoints': [
                        'string',
                    ],
                    'NewInThisVersionBulletPoints': [
                        'string',
                    ],
                    'SkillTypes': [
                        'string',
                    ],
                    'Reviews': {
                        'string': 'string'
                    },
                    'DeveloperInfo': {
                        'DeveloperName': 'string',
                        'PrivacyPolicy': 'string',
                        'Email': 'string',
                        'Url': 'string'
                    }
                },
                'SupportsLinking': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_smart_home_appliances(RoomArn=None, MaxResults=None, NextToken=None):
    """
    Lists all of the smart home appliances associated with a room.
    See also: AWS API Documentation
    
    
    :example: response = client.list_smart_home_appliances(
        RoomArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: [REQUIRED]
            The room that the appliances are associated with.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of appliances to be returned, per paginated calls.

    :type NextToken: string
    :param NextToken: The tokens used for pagination.

    :rtype: dict
    :return: {
        'SmartHomeAppliances': [
            {
                'FriendlyName': 'string',
                'Description': 'string',
                'ManufacturerName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_tags(Arn=None, NextToken=None, MaxResults=None):
    """
    Lists all tags for the specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags(
        Arn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            The ARN of the specified resource for which to list tags.
            

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def put_conference_preference(ConferencePreference=None):
    """
    Sets the conference preferences on a specific conference provider at the account level.
    See also: AWS API Documentation
    
    
    :example: response = client.put_conference_preference(
        ConferencePreference={
            'DefaultConferenceProviderArn': 'string'
        }
    )
    
    
    :type ConferencePreference: dict
    :param ConferencePreference: [REQUIRED]
            The conference preference of a specific conference provider.
            DefaultConferenceProviderArn (string) --The ARN of the default conference provider.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def put_room_skill_parameter(RoomArn=None, SkillId=None, RoomSkillParameter=None):
    """
    Updates room skill parameter details by room, skill, and parameter key ID. Not all skills have a room skill parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.put_room_skill_parameter(
        RoomArn='string',
        SkillId='string',
        RoomSkillParameter={
            'ParameterKey': 'string',
            'ParameterValue': 'string'
        }
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room associated with the room skill parameter. Required.

    :type SkillId: string
    :param SkillId: [REQUIRED]
            The ARN of the skill associated with the room skill parameter. Required.
            

    :type RoomSkillParameter: dict
    :param RoomSkillParameter: [REQUIRED]
            The updated room skill parameter. Required.
            ParameterKey (string) -- [REQUIRED]The parameter key of a room skill parameter. ParameterKey is an enumerated type that only takes  DEFAULT  or  SCOPE  as valid values.
            ParameterValue (string) -- [REQUIRED]The parameter value of a room skill parameter.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_skill_authorization(AuthorizationResult=None, SkillId=None, RoomArn=None):
    """
    Links a user's account to a third-party skill provider. If this API operation is called by an assumed IAM role, the skill being linked must be a private skill. Also, the skill must be owned by the AWS account that assumed the IAM role.
    See also: AWS API Documentation
    
    
    :example: response = client.put_skill_authorization(
        AuthorizationResult={
            'string': 'string'
        },
        SkillId='string',
        RoomArn='string'
    )
    
    
    :type AuthorizationResult: dict
    :param AuthorizationResult: [REQUIRED]
            The authorization result specific to OAUTH code grant output. 'Code  must be populated in the AuthorizationResult map to establish the authorization.
            (string) --
            (string) --
            

    :type SkillId: string
    :param SkillId: [REQUIRED]
            The unique identifier of a skill.
            

    :type RoomArn: string
    :param RoomArn: The room that the skill is authorized for.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def register_avs_device(ClientId=None, UserCode=None, ProductId=None, DeviceSerialNumber=None, AmazonId=None):
    """
    Registers an Alexa-enabled device built by an Original Equipment Manufacturer (OEM) using Alexa Voice Service (AVS).
    See also: AWS API Documentation
    
    
    :example: response = client.register_avs_device(
        ClientId='string',
        UserCode='string',
        ProductId='string',
        DeviceSerialNumber='string',
        AmazonId='string'
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]
            The client ID of the OEM used for code-based linking authorization on an AVS device.
            

    :type UserCode: string
    :param UserCode: [REQUIRED]
            The code that is obtained after your AVS device has made a POST request to LWA as a part of the Device Authorization Request component of the OAuth code-based linking specification.
            

    :type ProductId: string
    :param ProductId: [REQUIRED]
            The product ID used to identify your AVS device during authorization.
            

    :type DeviceSerialNumber: string
    :param DeviceSerialNumber: [REQUIRED]
            The key generated by the OEM that uniquely identifies a specified instance of your AVS device.
            

    :type AmazonId: string
    :param AmazonId: [REQUIRED]
            The device type ID for your AVS device generated by Amazon when the OEM creates a new product on Amazon's Developer Console.
            

    :rtype: dict
    :return: {
        'DeviceArn': 'string'
    }
    
    
    """
    pass

def reject_skill(SkillId=None):
    """
    Disassociates a skill from the organization under a user's AWS account. If the skill is a private skill, it moves to an AcceptStatus of PENDING. Any private or public skill that is rejected can be added later by calling the ApproveSkill API.
    See also: AWS API Documentation
    
    
    :example: response = client.reject_skill(
        SkillId='string'
    )
    
    
    :type SkillId: string
    :param SkillId: [REQUIRED]
            The unique identifier of the skill.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def resolve_room(UserId=None, SkillId=None):
    """
    Determines the details for the room from which a skill request was invoked. This operation is used by skill developers.
    See also: AWS API Documentation
    
    
    :example: response = client.resolve_room(
        UserId='string',
        SkillId='string'
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]
            The ARN of the user. Required.
            

    :type SkillId: string
    :param SkillId: [REQUIRED]
            The ARN of the skill that was requested. Required.
            

    :rtype: dict
    :return: {
        'RoomArn': 'string',
        'RoomName': 'string',
        'RoomSkillParameters': [
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string'
            },
        ]
    }
    
    
    """
    pass

def revoke_invitation(UserArn=None, EnrollmentId=None):
    """
    Revokes an invitation and invalidates the enrollment URL.
    See also: AWS API Documentation
    
    
    :example: response = client.revoke_invitation(
        UserArn='string',
        EnrollmentId='string'
    )
    
    
    :type UserArn: string
    :param UserArn: The ARN of the user for whom to revoke an enrollment invitation. Required.

    :type EnrollmentId: string
    :param EnrollmentId: The ARN of the enrollment invitation to revoke. Required.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def search_address_books(Filters=None, SortCriteria=None, NextToken=None, MaxResults=None):
    """
    Searches address books and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_address_books(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: The filters to use to list a specified set of address books. The supported filter key is AddressBookName.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
            Key (string) -- [REQUIRED]The key of a filter.
            Values (list) -- [REQUIRED]The values of a filter.
            (string) --
            
            

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of address books. The supported sort key is AddressBookName.
            (dict) --An object representing a sort criteria.
            Key (string) -- [REQUIRED]The sort key of a sort object.
            Value (string) -- [REQUIRED]The sort value of a sort object.
            
            

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response only includes results beyond the token, up to the value specified by MaxResults.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :rtype: dict
    :return: {
        'AddressBooks': [
            {
                'AddressBookArn': 'string',
                'Name': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_contacts(Filters=None, SortCriteria=None, NextToken=None, MaxResults=None):
    """
    Searches contacts and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_contacts(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: The filters to use to list a specified set of address books. The supported filter keys are DisplayName, FirstName, LastName, and AddressBookArns.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
            Key (string) -- [REQUIRED]The key of a filter.
            Values (list) -- [REQUIRED]The values of a filter.
            (string) --
            
            

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of contacts. The supported sort keys are DisplayName, FirstName, and LastName.
            (dict) --An object representing a sort criteria.
            Key (string) -- [REQUIRED]The sort key of a sort object.
            Value (string) -- [REQUIRED]The sort value of a sort object.
            
            

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response only includes results beyond the token, up to the value specified by MaxResults.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :rtype: dict
    :return: {
        'Contacts': [
            {
                'ContactArn': 'string',
                'DisplayName': 'string',
                'FirstName': 'string',
                'LastName': 'string',
                'PhoneNumber': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_devices(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches devices and lists the ones that meet a set of filter criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_devices(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :type Filters: list
    :param Filters: The filters to use to list a specified set of devices. Supported filter keys are DeviceName, DeviceStatus, DeviceStatusDetailCode, RoomName, DeviceType, DeviceSerialNumber, UnassociatedOnly, and ConnectionStatus (ONLINE and OFFLINE).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
            Key (string) -- [REQUIRED]The key of a filter.
            Values (list) -- [REQUIRED]The values of a filter.
            (string) --
            
            

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of devices. Supported sort keys are DeviceName, DeviceStatus, RoomName, DeviceType, DeviceSerialNumber, and ConnectionStatus.
            (dict) --An object representing a sort criteria.
            Key (string) -- [REQUIRED]The sort key of a sort object.
            Value (string) -- [REQUIRED]The sort value of a sort object.
            
            

    :rtype: dict
    :return: {
        'Devices': [
            {
                'DeviceArn': 'string',
                'DeviceSerialNumber': 'string',
                'DeviceType': 'string',
                'DeviceName': 'string',
                'SoftwareVersion': 'string',
                'MacAddress': 'string',
                'DeviceStatus': 'READY'|'PENDING'|'WAS_OFFLINE'|'DEREGISTERED',
                'RoomArn': 'string',
                'RoomName': 'string',
                'DeviceStatusInfo': {
                    'DeviceStatusDetails': [
                        {
                            'Code': 'DEVICE_SOFTWARE_UPDATE_NEEDED'|'DEVICE_WAS_OFFLINE'
                        },
                    ],
                    'ConnectionStatus': 'ONLINE'|'OFFLINE'
                }
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_profiles(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches room profiles and lists the ones that meet a set of filter criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_profiles(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :type Filters: list
    :param Filters: The filters to use to list a specified set of room profiles. Supported filter keys are ProfileName and Address. Required.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
            Key (string) -- [REQUIRED]The key of a filter.
            Values (list) -- [REQUIRED]The values of a filter.
            (string) --
            
            

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of room profiles. Supported sort keys are ProfileName and Address.
            (dict) --An object representing a sort criteria.
            Key (string) -- [REQUIRED]The sort key of a sort object.
            Value (string) -- [REQUIRED]The sort value of a sort object.
            
            

    :rtype: dict
    :return: {
        'Profiles': [
            {
                'ProfileArn': 'string',
                'ProfileName': 'string',
                'IsDefault': True|False,
                'Address': 'string',
                'Timezone': 'string',
                'DistanceUnit': 'METRIC'|'IMPERIAL',
                'TemperatureUnit': 'FAHRENHEIT'|'CELSIUS',
                'WakeWord': 'ALEXA'|'AMAZON'|'ECHO'|'COMPUTER'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_rooms(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches rooms and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_rooms(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :type Filters: list
    :param Filters: The filters to use to list a specified set of rooms. The supported filter keys are RoomName and ProfileName.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
            Key (string) -- [REQUIRED]The key of a filter.
            Values (list) -- [REQUIRED]The values of a filter.
            (string) --
            
            

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of rooms. The supported sort keys are RoomName and ProfileName.
            (dict) --An object representing a sort criteria.
            Key (string) -- [REQUIRED]The sort key of a sort object.
            Value (string) -- [REQUIRED]The sort value of a sort object.
            
            

    :rtype: dict
    :return: {
        'Rooms': [
            {
                'RoomArn': 'string',
                'RoomName': 'string',
                'Description': 'string',
                'ProviderCalendarId': 'string',
                'ProfileArn': 'string',
                'ProfileName': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_skill_groups(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches skill groups and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_skill_groups(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults . Required.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.

    :type Filters: list
    :param Filters: The filters to use to list a specified set of skill groups. The supported filter key is SkillGroupName.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
            Key (string) -- [REQUIRED]The key of a filter.
            Values (list) -- [REQUIRED]The values of a filter.
            (string) --
            
            

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the specified set of skill groups. The supported sort key is SkillGroupName.
            (dict) --An object representing a sort criteria.
            Key (string) -- [REQUIRED]The sort key of a sort object.
            Value (string) -- [REQUIRED]The sort value of a sort object.
            
            

    :rtype: dict
    :return: {
        'SkillGroups': [
            {
                'SkillGroupArn': 'string',
                'SkillGroupName': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def search_users(NextToken=None, MaxResults=None, Filters=None, SortCriteria=None):
    """
    Searches users and lists the ones that meet a set of filter and sort criteria.
    See also: AWS API Documentation
    
    
    :example: response = client.search_users(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        SortCriteria=[
            {
                'Key': 'string',
                'Value': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults . Required.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. Required.

    :type Filters: list
    :param Filters: The filters to use for listing a specific set of users. Required. Supported filter keys are UserId, FirstName, LastName, Email, and EnrollmentStatus.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria.
            Key (string) -- [REQUIRED]The key of a filter.
            Values (list) -- [REQUIRED]The values of a filter.
            (string) --
            
            

    :type SortCriteria: list
    :param SortCriteria: The sort order to use in listing the filtered set of users. Required. Supported sort keys are UserId, FirstName, LastName, Email, and EnrollmentStatus.
            (dict) --An object representing a sort criteria.
            Key (string) -- [REQUIRED]The sort key of a sort object.
            Value (string) -- [REQUIRED]The sort value of a sort object.
            
            

    :rtype: dict
    :return: {
        'Users': [
            {
                'UserArn': 'string',
                'FirstName': 'string',
                'LastName': 'string',
                'Email': 'string',
                'EnrollmentStatus': 'INITIALIZED'|'PENDING'|'REGISTERED'|'DISASSOCIATING'|'DEREGISTERING',
                'EnrollmentId': 'string'
            },
        ],
        'NextToken': 'string',
        'TotalCount': 123
    }
    
    
    """
    pass

def send_invitation(UserArn=None):
    """
    Sends an enrollment invitation email with a URL to a user. The URL is valid for 72 hours or until you call this operation again, whichever comes first.
    See also: AWS API Documentation
    
    
    :example: response = client.send_invitation(
        UserArn='string'
    )
    
    
    :type UserArn: string
    :param UserArn: The ARN of the user to whom to send an invitation. Required.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def start_device_sync(RoomArn=None, DeviceArn=None, Features=None):
    """
    Resets a device and its account to the known default settings, by clearing all information and settings set by previous users.
    See also: AWS API Documentation
    
    
    :example: response = client.start_device_sync(
        RoomArn='string',
        DeviceArn='string',
        Features=[
            'BLUETOOTH'|'VOLUME'|'NOTIFICATIONS'|'LISTS'|'SKILLS'|'ALL',
        ]
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room with which the device to sync is associated. Required.

    :type DeviceArn: string
    :param DeviceArn: The ARN of the device to sync. Required.

    :type Features: list
    :param Features: [REQUIRED]
            Request structure to start the device sync. Required.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_smart_home_appliance_discovery(RoomArn=None):
    """
    Initiates the discovery of any smart home appliances associated with the room.
    See also: AWS API Documentation
    
    
    :example: response = client.start_smart_home_appliance_discovery(
        RoomArn='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: [REQUIRED]
            The room where smart home appliance discovery was initiated.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def tag_resource(Arn=None, Tags=None):
    """
    Adds metadata tags to a specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        Arn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            The ARN of the resource to which to add metadata tags. Required.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags to be added to the specified resource. Do not provide system tags. Required.
            (dict) --A key-value pair that can be associated with a resource.
            Key (string) -- [REQUIRED]The key of a tag. Tag keys are case-sensitive.
            Value (string) -- [REQUIRED]The value of a tag. Tag values are case-sensitive and can be null.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(Arn=None, TagKeys=None):
    """
    Removes metadata tags from a specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        Arn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            The ARN of the resource from which to remove metadata tags. Required.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tags to be removed from the specified resource. Do not provide system tags. Required.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_address_book(AddressBookArn=None, Name=None, Description=None):
    """
    Updates address book details by the address book ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.update_address_book(
        AddressBookArn='string',
        Name='string',
        Description='string'
    )
    
    
    :type AddressBookArn: string
    :param AddressBookArn: [REQUIRED]
            The ARN of the room to update.
            

    :type Name: string
    :param Name: The updated name of the room.

    :type Description: string
    :param Description: The updated description of the room.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_business_report_schedule(ScheduleArn=None, S3BucketName=None, S3KeyPrefix=None, Format=None, ScheduleName=None, Recurrence=None):
    """
    Updates the configuration of the report delivery schedule with the specified schedule ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.update_business_report_schedule(
        ScheduleArn='string',
        S3BucketName='string',
        S3KeyPrefix='string',
        Format='CSV'|'CSV_ZIP',
        ScheduleName='string',
        Recurrence={
            'StartDate': 'string'
        }
    )
    
    
    :type ScheduleArn: string
    :param ScheduleArn: [REQUIRED]
            The ARN of the business report schedule.
            

    :type S3BucketName: string
    :param S3BucketName: The S3 location of the output reports.

    :type S3KeyPrefix: string
    :param S3KeyPrefix: The S3 key where the report is delivered.

    :type Format: string
    :param Format: The format of the generated report (individual CSV files or zipped files of individual files).

    :type ScheduleName: string
    :param ScheduleName: The name identifier of the schedule.

    :type Recurrence: dict
    :param Recurrence: The recurrence of the reports.
            StartDate (string) --The start date.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_conference_provider(ConferenceProviderArn=None, ConferenceProviderType=None, IPDialIn=None, PSTNDialIn=None, MeetingSetting=None):
    """
    Updates an existing conference provider's settings.
    See also: AWS API Documentation
    
    
    :example: response = client.update_conference_provider(
        ConferenceProviderArn='string',
        ConferenceProviderType='CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'|'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
        IPDialIn={
            'Endpoint': 'string',
            'CommsProtocol': 'SIP'|'SIPS'|'H323'
        },
        PSTNDialIn={
            'CountryCode': 'string',
            'PhoneNumber': 'string',
            'OneClickIdDelay': 'string',
            'OneClickPinDelay': 'string'
        },
        MeetingSetting={
            'RequirePin': 'YES'|'NO'|'OPTIONAL'
        }
    )
    
    
    :type ConferenceProviderArn: string
    :param ConferenceProviderArn: [REQUIRED]
            The ARN of the conference provider.
            

    :type ConferenceProviderType: string
    :param ConferenceProviderType: [REQUIRED]
            The type of the conference provider.
            

    :type IPDialIn: dict
    :param IPDialIn: The IP endpoint and protocol for calling.
            Endpoint (string) -- [REQUIRED]The IP address.
            CommsProtocol (string) -- [REQUIRED]The protocol, including SIP, SIPS, and H323.
            

    :type PSTNDialIn: dict
    :param PSTNDialIn: The information for PSTN conferencing.
            CountryCode (string) -- [REQUIRED]The zip code.
            PhoneNumber (string) -- [REQUIRED]The phone number to call to join the conference.
            OneClickIdDelay (string) -- [REQUIRED]The delay duration before Alexa enters the conference ID with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
            OneClickPinDelay (string) -- [REQUIRED]The delay duration before Alexa enters the conference pin with dual-tone multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone, which is how we send data over the telephone network.
            

    :type MeetingSetting: dict
    :param MeetingSetting: [REQUIRED]
            The meeting settings for the conference provider.
            RequirePin (string) -- [REQUIRED]The values that indicate whether the pin is always required.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_contact(ContactArn=None, DisplayName=None, FirstName=None, LastName=None, PhoneNumber=None):
    """
    Updates the contact details by the contact ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.update_contact(
        ContactArn='string',
        DisplayName='string',
        FirstName='string',
        LastName='string',
        PhoneNumber='string'
    )
    
    
    :type ContactArn: string
    :param ContactArn: [REQUIRED]
            The ARN of the contact to update.
            

    :type DisplayName: string
    :param DisplayName: The updated display name of the contact.

    :type FirstName: string
    :param FirstName: The updated first name of the contact.

    :type LastName: string
    :param LastName: The updated last name of the contact.

    :type PhoneNumber: string
    :param PhoneNumber: The updated phone number of the contact.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_device(DeviceArn=None, DeviceName=None):
    """
    Updates the device name by device ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.update_device(
        DeviceArn='string',
        DeviceName='string'
    )
    
    
    :type DeviceArn: string
    :param DeviceArn: The ARN of the device to update. Required.

    :type DeviceName: string
    :param DeviceName: The updated device name. Required.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_profile(ProfileArn=None, ProfileName=None, IsDefault=None, Timezone=None, Address=None, DistanceUnit=None, TemperatureUnit=None, WakeWord=None, SetupModeDisabled=None, MaxVolumeLimit=None, PSTNEnabled=None):
    """
    Updates an existing room profile by room profile ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.update_profile(
        ProfileArn='string',
        ProfileName='string',
        IsDefault=True|False,
        Timezone='string',
        Address='string',
        DistanceUnit='METRIC'|'IMPERIAL',
        TemperatureUnit='FAHRENHEIT'|'CELSIUS',
        WakeWord='ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
        SetupModeDisabled=True|False,
        MaxVolumeLimit=123,
        PSTNEnabled=True|False
    )
    
    
    :type ProfileArn: string
    :param ProfileArn: The ARN of the room profile to update. Required.

    :type ProfileName: string
    :param ProfileName: The updated name for the room profile.

    :type IsDefault: boolean
    :param IsDefault: Sets the profile as default if selected. If this is missing, no update is done to the default status.

    :type Timezone: string
    :param Timezone: The updated timezone for the room profile.

    :type Address: string
    :param Address: The updated address for the room profile.

    :type DistanceUnit: string
    :param DistanceUnit: The updated distance unit for the room profile.

    :type TemperatureUnit: string
    :param TemperatureUnit: The updated temperature unit for the room profile.

    :type WakeWord: string
    :param WakeWord: The updated wake word for the room profile.

    :type SetupModeDisabled: boolean
    :param SetupModeDisabled: Whether the setup mode of the profile is enabled.

    :type MaxVolumeLimit: integer
    :param MaxVolumeLimit: The updated maximum volume limit for the room profile.

    :type PSTNEnabled: boolean
    :param PSTNEnabled: Whether the PSTN setting of the room profile is enabled.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_room(RoomArn=None, RoomName=None, Description=None, ProviderCalendarId=None, ProfileArn=None):
    """
    Updates room details by room ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.update_room(
        RoomArn='string',
        RoomName='string',
        Description='string',
        ProviderCalendarId='string',
        ProfileArn='string'
    )
    
    
    :type RoomArn: string
    :param RoomArn: The ARN of the room to update.

    :type RoomName: string
    :param RoomName: The updated name for the room.

    :type Description: string
    :param Description: The updated description for the room.

    :type ProviderCalendarId: string
    :param ProviderCalendarId: The updated provider calendar ARN for the room.

    :type ProfileArn: string
    :param ProfileArn: The updated profile ARN for the room.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_skill_group(SkillGroupArn=None, SkillGroupName=None, Description=None):
    """
    Updates skill group details by skill group ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.update_skill_group(
        SkillGroupArn='string',
        SkillGroupName='string',
        Description='string'
    )
    
    
    :type SkillGroupArn: string
    :param SkillGroupArn: The ARN of the skill group to update.

    :type SkillGroupName: string
    :param SkillGroupName: The updated name for the skill group.

    :type Description: string
    :param Description: The updated description for the skill group.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

