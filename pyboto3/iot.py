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

def accept_certificate_transfer(certificateId=None, setAsActive=None):
    """
    Accepts a pending certificate transfer. The default state of the certificate is INACTIVE.
    To check for pending certificate transfers, call  ListCertificates to enumerate your certificates.
    See also: AWS API Documentation
    
    
    :example: response = client.accept_certificate_transfer(
        certificateId='string',
        setAsActive=True|False
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
            

    :type setAsActive: boolean
    :param setAsActive: Specifies whether the certificate is active.

    """
    pass

def add_thing_to_billing_group(billingGroupName=None, billingGroupArn=None, thingName=None, thingArn=None):
    """
    Adds a thing to a billing group.
    See also: AWS API Documentation
    
    
    :example: response = client.add_thing_to_billing_group(
        billingGroupName='string',
        billingGroupArn='string',
        thingName='string',
        thingArn='string'
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: The name of the billing group.

    :type billingGroupArn: string
    :param billingGroupArn: The ARN of the billing group.

    :type thingName: string
    :param thingName: The name of the thing to be added to the billing group.

    :type thingArn: string
    :param thingArn: The ARN of the thing to be added to the billing group.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def add_thing_to_thing_group(thingGroupName=None, thingGroupArn=None, thingName=None, thingArn=None, overrideDynamicGroups=None):
    """
    Adds a thing to a thing group.
    See also: AWS API Documentation
    
    
    :example: response = client.add_thing_to_thing_group(
        thingGroupName='string',
        thingGroupArn='string',
        thingName='string',
        thingArn='string',
        overrideDynamicGroups=True|False
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: The name of the group to which you are adding a thing.

    :type thingGroupArn: string
    :param thingGroupArn: The ARN of the group to which you are adding a thing.

    :type thingName: string
    :param thingName: The name of the thing to add to a group.

    :type thingArn: string
    :param thingArn: The ARN of the thing to add to a group.

    :type overrideDynamicGroups: boolean
    :param overrideDynamicGroups: Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_targets_with_job(targets=None, jobId=None, comment=None):
    """
    Associates a group with a continuous job. The following criteria must be met:
    See also: AWS API Documentation
    
    
    :example: response = client.associate_targets_with_job(
        targets=[
            'string',
        ],
        jobId='string',
        comment='string'
    )
    
    
    :type targets: list
    :param targets: [REQUIRED]
            A list of thing group ARNs that define the targets of the job.
            (string) --
            

    :type jobId: string
    :param jobId: [REQUIRED]
            The unique identifier you assigned to this job when it was created.
            

    :type comment: string
    :param comment: An optional comment string describing why the job was associated with the targets.

    :rtype: dict
    :return: {
        'jobArn': 'string',
        'jobId': 'string',
        'description': 'string'
    }
    
    
    :returns: 
    targets (list) -- [REQUIRED]
    A list of thing group ARNs that define the targets of the job.
    
    (string) --
    
    
    jobId (string) -- [REQUIRED]
    The unique identifier you assigned to this job when it was created.
    
    comment (string) -- An optional comment string describing why the job was associated with the targets.
    
    """
    pass

def attach_policy(policyName=None, target=None):
    """
    Attaches a policy to the specified target.
    See also: AWS API Documentation
    
    
    :example: response = client.attach_policy(
        policyName='string',
        target='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy to attach.
            

    :type target: string
    :param target: [REQUIRED]
            The identity to which the policy is attached.
            

    """
    pass

def attach_principal_policy(policyName=None, principal=None):
    """
    Attaches the specified policy to the specified principal (certificate or other credential).
    See also: AWS API Documentation
    
    
    :example: response = client.attach_principal_policy(
        policyName='string',
        principal='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type principal: string
    :param principal: [REQUIRED]
            The principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.
            

    """
    pass

def attach_security_profile(securityProfileName=None, securityProfileTargetArn=None):
    """
    Associates a Device Defender security profile with a thing group or with this account. Each thing group or account can have up to five security profiles associated with it.
    See also: AWS API Documentation
    
    
    :example: response = client.attach_security_profile(
        securityProfileName='string',
        securityProfileTargetArn='string'
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]
            The security profile that is attached.
            

    :type securityProfileTargetArn: string
    :param securityProfileTargetArn: [REQUIRED]
            The ARN of the target (thing group) to which the security profile is attached.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def attach_thing_principal(thingName=None, principal=None):
    """
    Attaches the specified principal to the specified thing.
    See also: AWS API Documentation
    
    
    :example: response = client.attach_thing_principal(
        thingName='string',
        principal='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing.
            

    :type principal: string
    :param principal: [REQUIRED]
            The principal, such as a certificate or other credential.
            

    :rtype: dict
    :return: {}
    
    
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

def cancel_audit_task(taskId=None):
    """
    Cancels an audit that is in progress. The audit can be either scheduled or on-demand. If the audit is not in progress, an "InvalidRequestException" occurs.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_audit_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]
            The ID of the audit you want to cancel. You can only cancel an audit that is 'IN_PROGRESS'.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def cancel_certificate_transfer(certificateId=None):
    """
    Cancels a pending transfer for the specified certificate.
    After a certificate transfer is cancelled, the status of the certificate changes from PENDING_TRANSFER to INACTIVE.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_certificate_transfer(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
            

    """
    pass

def cancel_job(jobId=None, reasonCode=None, comment=None, force=None):
    """
    Cancels a job.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_job(
        jobId='string',
        reasonCode='string',
        comment='string',
        force=True|False
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique identifier you assigned to this job when it was created.
            

    :type reasonCode: string
    :param reasonCode: (Optional)A reason code string that explains why the job was canceled.

    :type comment: string
    :param comment: An optional comment string describing why the job was canceled.

    :type force: boolean
    :param force: (Optional) If true job executions with status 'IN_PROGRESS' and 'QUEUED' are canceled, otherwise only job executions with status 'QUEUED' are canceled. The default is false .
            Canceling a job which is 'IN_PROGRESS', will cause a device which is executing the job to be unable to update the job execution status. Use caution and ensure that each device executing a job which is canceled is able to recover to a valid state.
            

    :rtype: dict
    :return: {
        'jobArn': 'string',
        'jobId': 'string',
        'description': 'string'
    }
    
    
    """
    pass

def cancel_job_execution(jobId=None, thingName=None, force=None, expectedVersion=None, statusDetails=None):
    """
    Cancels the execution of a job for a given thing.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_job_execution(
        jobId='string',
        thingName='string',
        force=True|False,
        expectedVersion=123,
        statusDetails={
            'string': 'string'
        }
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The ID of the job to be canceled.
            

    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing whose execution of the job will be canceled.
            

    :type force: boolean
    :param force: (Optional) If true the job execution will be canceled if it has status IN_PROGRESS or QUEUED, otherwise the job execution will be canceled only if it has status QUEUED. If you attempt to cancel a job execution that is IN_PROGRESS, and you do not set force to true , then an InvalidStateTransitionException will be thrown. The default is false .
            Canceling a job execution which is 'IN_PROGRESS', will cause the device to be unable to update the job execution status. Use caution and ensure that the device is able to recover to a valid state.
            

    :type expectedVersion: integer
    :param expectedVersion: (Optional) The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)

    :type statusDetails: dict
    :param statusDetails: A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged. You can specify at most 10 name/value pairs.
            (string) --
            (string) --
            

    """
    pass

def clear_default_authorizer():
    """
    Clears the default authorizer.
    See also: AWS API Documentation
    
    
    :example: response = client.clear_default_authorizer()
    
    
    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_authorizer(authorizerName=None, authorizerFunctionArn=None, tokenKeyName=None, tokenSigningPublicKeys=None, status=None):
    """
    Creates an authorizer.
    See also: AWS API Documentation
    
    
    :example: response = client.create_authorizer(
        authorizerName='string',
        authorizerFunctionArn='string',
        tokenKeyName='string',
        tokenSigningPublicKeys={
            'string': 'string'
        },
        status='ACTIVE'|'INACTIVE'
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]
            The authorizer name.
            

    :type authorizerFunctionArn: string
    :param authorizerFunctionArn: [REQUIRED]
            The ARN of the authorizer's Lambda function.
            

    :type tokenKeyName: string
    :param tokenKeyName: [REQUIRED]
            The name of the token key used to extract the token from the HTTP headers.
            

    :type tokenSigningPublicKeys: dict
    :param tokenSigningPublicKeys: [REQUIRED]
            The public keys used to verify the digital signature returned by your custom authentication service.
            (string) --
            (string) --
            

    :type status: string
    :param status: The status of the create authorizer request.

    :rtype: dict
    :return: {
        'authorizerName': 'string',
        'authorizerArn': 'string'
    }
    
    
    """
    pass

def create_billing_group(billingGroupName=None, billingGroupProperties=None, tags=None):
    """
    Creates a billing group.
    See also: AWS API Documentation
    
    
    :example: response = client.create_billing_group(
        billingGroupName='string',
        billingGroupProperties={
            'billingGroupDescription': 'string'
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: [REQUIRED]
            The name you wish to give to the billing group.
            

    :type billingGroupProperties: dict
    :param billingGroupProperties: The properties of the billing group.
            billingGroupDescription (string) --The description of the billing group.
            

    :type tags: list
    :param tags: Metadata which can be used to manage the billing group.
            (dict) --A set of key/value pairs that are used to manage the resource.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            

    :rtype: dict
    :return: {
        'billingGroupName': 'string',
        'billingGroupArn': 'string',
        'billingGroupId': 'string'
    }
    
    
    """
    pass

def create_certificate_from_csr(certificateSigningRequest=None, setAsActive=None):
    """
    Creates an X.509 certificate using the specified certificate signing request.
    You can create multiple certificates in a batch by creating a directory, copying multiple .csr files into that directory, and then specifying that directory on the command line. The following commands show how to create a batch of certificates given a batch of CSRs.
    Assuming a set of CSRs are located inside of the directory my-csr-directory:
    On Linux and OS X, the command is:
    $ ls my-csr-directory/ | xargs -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}
    This command lists all of the CSRs in my-csr-directory and pipes each CSR file name to the aws iot create-certificate-from-csr AWS CLI command to create a certificate for the corresponding CSR.
    The aws iot create-certificate-from-csr part of the command can also be run in parallel to speed up the certificate creation process:
    $ ls my-csr-directory/ | xargs -P 10 -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}
    On Windows PowerShell, the command to create certificates for all CSRs in my-csr-directory is:
    > ls -Name my-csr-directory | %{aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/$_}
    On a Windows command prompt, the command to create certificates for all CSRs in my-csr-directory is:
    > forfiles /p my-csr-directory /c "cmd /c aws iot create-certificate-from-csr --certificate-signing-request file://@path"
    See also: AWS API Documentation
    
    
    :example: response = client.create_certificate_from_csr(
        certificateSigningRequest='string',
        setAsActive=True|False
    )
    
    
    :type certificateSigningRequest: string
    :param certificateSigningRequest: [REQUIRED]
            The certificate signing request (CSR).
            

    :type setAsActive: boolean
    :param setAsActive: Specifies whether the certificate is active.

    :rtype: dict
    :return: {
        'certificateArn': 'string',
        'certificateId': 'string',
        'certificatePem': 'string'
    }
    
    
    """
    pass

def create_dynamic_thing_group(thingGroupName=None, thingGroupProperties=None, indexName=None, queryString=None, queryVersion=None, tags=None):
    """
    Creates a dynamic thing group.
    See also: AWS API Documentation
    
    
    :example: response = client.create_dynamic_thing_group(
        thingGroupName='string',
        thingGroupProperties={
            'thingGroupDescription': 'string',
            'attributePayload': {
                'attributes': {
                    'string': 'string'
                },
                'merge': True|False
            }
        },
        indexName='string',
        queryString='string',
        queryVersion='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]
            The dynamic thing group name to create.
            

    :type thingGroupProperties: dict
    :param thingGroupProperties: The dynamic thing group properties.
            thingGroupDescription (string) --The thing group description.
            attributePayload (dict) --The thing group attributes in JSON format.
            attributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:
            {\'attributes\':{\'string1\':\'string2\'}}
            (string) --
            (string) --
            
            merge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.
            To remove an attribute, call UpdateThing with an empty attribute value.
            Note
            The merge attribute is only valid when calling UpdateThing .
            
            

    :type indexName: string
    :param indexName: The dynamic thing group index name.
            Note
            Currently one index is supported: 'AWS_Things'.
            

    :type queryString: string
    :param queryString: [REQUIRED]
            The dynamic thing group search query string.
            See Query Syntax for information about query string syntax.
            

    :type queryVersion: string
    :param queryVersion: The dynamic thing group query version.
            Note
            Currently one query version is supported: '2017-09-30'. If not specified, the query version defaults to this value.
            

    :type tags: list
    :param tags: Metadata which can be used to manage the dynamic thing group.
            (dict) --A set of key/value pairs that are used to manage the resource.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            

    :rtype: dict
    :return: {
        'thingGroupName': 'string',
        'thingGroupArn': 'string',
        'thingGroupId': 'string',
        'indexName': 'string',
        'queryString': 'string',
        'queryVersion': 'string'
    }
    
    
    """
    pass

def create_job(jobId=None, targets=None, documentSource=None, document=None, description=None, presignedUrlConfig=None, targetSelection=None, jobExecutionsRolloutConfig=None, abortConfig=None, timeoutConfig=None, tags=None):
    """
    Creates a job.
    See also: AWS API Documentation
    
    
    :example: response = client.create_job(
        jobId='string',
        targets=[
            'string',
        ],
        documentSource='string',
        document='string',
        description='string',
        presignedUrlConfig={
            'roleArn': 'string',
            'expiresInSec': 123
        },
        targetSelection='CONTINUOUS'|'SNAPSHOT',
        jobExecutionsRolloutConfig={
            'maximumPerMinute': 123,
            'exponentialRate': {
                'baseRatePerMinute': 123,
                'incrementFactor': 123.0,
                'rateIncreaseCriteria': {
                    'numberOfNotifiedThings': 123,
                    'numberOfSucceededThings': 123
                }
            }
        },
        abortConfig={
            'criteriaList': [
                {
                    'failureType': 'FAILED'|'REJECTED'|'TIMED_OUT'|'ALL',
                    'action': 'CANCEL',
                    'thresholdPercentage': 123.0,
                    'minNumberOfExecutedThings': 123
                },
            ]
        },
        timeoutConfig={
            'inProgressTimeoutInMinutes': 123
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            A job identifier which must be unique for your AWS account. We recommend using a UUID. Alpha-numeric characters, '-' and '_' are valid for use here.
            

    :type targets: list
    :param targets: [REQUIRED]
            A list of things and thing groups to which the job should be sent.
            (string) --
            

    :type documentSource: string
    :param documentSource: An S3 link to the job document.

    :type document: string
    :param document: The job document.
            Note
            If the job document resides in an S3 bucket, you must use a placeholder link when specifying the document.
            The placeholder link is of the following form:
            ${aws:iot:s3-presigned-url:https://s3.amazonaws.com/*bucket* /*key* }
            where bucket is your bucket name and key is the object in the bucket to which you are linking.
            

    :type description: string
    :param description: A short text description of the job.

    :type presignedUrlConfig: dict
    :param presignedUrlConfig: Configuration information for pre-signed S3 URLs.
            roleArn (string) --The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.
            expiresInSec (integer) --How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.
            

    :type targetSelection: string
    :param targetSelection: Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.

    :type jobExecutionsRolloutConfig: dict
    :param jobExecutionsRolloutConfig: Allows you to create a staged rollout of the job.
            maximumPerMinute (integer) --The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.
            exponentialRate (dict) --The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.
            baseRatePerMinute (integer) -- [REQUIRED]The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.
            incrementFactor (float) -- [REQUIRED]The exponential factor to increase the rate of rollout for a job.
            rateIncreaseCriteria (dict) -- [REQUIRED]The criteria to initiate the increase in rate of rollout for a job.
            AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).
            numberOfNotifiedThings (integer) --The threshold for number of notified things that will initiate the increase in rate of rollout.
            numberOfSucceededThings (integer) --The threshold for number of succeeded things that will initiate the increase in rate of rollout.
            
            

    :type abortConfig: dict
    :param abortConfig: Allows you to create criteria to abort a job.
            criteriaList (list) -- [REQUIRED]The list of abort criteria to define rules to abort the job.
            (dict) --Details of abort criteria to define rules to abort the job.
            failureType (string) -- [REQUIRED]The type of job execution failure to define a rule to initiate a job abort.
            action (string) -- [REQUIRED]The type of abort action to initiate a job abort.
            thresholdPercentage (float) -- [REQUIRED]The threshold as a percentage of the total number of executed things that will initiate a job abort.
            AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).
            minNumberOfExecutedThings (integer) -- [REQUIRED]Minimum number of executed things before evaluating an abort rule.
            
            

    :type timeoutConfig: dict
    :param timeoutConfig: Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to IN_PROGRESS . If the job execution status is not set to another terminal state before the time expires, it will be automatically set to TIMED_OUT .
            inProgressTimeoutInMinutes (integer) --Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can't be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal TIMED_OUT status.
            

    :type tags: list
    :param tags: Metadata which can be used to manage the job.
            (dict) --A set of key/value pairs that are used to manage the resource.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            

    :rtype: dict
    :return: {
        'jobArn': 'string',
        'jobId': 'string',
        'description': 'string'
    }
    
    
    """
    pass

def create_keys_and_certificate(setAsActive=None):
    """
    Creates a 2048-bit RSA key pair and issues an X.509 certificate using the issued public key.
    See also: AWS API Documentation
    
    
    :example: response = client.create_keys_and_certificate(
        setAsActive=True|False
    )
    
    
    :type setAsActive: boolean
    :param setAsActive: Specifies whether the certificate is active.

    :rtype: dict
    :return: {
        'certificateArn': 'string',
        'certificateId': 'string',
        'certificatePem': 'string',
        'keyPair': {
            'PublicKey': 'string',
            'PrivateKey': 'string'
        }
    }
    
    
    """
    pass

def create_ota_update(otaUpdateId=None, description=None, targets=None, targetSelection=None, awsJobExecutionsRolloutConfig=None, files=None, roleArn=None, additionalParameters=None):
    """
    Creates an AWS IoT OTAUpdate on a target group of things or groups.
    See also: AWS API Documentation
    
    
    :example: response = client.create_ota_update(
        otaUpdateId='string',
        description='string',
        targets=[
            'string',
        ],
        targetSelection='CONTINUOUS'|'SNAPSHOT',
        awsJobExecutionsRolloutConfig={
            'maximumPerMinute': 123
        },
        files=[
            {
                'fileName': 'string',
                'fileVersion': 'string',
                'fileLocation': {
                    'stream': {
                        'streamId': 'string',
                        'fileId': 123
                    },
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'version': 'string'
                    }
                },
                'codeSigning': {
                    'awsSignerJobId': 'string',
                    'startSigningJobParameter': {
                        'signingProfileParameter': {
                            'certificateArn': 'string',
                            'platform': 'string',
                            'certificatePathOnDevice': 'string'
                        },
                        'signingProfileName': 'string',
                        'destination': {
                            's3Destination': {
                                'bucket': 'string',
                                'prefix': 'string'
                            }
                        }
                    },
                    'customCodeSigning': {
                        'signature': {
                            'inlineDocument': b'bytes'
                        },
                        'certificateChain': {
                            'certificateName': 'string',
                            'inlineDocument': 'string'
                        },
                        'hashAlgorithm': 'string',
                        'signatureAlgorithm': 'string'
                    }
                },
                'attributes': {
                    'string': 'string'
                }
            },
        ],
        roleArn='string',
        additionalParameters={
            'string': 'string'
        }
    )
    
    
    :type otaUpdateId: string
    :param otaUpdateId: [REQUIRED]
            The ID of the OTA update to be created.
            

    :type description: string
    :param description: The description of the OTA update.

    :type targets: list
    :param targets: [REQUIRED]
            The targeted devices to receive OTA updates.
            (string) --
            

    :type targetSelection: string
    :param targetSelection: Specifies whether the update will continue to run (CONTINUOUS), or will be complete after all the things specified as targets have completed the update (SNAPSHOT). If continuous, the update may also be run on a thing when a change is detected in a target. For example, an update will run on a thing when the thing is added to a target group, even after the update was completed by all things originally in the group. Valid values: CONTINUOUS | SNAPSHOT.

    :type awsJobExecutionsRolloutConfig: dict
    :param awsJobExecutionsRolloutConfig: Configuration for the rollout of OTA updates.
            maximumPerMinute (integer) --The maximum number of OTA update job executions started per minute.
            

    :type files: list
    :param files: [REQUIRED]
            The files to be streamed by the OTA update.
            (dict) --Describes a file to be associated with an OTA update.
            fileName (string) --The name of the file.
            fileVersion (string) --The file version.
            fileLocation (dict) --The location of the updated firmware.
            stream (dict) --The stream that contains the OTA update.
            streamId (string) --The stream ID.
            fileId (integer) --The ID of a file associated with a stream.
            s3Location (dict) --The location of the updated firmware in S3.
            bucket (string) --The S3 bucket.
            key (string) --The S3 key.
            version (string) --The S3 bucket version.
            
            codeSigning (dict) --The code signing method of the file.
            awsSignerJobId (string) --The ID of the AWSSignerJob which was created to sign the file.
            startSigningJobParameter (dict) --Describes the code-signing job.
            signingProfileParameter (dict) --Describes the code-signing profile.
            certificateArn (string) --Certificate ARN.
            platform (string) --The hardware platform of your device.
            certificatePathOnDevice (string) --The location of the code-signing certificate on your device.
            signingProfileName (string) --The code-signing profile name.
            destination (dict) --The location to write the code-signed file.
            s3Destination (dict) --Describes the location in S3 of the updated firmware.
            bucket (string) --The S3 bucket that contains the updated firmware.
            prefix (string) --The S3 prefix.
            
            customCodeSigning (dict) --A custom method for code signing a file.
            signature (dict) --The signature for the file.
            inlineDocument (bytes) --A base64 encoded binary representation of the code signing signature.
            certificateChain (dict) --The certificate chain.
            certificateName (string) --The name of the certificate.
            inlineDocument (string) --A base64 encoded binary representation of the code signing certificate chain.
            hashAlgorithm (string) --The hash algorithm used to code sign the file.
            signatureAlgorithm (string) --The signature algorithm used to code sign the file.
            
            attributes (dict) --A list of name/attribute pairs.
            (string) --
            (string) --
            
            

    :type roleArn: string
    :param roleArn: [REQUIRED]
            The IAM role that allows access to the AWS IoT Jobs service.
            

    :type additionalParameters: dict
    :param additionalParameters: A list of additional OTA update parameters which are name-value pairs.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'otaUpdateId': 'string',
        'awsIotJobId': 'string',
        'otaUpdateArn': 'string',
        'awsIotJobArn': 'string',
        'otaUpdateStatus': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
    }
    
    
    """
    pass

def create_policy(policyName=None, policyDocument=None):
    """
    Creates an AWS IoT policy.
    The created policy is the default version for the policy. This operation creates a policy version with a version identifier of 1 and sets 1 as the policy's default version.
    See also: AWS API Documentation
    
    
    :example: response = client.create_policy(
        policyName='string',
        policyDocument='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type policyDocument: string
    :param policyDocument: [REQUIRED]
            The JSON document that describes the policy. policyDocument must have a minimum length of 1, with a maximum length of 2048, excluding whitespace.
            

    :rtype: dict
    :return: {
        'policyName': 'string',
        'policyArn': 'string',
        'policyDocument': 'string',
        'policyVersionId': 'string'
    }
    
    
    """
    pass

def create_policy_version(policyName=None, policyDocument=None, setAsDefault=None):
    """
    Creates a new version of the specified AWS IoT policy. To update a policy, create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must use  DeletePolicyVersion to delete an existing version before you create a new one.
    Optionally, you can set the new version as the policy's default version. The default version is the operative version (that is, the version that is in effect for the certificates to which the policy is attached).
    See also: AWS API Documentation
    
    
    :example: response = client.create_policy_version(
        policyName='string',
        policyDocument='string',
        setAsDefault=True|False
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type policyDocument: string
    :param policyDocument: [REQUIRED]
            The JSON document that describes the policy. Minimum length of 1. Maximum length of 2048, excluding whitespace.
            

    :type setAsDefault: boolean
    :param setAsDefault: Specifies whether the policy version is set as the default. When this parameter is true, the new policy version becomes the operative version (that is, the version that is in effect for the certificates to which the policy is attached).

    :rtype: dict
    :return: {
        'policyArn': 'string',
        'policyDocument': 'string',
        'policyVersionId': 'string',
        'isDefaultVersion': True|False
    }
    
    
    """
    pass

def create_role_alias(roleAlias=None, roleArn=None, credentialDurationSeconds=None):
    """
    Creates a role alias.
    See also: AWS API Documentation
    
    
    :example: response = client.create_role_alias(
        roleAlias='string',
        roleArn='string',
        credentialDurationSeconds=123
    )
    
    
    :type roleAlias: string
    :param roleAlias: [REQUIRED]
            The role alias that points to a role ARN. This allows you to change the role without having to update the device.
            

    :type roleArn: string
    :param roleArn: [REQUIRED]
            The role ARN.
            

    :type credentialDurationSeconds: integer
    :param credentialDurationSeconds: How long (in seconds) the credentials will be valid.

    :rtype: dict
    :return: {
        'roleAlias': 'string',
        'roleAliasArn': 'string'
    }
    
    
    """
    pass

def create_scheduled_audit(frequency=None, dayOfMonth=None, dayOfWeek=None, targetCheckNames=None, scheduledAuditName=None):
    """
    Creates a scheduled audit that is run at a specified time interval.
    See also: AWS API Documentation
    
    
    :example: response = client.create_scheduled_audit(
        frequency='DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
        dayOfMonth='string',
        dayOfWeek='SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT',
        targetCheckNames=[
            'string',
        ],
        scheduledAuditName='string'
    )
    
    
    :type frequency: string
    :param frequency: [REQUIRED]
            How often the scheduled audit takes place. Can be one of 'DAILY', 'WEEKLY', 'BIWEEKLY' or 'MONTHLY'. The actual start time of each audit is determined by the system.
            

    :type dayOfMonth: string
    :param dayOfMonth: The day of the month on which the scheduled audit takes place. Can be '1' through '31' or 'LAST'. This field is required if the 'frequency' parameter is set to 'MONTHLY'. If days 29-31 are specified, and the month does not have that many days, the audit takes place on the 'LAST' day of the month.

    :type dayOfWeek: string
    :param dayOfWeek: The day of the week on which the scheduled audit takes place. Can be one of 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI' or 'SAT'. This field is required if the 'frequency' parameter is set to 'WEEKLY' or 'BIWEEKLY'.

    :type targetCheckNames: list
    :param targetCheckNames: [REQUIRED]
            Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks including those that are enabled or UpdateAccountAuditConfiguration to select which checks are enabled.)
            (string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks including those that are enabled or UpdateAccountAuditConfiguration to select which checks are enabled.)
            

    :type scheduledAuditName: string
    :param scheduledAuditName: [REQUIRED]
            The name you want to give to the scheduled audit. (Max. 128 chars)
            

    :rtype: dict
    :return: {
        'scheduledAuditArn': 'string'
    }
    
    
    """
    pass

def create_security_profile(securityProfileName=None, securityProfileDescription=None, behaviors=None, alertTargets=None, tags=None):
    """
    Creates a Device Defender security profile.
    See also: AWS API Documentation
    
    
    :example: response = client.create_security_profile(
        securityProfileName='string',
        securityProfileDescription='string',
        behaviors=[
            {
                'name': 'string',
                'metric': 'string',
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123
                }
            },
        ],
        alertTargets={
            'string': {
                'alertTargetArn': 'string',
                'roleArn': 'string'
            }
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]
            The name you are giving to the security profile.
            

    :type securityProfileDescription: string
    :param securityProfileDescription: A description of the security profile.

    :type behaviors: list
    :param behaviors: [REQUIRED]
            Specifies the behaviors that, when violated by a device (thing), cause an alert.
            (dict) --A Device Defender security profile behavior.
            name (string) -- [REQUIRED]The name you have given to the behavior.
            metric (string) --What is measured by the behavior.
            criteria (dict) --The criteria that determine if a device is behaving normally in regard to the metric .
            comparisonOperator (string) --The operator that relates the thing measured (metric ) to the criteria (value ).
            value (dict) --The value to be compared with the metric .
            count (integer) --If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .
            cidrs (list) --If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .
            (string) --
            ports (list) --If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .
            (integer) --
            
            durationSeconds (integer) --Use this to specify the period of time over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ).
            
            

    :type alertTargets: dict
    :param alertTargets: Specifies the destinations to which alerts are sent. (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.
            (string) --The type of alert target: one of 'SNS'.
            (dict) --A structure containing the alert target ARN and the role ARN.
            alertTargetArn (string) -- [REQUIRED]The ARN of the notification target to which alerts are sent.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants permission to send alerts to the notification target.
            
            

    :type tags: list
    :param tags: Metadata which can be used to manage the security profile.
            (dict) --A set of key/value pairs that are used to manage the resource.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            

    :rtype: dict
    :return: {
        'securityProfileName': 'string',
        'securityProfileArn': 'string'
    }
    
    
    """
    pass

def create_stream(streamId=None, description=None, files=None, roleArn=None):
    """
    Creates a stream for delivering one or more large files in chunks over MQTT. A stream transports data bytes in chunks or blocks packaged as MQTT messages from a source like S3. You can have one or more files associated with a stream. The total size of a file associated with the stream cannot exceed more than 2 MB. The stream will be created with version 0. If a stream is created with the same streamID as a stream that existed and was deleted within last 90 days, we will resurrect that old stream by incrementing the version by 1.
    See also: AWS API Documentation
    
    
    :example: response = client.create_stream(
        streamId='string',
        description='string',
        files=[
            {
                'fileId': 123,
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'version': 'string'
                }
            },
        ],
        roleArn='string'
    )
    
    
    :type streamId: string
    :param streamId: [REQUIRED]
            The stream ID.
            

    :type description: string
    :param description: A description of the stream.

    :type files: list
    :param files: [REQUIRED]
            The files to stream.
            (dict) --Represents a file to stream.
            fileId (integer) --The file ID.
            s3Location (dict) --The location of the file in S3.
            bucket (string) --The S3 bucket.
            key (string) --The S3 key.
            version (string) --The S3 bucket version.
            
            

    :type roleArn: string
    :param roleArn: [REQUIRED]
            An IAM role that allows the IoT service principal assumes to access your S3 files.
            

    :rtype: dict
    :return: {
        'streamId': 'string',
        'streamArn': 'string',
        'description': 'string',
        'streamVersion': 123
    }
    
    
    """
    pass

def create_thing(thingName=None, thingTypeName=None, attributePayload=None, billingGroupName=None):
    """
    Creates a thing record in the registry.
    See also: AWS API Documentation
    
    
    :example: response = client.create_thing(
        thingName='string',
        thingTypeName='string',
        attributePayload={
            'attributes': {
                'string': 'string'
            },
            'merge': True|False
        },
        billingGroupName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing to create.
            

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type associated with the new thing.

    :type attributePayload: dict
    :param attributePayload: The attribute payload, which consists of up to three name/value pairs in a JSON document. For example:
            {\'attributes\':{\'string1\':\'string2\'}}
            attributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:
            {\'attributes\':{\'string1\':\'string2\'}}
            (string) --
            (string) --
            
            merge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.
            To remove an attribute, call UpdateThing with an empty attribute value.
            Note
            The merge attribute is only valid when calling UpdateThing .
            

    :type billingGroupName: string
    :param billingGroupName: The name of the billing group the thing will be added to.

    :rtype: dict
    :return: {
        'thingName': 'string',
        'thingArn': 'string',
        'thingId': 'string'
    }
    
    
    """
    pass

def create_thing_group(thingGroupName=None, parentGroupName=None, thingGroupProperties=None, tags=None):
    """
    Create a thing group.
    See also: AWS API Documentation
    
    
    :example: response = client.create_thing_group(
        thingGroupName='string',
        parentGroupName='string',
        thingGroupProperties={
            'thingGroupDescription': 'string',
            'attributePayload': {
                'attributes': {
                    'string': 'string'
                },
                'merge': True|False
            }
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]
            The thing group name to create.
            

    :type parentGroupName: string
    :param parentGroupName: The name of the parent thing group.

    :type thingGroupProperties: dict
    :param thingGroupProperties: The thing group properties.
            thingGroupDescription (string) --The thing group description.
            attributePayload (dict) --The thing group attributes in JSON format.
            attributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:
            {\'attributes\':{\'string1\':\'string2\'}}
            (string) --
            (string) --
            
            merge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.
            To remove an attribute, call UpdateThing with an empty attribute value.
            Note
            The merge attribute is only valid when calling UpdateThing .
            
            

    :type tags: list
    :param tags: Metadata which can be used to manage the thing group.
            (dict) --A set of key/value pairs that are used to manage the resource.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            

    :rtype: dict
    :return: {
        'thingGroupName': 'string',
        'thingGroupArn': 'string',
        'thingGroupId': 'string'
    }
    
    
    """
    pass

def create_thing_type(thingTypeName=None, thingTypeProperties=None, tags=None):
    """
    Creates a new thing type.
    See also: AWS API Documentation
    
    
    :example: response = client.create_thing_type(
        thingTypeName='string',
        thingTypeProperties={
            'thingTypeDescription': 'string',
            'searchableAttributes': [
                'string',
            ]
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]
            The name of the thing type.
            

    :type thingTypeProperties: dict
    :param thingTypeProperties: The ThingTypeProperties for the thing type to create. It contains information about the new thing type including a description, and a list of searchable thing attribute names.
            thingTypeDescription (string) --The description of the thing type.
            searchableAttributes (list) --A list of searchable thing attribute names.
            (string) --
            

    :type tags: list
    :param tags: Metadata which can be used to manage the thing type.
            (dict) --A set of key/value pairs that are used to manage the resource.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            

    :rtype: dict
    :return: {
        'thingTypeName': 'string',
        'thingTypeArn': 'string',
        'thingTypeId': 'string'
    }
    
    
    """
    pass

def create_topic_rule(ruleName=None, topicRulePayload=None):
    """
    Creates a rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.create_topic_rule(
        ruleName='string',
        topicRulePayload={
            'sql': 'string',
            'description': 'string',
            'actions': [
                {
                    'dynamoDB': {
                        'tableName': 'string',
                        'roleArn': 'string',
                        'operation': 'string',
                        'hashKeyField': 'string',
                        'hashKeyValue': 'string',
                        'hashKeyType': 'STRING'|'NUMBER',
                        'rangeKeyField': 'string',
                        'rangeKeyValue': 'string',
                        'rangeKeyType': 'STRING'|'NUMBER',
                        'payloadField': 'string'
                    },
                    'dynamoDBv2': {
                        'roleArn': 'string',
                        'putItem': {
                            'tableName': 'string'
                        }
                    },
                    'lambda': {
                        'functionArn': 'string'
                    },
                    'sns': {
                        'targetArn': 'string',
                        'roleArn': 'string',
                        'messageFormat': 'RAW'|'JSON'
                    },
                    'sqs': {
                        'roleArn': 'string',
                        'queueUrl': 'string',
                        'useBase64': True|False
                    },
                    'kinesis': {
                        'roleArn': 'string',
                        'streamName': 'string',
                        'partitionKey': 'string'
                    },
                    'republish': {
                        'roleArn': 'string',
                        'topic': 'string'
                    },
                    's3': {
                        'roleArn': 'string',
                        'bucketName': 'string',
                        'key': 'string',
                        'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                    },
                    'firehose': {
                        'roleArn': 'string',
                        'deliveryStreamName': 'string',
                        'separator': 'string'
                    },
                    'cloudwatchMetric': {
                        'roleArn': 'string',
                        'metricNamespace': 'string',
                        'metricName': 'string',
                        'metricValue': 'string',
                        'metricUnit': 'string',
                        'metricTimestamp': 'string'
                    },
                    'cloudwatchAlarm': {
                        'roleArn': 'string',
                        'alarmName': 'string',
                        'stateReason': 'string',
                        'stateValue': 'string'
                    },
                    'elasticsearch': {
                        'roleArn': 'string',
                        'endpoint': 'string',
                        'index': 'string',
                        'type': 'string',
                        'id': 'string'
                    },
                    'salesforce': {
                        'token': 'string',
                        'url': 'string'
                    },
                    'iotAnalytics': {
                        'channelArn': 'string',
                        'channelName': 'string',
                        'roleArn': 'string'
                    },
                    'iotEvents': {
                        'inputName': 'string',
                        'messageId': 'string',
                        'roleArn': 'string'
                    },
                    'stepFunctions': {
                        'executionNamePrefix': 'string',
                        'stateMachineName': 'string',
                        'roleArn': 'string'
                    }
                },
            ],
            'ruleDisabled': True|False,
            'awsIotSqlVersion': 'string',
            'errorAction': {
                'dynamoDB': {
                    'tableName': 'string',
                    'roleArn': 'string',
                    'operation': 'string',
                    'hashKeyField': 'string',
                    'hashKeyValue': 'string',
                    'hashKeyType': 'STRING'|'NUMBER',
                    'rangeKeyField': 'string',
                    'rangeKeyValue': 'string',
                    'rangeKeyType': 'STRING'|'NUMBER',
                    'payloadField': 'string'
                },
                'dynamoDBv2': {
                    'roleArn': 'string',
                    'putItem': {
                        'tableName': 'string'
                    }
                },
                'lambda': {
                    'functionArn': 'string'
                },
                'sns': {
                    'targetArn': 'string',
                    'roleArn': 'string',
                    'messageFormat': 'RAW'|'JSON'
                },
                'sqs': {
                    'roleArn': 'string',
                    'queueUrl': 'string',
                    'useBase64': True|False
                },
                'kinesis': {
                    'roleArn': 'string',
                    'streamName': 'string',
                    'partitionKey': 'string'
                },
                'republish': {
                    'roleArn': 'string',
                    'topic': 'string'
                },
                's3': {
                    'roleArn': 'string',
                    'bucketName': 'string',
                    'key': 'string',
                    'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                },
                'firehose': {
                    'roleArn': 'string',
                    'deliveryStreamName': 'string',
                    'separator': 'string'
                },
                'cloudwatchMetric': {
                    'roleArn': 'string',
                    'metricNamespace': 'string',
                    'metricName': 'string',
                    'metricValue': 'string',
                    'metricUnit': 'string',
                    'metricTimestamp': 'string'
                },
                'cloudwatchAlarm': {
                    'roleArn': 'string',
                    'alarmName': 'string',
                    'stateReason': 'string',
                    'stateValue': 'string'
                },
                'elasticsearch': {
                    'roleArn': 'string',
                    'endpoint': 'string',
                    'index': 'string',
                    'type': 'string',
                    'id': 'string'
                },
                'salesforce': {
                    'token': 'string',
                    'url': 'string'
                },
                'iotAnalytics': {
                    'channelArn': 'string',
                    'channelName': 'string',
                    'roleArn': 'string'
                },
                'iotEvents': {
                    'inputName': 'string',
                    'messageId': 'string',
                    'roleArn': 'string'
                },
                'stepFunctions': {
                    'executionNamePrefix': 'string',
                    'stateMachineName': 'string',
                    'roleArn': 'string'
                }
            }
        }
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the rule.
            

    :type topicRulePayload: dict
    :param topicRulePayload: [REQUIRED]
            The rule payload.
            sql (string) -- [REQUIRED]The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference in the AWS IoT Developer Guide .
            description (string) --The description of the rule.
            actions (list) -- [REQUIRED]The actions associated with the rule.
            (dict) --Describes the actions associated with a rule.
            dynamoDB (dict) --Write to a DynamoDB table.
            tableName (string) -- [REQUIRED]The name of the DynamoDB table.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.
            operation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .
            hashKeyField (string) -- [REQUIRED]The hash key name.
            hashKeyValue (string) -- [REQUIRED]The hash key value.
            hashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'
            rangeKeyField (string) --The range key name.
            rangeKeyValue (string) --The range key value.
            rangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'
            payloadField (string) --The action payload. This name can be customized.
            dynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
            roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.
            putItem (dict) --Specifies the DynamoDB table to which the message data will be written. For example:
            { 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }
            Each attribute in the message payload will be written to a separate column in the DynamoDB database.
            tableName (string) -- [REQUIRED]The table where the message data will be written
            
            lambda (dict) --Invoke a Lambda function.
            functionArn (string) -- [REQUIRED]The ARN of the Lambda function.
            sns (dict) --Publish to an Amazon SNS topic.
            targetArn (string) -- [REQUIRED]The ARN of the SNS topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            messageFormat (string) --(Optional) The message format of the message to publish. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see http://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.
            sqs (dict) --Publish to an Amazon SQS queue.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            queueUrl (string) -- [REQUIRED]The URL of the Amazon SQS queue.
            useBase64 (boolean) --Specifies whether to use Base64 encoding.
            kinesis (dict) --Write data to an Amazon Kinesis stream.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the Amazon Kinesis stream.
            streamName (string) -- [REQUIRED]The name of the Amazon Kinesis stream.
            partitionKey (string) --The partition key.
            republish (dict) --Publish to another MQTT topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            topic (string) -- [REQUIRED]The name of the MQTT topic.
            s3 (dict) --Write to an Amazon S3 bucket.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            bucketName (string) -- [REQUIRED]The Amazon S3 bucket.
            key (string) -- [REQUIRED]The object key.
            cannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .
            firehose (dict) --Write to an Amazon Kinesis Firehose stream.
            roleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehose stream.
            deliveryStreamName (string) -- [REQUIRED]The delivery stream name.
            separator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: 'n' (newline), 't' (tab), 'rn' (Windows newline), ',' (comma).
            cloudwatchMetric (dict) --Capture a CloudWatch metric.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch metric.
            metricNamespace (string) -- [REQUIRED]The CloudWatch metric namespace name.
            metricName (string) -- [REQUIRED]The CloudWatch metric name.
            metricValue (string) -- [REQUIRED]The CloudWatch metric value.
            metricUnit (string) -- [REQUIRED]The metric unit supported by CloudWatch.
            metricTimestamp (string) --An optional Unix timestamp .
            cloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch alarm.
            alarmName (string) -- [REQUIRED]The CloudWatch alarm name.
            stateReason (string) -- [REQUIRED]The reason for the alarm change.
            stateValue (string) -- [REQUIRED]The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
            elasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.
            roleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.
            endpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.
            index (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.
            type (string) -- [REQUIRED]The type of document you are storing.
            id (string) -- [REQUIRED]The unique identifier for the document you are storing.
            salesforce (dict) --Send a message to a Salesforce IoT Cloud Input Stream.
            token (string) -- [REQUIRED]The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
            url (string) -- [REQUIRED]The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
            iotAnalytics (dict) --Sends message data to an AWS IoT Analytics channel.
            channelArn (string) --(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
            channelName (string) --The name of the IoT Analytics channel to which message data will be sent.
            roleArn (string) --The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
            iotEvents (dict) --Sends an input to an AWS IoT Events detector.
            inputName (string) -- [REQUIRED]The name of the AWS IoT Events input.
            messageId (string) --[Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ('Action':'iotevents:BatchPutMessage').
            stepFunctions (dict) --Starts execution of a Step Functions state machine.
            executionNamePrefix (string) --(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
            stateMachineName (string) -- [REQUIRED]The name of the Step Functions state machine whose execution will be started.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants IoT permission to start execution of a state machine ('Action':'states:StartExecution').
            
            ruleDisabled (boolean) --Specifies whether the rule is disabled.
            awsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.
            errorAction (dict) --The action to take when an error occurs.
            dynamoDB (dict) --Write to a DynamoDB table.
            tableName (string) -- [REQUIRED]The name of the DynamoDB table.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.
            operation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .
            hashKeyField (string) -- [REQUIRED]The hash key name.
            hashKeyValue (string) -- [REQUIRED]The hash key value.
            hashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'
            rangeKeyField (string) --The range key name.
            rangeKeyValue (string) --The range key value.
            rangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'
            payloadField (string) --The action payload. This name can be customized.
            dynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
            roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.
            putItem (dict) --Specifies the DynamoDB table to which the message data will be written. For example:
            { 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }
            Each attribute in the message payload will be written to a separate column in the DynamoDB database.
            tableName (string) -- [REQUIRED]The table where the message data will be written
            
            lambda (dict) --Invoke a Lambda function.
            functionArn (string) -- [REQUIRED]The ARN of the Lambda function.
            sns (dict) --Publish to an Amazon SNS topic.
            targetArn (string) -- [REQUIRED]The ARN of the SNS topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            messageFormat (string) --(Optional) The message format of the message to publish. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see http://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.
            sqs (dict) --Publish to an Amazon SQS queue.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            queueUrl (string) -- [REQUIRED]The URL of the Amazon SQS queue.
            useBase64 (boolean) --Specifies whether to use Base64 encoding.
            kinesis (dict) --Write data to an Amazon Kinesis stream.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the Amazon Kinesis stream.
            streamName (string) -- [REQUIRED]The name of the Amazon Kinesis stream.
            partitionKey (string) --The partition key.
            republish (dict) --Publish to another MQTT topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            topic (string) -- [REQUIRED]The name of the MQTT topic.
            s3 (dict) --Write to an Amazon S3 bucket.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            bucketName (string) -- [REQUIRED]The Amazon S3 bucket.
            key (string) -- [REQUIRED]The object key.
            cannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .
            firehose (dict) --Write to an Amazon Kinesis Firehose stream.
            roleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehose stream.
            deliveryStreamName (string) -- [REQUIRED]The delivery stream name.
            separator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: 'n' (newline), 't' (tab), 'rn' (Windows newline), ',' (comma).
            cloudwatchMetric (dict) --Capture a CloudWatch metric.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch metric.
            metricNamespace (string) -- [REQUIRED]The CloudWatch metric namespace name.
            metricName (string) -- [REQUIRED]The CloudWatch metric name.
            metricValue (string) -- [REQUIRED]The CloudWatch metric value.
            metricUnit (string) -- [REQUIRED]The metric unit supported by CloudWatch.
            metricTimestamp (string) --An optional Unix timestamp .
            cloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch alarm.
            alarmName (string) -- [REQUIRED]The CloudWatch alarm name.
            stateReason (string) -- [REQUIRED]The reason for the alarm change.
            stateValue (string) -- [REQUIRED]The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
            elasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.
            roleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.
            endpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.
            index (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.
            type (string) -- [REQUIRED]The type of document you are storing.
            id (string) -- [REQUIRED]The unique identifier for the document you are storing.
            salesforce (dict) --Send a message to a Salesforce IoT Cloud Input Stream.
            token (string) -- [REQUIRED]The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
            url (string) -- [REQUIRED]The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
            iotAnalytics (dict) --Sends message data to an AWS IoT Analytics channel.
            channelArn (string) --(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
            channelName (string) --The name of the IoT Analytics channel to which message data will be sent.
            roleArn (string) --The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
            iotEvents (dict) --Sends an input to an AWS IoT Events detector.
            inputName (string) -- [REQUIRED]The name of the AWS IoT Events input.
            messageId (string) --[Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ('Action':'iotevents:BatchPutMessage').
            stepFunctions (dict) --Starts execution of a Step Functions state machine.
            executionNamePrefix (string) --(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
            stateMachineName (string) -- [REQUIRED]The name of the Step Functions state machine whose execution will be started.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants IoT permission to start execution of a state machine ('Action':'states:StartExecution').
            
            

    """
    pass

def delete_account_audit_configuration(deleteScheduledAudits=None):
    """
    Restores the default settings for Device Defender audits for this account. Any configuration data you entered is deleted and all audit checks are reset to disabled.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_account_audit_configuration(
        deleteScheduledAudits=True|False
    )
    
    
    :type deleteScheduledAudits: boolean
    :param deleteScheduledAudits: If true, all scheduled audits are deleted.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_authorizer(authorizerName=None):
    """
    Deletes an authorizer.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_authorizer(
        authorizerName='string'
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]
            The name of the authorizer to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_billing_group(billingGroupName=None, expectedVersion=None):
    """
    Deletes the billing group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_billing_group(
        billingGroupName='string',
        expectedVersion=123
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: [REQUIRED]
            The name of the billing group.
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the billing group. If the version of the billing group does not match the expected version specified in the request, the DeleteBillingGroup request is rejected with a VersionConflictException .

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_ca_certificate(certificateId=None):
    """
    Deletes a registered CA certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_ca_certificate(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate to delete. (The last part of the certificate ARN contains the certificate ID.)
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_certificate(certificateId=None, forceDelete=None):
    """
    Deletes the specified certificate.
    A certificate cannot be deleted if it has a policy attached to it or if its status is set to ACTIVE. To delete a certificate, first use the  DetachPrincipalPolicy API to detach all policies. Next, use the  UpdateCertificate API to set the certificate to the INACTIVE status.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_certificate(
        certificateId='string',
        forceDelete=True|False
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
            

    :type forceDelete: boolean
    :param forceDelete: Forces a certificate request to be deleted.

    """
    pass

def delete_dynamic_thing_group(thingGroupName=None, expectedVersion=None):
    """
    Deletes a dynamic thing group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_dynamic_thing_group(
        thingGroupName='string',
        expectedVersion=123
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]
            The name of the dynamic thing group to delete.
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the dynamic thing group to delete.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_job(jobId=None, force=None):
    """
    Deletes a job and its related job executions.
    Deleting a job may take time, depending on the number of job executions created for the job and various other factors. While the job is being deleted, the status of the job will be shown as "DELETION_IN_PROGRESS". Attempting to delete or cancel a job whose status is already "DELETION_IN_PROGRESS" will result in an error.
    Only 10 jobs may have status "DELETION_IN_PROGRESS" at the same time, or a LimitExceededException will occur.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_job(
        jobId='string',
        force=True|False
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The ID of the job to be deleted.
            After a job deletion is completed, you may reuse this jobId when you create a new job. However, this is not recommended, and you must ensure that your devices are not using the jobId to refer to the deleted job.
            

    :type force: boolean
    :param force: (Optional) When true, you can delete a job which is 'IN_PROGRESS'. Otherwise, you can only delete a job which is in a terminal state ('COMPLETED' or 'CANCELED') or an exception will occur. The default is false.
            Note
            Deleting a job which is 'IN_PROGRESS', will cause a device which is executing the job to be unable to access job information or update the job execution status. Use caution and ensure that each device executing a job which is deleted is able to recover to a valid state.
            

    """
    pass

def delete_job_execution(jobId=None, thingName=None, executionNumber=None, force=None):
    """
    Deletes a job execution.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_job_execution(
        jobId='string',
        thingName='string',
        executionNumber=123,
        force=True|False
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The ID of the job whose execution on a particular device will be deleted.
            

    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing whose job execution will be deleted.
            

    :type executionNumber: integer
    :param executionNumber: [REQUIRED]
            The ID of the job execution to be deleted. The executionNumber refers to the execution of a particular job on a particular device.
            Note that once a job execution is deleted, the executionNumber may be reused by IoT, so be sure you get and use the correct value here.
            

    :type force: boolean
    :param force: (Optional) When true, you can delete a job execution which is 'IN_PROGRESS'. Otherwise, you can only delete a job execution which is in a terminal state ('SUCCEEDED', 'FAILED', 'REJECTED', 'REMOVED' or 'CANCELED') or an exception will occur. The default is false.
            Note
            Deleting a job execution which is 'IN_PROGRESS', will cause the device to be unable to access job information or update the job execution status. Use caution and ensure that the device is able to recover to a valid state.
            

    """
    pass

def delete_ota_update(otaUpdateId=None, deleteStream=None, forceDeleteAWSJob=None):
    """
    Delete an OTA update.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_ota_update(
        otaUpdateId='string',
        deleteStream=True|False,
        forceDeleteAWSJob=True|False
    )
    
    
    :type otaUpdateId: string
    :param otaUpdateId: [REQUIRED]
            The OTA update ID to delete.
            

    :type deleteStream: boolean
    :param deleteStream: Specifies if the stream associated with an OTA update should be deleted when the OTA update is deleted.

    :type forceDeleteAWSJob: boolean
    :param forceDeleteAWSJob: Specifies if the AWS Job associated with the OTA update should be deleted with the OTA update is deleted.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_policy(policyName=None):
    """
    Deletes the specified policy.
    A policy cannot be deleted if it has non-default versions or it is attached to any certificate.
    To delete a policy, use the DeletePolicyVersion API to delete all non-default versions of the policy; use the DetachPrincipalPolicy API to detach the policy from any certificate; and then use the DeletePolicy API to delete the policy.
    When a policy is deleted using DeletePolicy, its default version is deleted with it.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_policy(
        policyName='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy to delete.
            

    """
    pass

def delete_policy_version(policyName=None, policyVersionId=None):
    """
    Deletes the specified version of the specified policy. You cannot delete the default version of a policy using this API. To delete the default version of a policy, use  DeletePolicy . To find out which version of a policy is marked as the default version, use ListPolicyVersions.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_policy_version(
        policyName='string',
        policyVersionId='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy.
            

    :type policyVersionId: string
    :param policyVersionId: [REQUIRED]
            The policy version ID.
            

    """
    pass

def delete_registration_code():
    """
    Deletes a CA certificate registration code.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_registration_code()
    
    
    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_role_alias(roleAlias=None):
    """
    Deletes a role alias
    See also: AWS API Documentation
    
    
    :example: response = client.delete_role_alias(
        roleAlias='string'
    )
    
    
    :type roleAlias: string
    :param roleAlias: [REQUIRED]
            The role alias to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_scheduled_audit(scheduledAuditName=None):
    """
    Deletes a scheduled audit.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_scheduled_audit(
        scheduledAuditName='string'
    )
    
    
    :type scheduledAuditName: string
    :param scheduledAuditName: [REQUIRED]
            The name of the scheduled audit you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_security_profile(securityProfileName=None, expectedVersion=None):
    """
    Deletes a Device Defender security profile.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_security_profile(
        securityProfileName='string',
        expectedVersion=123
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]
            The name of the security profile to be deleted.
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the security profile. A new version is generated whenever the security profile is updated. If you specify a value that is different than the actual version, a VersionConflictException is thrown.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_stream(streamId=None):
    """
    Deletes a stream.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_stream(
        streamId='string'
    )
    
    
    :type streamId: string
    :param streamId: [REQUIRED]
            The stream ID.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_thing(thingName=None, expectedVersion=None):
    """
    Deletes the specified thing. Returns successfully with no error if the deletion is successful or you specify a thing that doesn't exist.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_thing(
        thingName='string',
        expectedVersion=123
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing to delete.
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the DeleteThing request is rejected with a VersionConflictException .

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_thing_group(thingGroupName=None, expectedVersion=None):
    """
    Deletes a thing group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_thing_group(
        thingGroupName='string',
        expectedVersion=123
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]
            The name of the thing group to delete.
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the thing group to delete.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_thing_type(thingTypeName=None):
    """
    Deletes the specified thing type. You cannot delete a thing type if it has things associated with it. To delete a thing type, first mark it as deprecated by calling  DeprecateThingType , then remove any associated things by calling  UpdateThing to change the thing type on any associated thing, and finally use  DeleteThingType to delete the thing type.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_thing_type(
        thingTypeName='string'
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]
            The name of the thing type.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_topic_rule(ruleName=None):
    """
    Deletes the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the rule.
            

    """
    pass

def delete_v2_logging_level(targetType=None, targetName=None):
    """
    Deletes a logging level.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_v2_logging_level(
        targetType='DEFAULT'|'THING_GROUP',
        targetName='string'
    )
    
    
    :type targetType: string
    :param targetType: [REQUIRED]
            The type of resource for which you are configuring logging. Must be THING_Group .
            

    :type targetName: string
    :param targetName: [REQUIRED]
            The name of the resource for which you are configuring logging.
            

    """
    pass

def deprecate_thing_type(thingTypeName=None, undoDeprecate=None):
    """
    Deprecates a thing type. You can not associate new things with deprecated thing type.
    See also: AWS API Documentation
    
    
    :example: response = client.deprecate_thing_type(
        thingTypeName='string',
        undoDeprecate=True|False
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]
            The name of the thing type to deprecate.
            

    :type undoDeprecate: boolean
    :param undoDeprecate: Whether to undeprecate a deprecated thing type. If true , the thing type will not be deprecated anymore and you can associate it with things.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_account_audit_configuration():
    """
    Gets information about the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_audit_configuration()
    
    
    :rtype: dict
    :return: {
        'roleArn': 'string',
        'auditNotificationTargetConfigurations': {
            'string': {
                'targetArn': 'string',
                'roleArn': 'string',
                'enabled': True|False
            }
        },
        'auditCheckConfigurations': {
            'string': {
                'enabled': True|False
            }
        }
    }
    
    
    """
    pass

def describe_audit_task(taskId=None):
    """
    Gets information about a Device Defender audit.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_audit_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]
            The ID of the audit whose information you want to get.
            

    :rtype: dict
    :return: {
        'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
        'taskType': 'ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK',
        'taskStartTime': datetime(2015, 1, 1),
        'taskStatistics': {
            'totalChecks': 123,
            'inProgressChecks': 123,
            'waitingForDataCollectionChecks': 123,
            'compliantChecks': 123,
            'nonCompliantChecks': 123,
            'failedChecks': 123,
            'canceledChecks': 123
        },
        'scheduledAuditName': 'string',
        'auditDetails': {
            'string': {
                'checkRunStatus': 'IN_PROGRESS'|'WAITING_FOR_DATA_COLLECTION'|'CANCELED'|'COMPLETED_COMPLIANT'|'COMPLETED_NON_COMPLIANT'|'FAILED',
                'checkCompliant': True|False,
                'totalResourcesCount': 123,
                'nonCompliantResourcesCount': 123,
                'errorCode': 'string',
                'message': 'string'
            }
        }
    }
    
    
    """
    pass

def describe_authorizer(authorizerName=None):
    """
    Describes an authorizer.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_authorizer(
        authorizerName='string'
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]
            The name of the authorizer to describe.
            

    :rtype: dict
    :return: {
        'authorizerDescription': {
            'authorizerName': 'string',
            'authorizerArn': 'string',
            'authorizerFunctionArn': 'string',
            'tokenKeyName': 'string',
            'tokenSigningPublicKeys': {
                'string': 'string'
            },
            'status': 'ACTIVE'|'INACTIVE',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def describe_billing_group(billingGroupName=None):
    """
    Returns information about a billing group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_billing_group(
        billingGroupName='string'
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: [REQUIRED]
            The name of the billing group.
            

    :rtype: dict
    :return: {
        'billingGroupName': 'string',
        'billingGroupId': 'string',
        'billingGroupArn': 'string',
        'version': 123,
        'billingGroupProperties': {
            'billingGroupDescription': 'string'
        },
        'billingGroupMetadata': {
            'creationDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def describe_ca_certificate(certificateId=None):
    """
    Describes a registered CA certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_ca_certificate(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The CA certificate identifier.
            

    :rtype: dict
    :return: {
        'certificateDescription': {
            'certificateArn': 'string',
            'certificateId': 'string',
            'status': 'ACTIVE'|'INACTIVE',
            'certificatePem': 'string',
            'ownedBy': 'string',
            'creationDate': datetime(2015, 1, 1),
            'autoRegistrationStatus': 'ENABLE'|'DISABLE',
            'lastModifiedDate': datetime(2015, 1, 1),
            'customerVersion': 123,
            'generationId': 'string',
            'validity': {
                'notBefore': datetime(2015, 1, 1),
                'notAfter': datetime(2015, 1, 1)
            }
        },
        'registrationConfig': {
            'templateBody': 'string',
            'roleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_certificate(certificateId=None):
    """
    Gets information about the specified certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_certificate(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
            

    :rtype: dict
    :return: {
        'certificateDescription': {
            'certificateArn': 'string',
            'certificateId': 'string',
            'caCertificateId': 'string',
            'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
            'certificatePem': 'string',
            'ownedBy': 'string',
            'previousOwnedBy': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'customerVersion': 123,
            'transferData': {
                'transferMessage': 'string',
                'rejectReason': 'string',
                'transferDate': datetime(2015, 1, 1),
                'acceptDate': datetime(2015, 1, 1),
                'rejectDate': datetime(2015, 1, 1)
            },
            'generationId': 'string',
            'validity': {
                'notBefore': datetime(2015, 1, 1),
                'notAfter': datetime(2015, 1, 1)
            }
        }
    }
    
    
    """
    pass

def describe_default_authorizer():
    """
    Describes the default authorizer.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_default_authorizer()
    
    
    :rtype: dict
    :return: {
        'authorizerDescription': {
            'authorizerName': 'string',
            'authorizerArn': 'string',
            'authorizerFunctionArn': 'string',
            'tokenKeyName': 'string',
            'tokenSigningPublicKeys': {
                'string': 'string'
            },
            'status': 'ACTIVE'|'INACTIVE',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def describe_endpoint(endpointType=None):
    """
    Returns a unique endpoint specific to the AWS account making the call.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_endpoint(
        endpointType='string'
    )
    
    
    :type endpointType: string
    :param endpointType: The endpoint type. Valid endpoint types include:
            iot:Data - Returns a VeriSign signed data endpoint.
            iot:Data-ATS - Returns an ATS signed data endpoint.
            iot:CredentialProvider - Returns an AWS IoT credentials provider API endpoint.
            iot:Jobs - Returns an AWS IoT device management Jobs API endpoint.
            

    :rtype: dict
    :return: {
        'endpointAddress': 'string'
    }
    
    
    """
    pass

def describe_event_configurations():
    """
    Describes event configurations.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_configurations()
    
    
    :rtype: dict
    :return: {
        'eventConfigurations': {
            'string': {
                'Enabled': True|False
            }
        },
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_index(indexName=None):
    """
    Describes a search index.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_index(
        indexName='string'
    )
    
    
    :type indexName: string
    :param indexName: [REQUIRED]
            The index name.
            

    :rtype: dict
    :return: {
        'indexName': 'string',
        'indexStatus': 'ACTIVE'|'BUILDING'|'REBUILDING',
        'schema': 'string'
    }
    
    
    """
    pass

def describe_job(jobId=None):
    """
    Describes a job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_job(
        jobId='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique identifier you assigned to this job when it was created.
            

    :rtype: dict
    :return: {
        'documentSource': 'string',
        'job': {
            'jobArn': 'string',
            'jobId': 'string',
            'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
            'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
            'forceCanceled': True|False,
            'reasonCode': 'string',
            'comment': 'string',
            'targets': [
                'string',
            ],
            'description': 'string',
            'presignedUrlConfig': {
                'roleArn': 'string',
                'expiresInSec': 123
            },
            'jobExecutionsRolloutConfig': {
                'maximumPerMinute': 123,
                'exponentialRate': {
                    'baseRatePerMinute': 123,
                    'incrementFactor': 123.0,
                    'rateIncreaseCriteria': {
                        'numberOfNotifiedThings': 123,
                        'numberOfSucceededThings': 123
                    }
                }
            },
            'abortConfig': {
                'criteriaList': [
                    {
                        'failureType': 'FAILED'|'REJECTED'|'TIMED_OUT'|'ALL',
                        'action': 'CANCEL',
                        'thresholdPercentage': 123.0,
                        'minNumberOfExecutedThings': 123
                    },
                ]
            },
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'completedAt': datetime(2015, 1, 1),
            'jobProcessDetails': {
                'processingTargets': [
                    'string',
                ],
                'numberOfCanceledThings': 123,
                'numberOfSucceededThings': 123,
                'numberOfFailedThings': 123,
                'numberOfRejectedThings': 123,
                'numberOfQueuedThings': 123,
                'numberOfInProgressThings': 123,
                'numberOfRemovedThings': 123,
                'numberOfTimedOutThings': 123
            },
            'timeoutConfig': {
                'inProgressTimeoutInMinutes': 123
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_job_execution(jobId=None, thingName=None, executionNumber=None):
    """
    Describes a job execution.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_job_execution(
        jobId='string',
        thingName='string',
        executionNumber=123
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique identifier you assigned to this job when it was created.
            

    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing on which the job execution is running.
            

    :type executionNumber: integer
    :param executionNumber: A string (consisting of the digits '0' through '9' which is used to specify a particular job execution on a particular device.

    :rtype: dict
    :return: {
        'execution': {
            'jobId': 'string',
            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
            'forceCanceled': True|False,
            'statusDetails': {
                'detailsMap': {
                    'string': 'string'
                }
            },
            'thingArn': 'string',
            'queuedAt': datetime(2015, 1, 1),
            'startedAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'executionNumber': 123,
            'versionNumber': 123,
            'approximateSecondsBeforeTimedOut': 123
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_role_alias(roleAlias=None):
    """
    Describes a role alias.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_role_alias(
        roleAlias='string'
    )
    
    
    :type roleAlias: string
    :param roleAlias: [REQUIRED]
            The role alias to describe.
            

    :rtype: dict
    :return: {
        'roleAliasDescription': {
            'roleAlias': 'string',
            'roleAliasArn': 'string',
            'roleArn': 'string',
            'owner': 'string',
            'credentialDurationSeconds': 123,
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def describe_scheduled_audit(scheduledAuditName=None):
    """
    Gets information about a scheduled audit.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_scheduled_audit(
        scheduledAuditName='string'
    )
    
    
    :type scheduledAuditName: string
    :param scheduledAuditName: [REQUIRED]
            The name of the scheduled audit whose information you want to get.
            

    :rtype: dict
    :return: {
        'frequency': 'DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
        'dayOfMonth': 'string',
        'dayOfWeek': 'SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT',
        'targetCheckNames': [
            'string',
        ],
        'scheduledAuditName': 'string',
        'scheduledAuditArn': 'string'
    }
    
    
    """
    pass

def describe_security_profile(securityProfileName=None):
    """
    Gets information about a Device Defender security profile.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_security_profile(
        securityProfileName='string'
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]
            The name of the security profile whose information you want to get.
            

    :rtype: dict
    :return: {
        'securityProfileName': 'string',
        'securityProfileArn': 'string',
        'securityProfileDescription': 'string',
        'behaviors': [
            {
                'name': 'string',
                'metric': 'string',
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123
                }
            },
        ],
        'alertTargets': {
            'string': {
                'alertTargetArn': 'string',
                'roleArn': 'string'
            }
        },
        'version': 123,
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def describe_stream(streamId=None):
    """
    Gets information about a stream.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stream(
        streamId='string'
    )
    
    
    :type streamId: string
    :param streamId: [REQUIRED]
            The stream ID.
            

    :rtype: dict
    :return: {
        'streamInfo': {
            'streamId': 'string',
            'streamArn': 'string',
            'streamVersion': 123,
            'description': 'string',
            'files': [
                {
                    'fileId': 123,
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'version': 'string'
                    }
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'roleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_thing(thingName=None):
    """
    Gets information about the specified thing.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_thing(
        thingName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing.
            

    :rtype: dict
    :return: {
        'defaultClientId': 'string',
        'thingName': 'string',
        'thingId': 'string',
        'thingArn': 'string',
        'thingTypeName': 'string',
        'attributes': {
            'string': 'string'
        },
        'version': 123,
        'billingGroupName': 'string'
    }
    
    
    """
    pass

def describe_thing_group(thingGroupName=None):
    """
    Describe a thing group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_thing_group(
        thingGroupName='string'
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]
            The name of the thing group.
            

    :rtype: dict
    :return: {
        'thingGroupName': 'string',
        'thingGroupId': 'string',
        'thingGroupArn': 'string',
        'version': 123,
        'thingGroupProperties': {
            'thingGroupDescription': 'string',
            'attributePayload': {
                'attributes': {
                    'string': 'string'
                },
                'merge': True|False
            }
        },
        'thingGroupMetadata': {
            'parentGroupName': 'string',
            'rootToParentThingGroups': [
                {
                    'groupName': 'string',
                    'groupArn': 'string'
                },
            ],
            'creationDate': datetime(2015, 1, 1)
        },
        'indexName': 'string',
        'queryString': 'string',
        'queryVersion': 'string',
        'status': 'ACTIVE'|'BUILDING'|'REBUILDING'
    }
    
    
    """
    pass

def describe_thing_registration_task(taskId=None):
    """
    Describes a bulk thing provisioning task.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_thing_registration_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]
            The task ID.
            

    :rtype: dict
    :return: {
        'taskId': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'templateBody': 'string',
        'inputFileBucket': 'string',
        'inputFileKey': 'string',
        'roleArn': 'string',
        'status': 'InProgress'|'Completed'|'Failed'|'Cancelled'|'Cancelling',
        'message': 'string',
        'successCount': 123,
        'failureCount': 123,
        'percentageProgress': 123
    }
    
    
    """
    pass

def describe_thing_type(thingTypeName=None):
    """
    Gets information about the specified thing type.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_thing_type(
        thingTypeName='string'
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]
            The name of the thing type.
            

    :rtype: dict
    :return: {
        'thingTypeName': 'string',
        'thingTypeId': 'string',
        'thingTypeArn': 'string',
        'thingTypeProperties': {
            'thingTypeDescription': 'string',
            'searchableAttributes': [
                'string',
            ]
        },
        'thingTypeMetadata': {
            'deprecated': True|False,
            'deprecationDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def detach_policy(policyName=None, target=None):
    """
    Detaches a policy from the specified target.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_policy(
        policyName='string',
        target='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy to detach.
            

    :type target: string
    :param target: [REQUIRED]
            The target from which the policy will be detached.
            

    """
    pass

def detach_principal_policy(policyName=None, principal=None):
    """
    Removes the specified policy from the specified certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_principal_policy(
        policyName='string',
        principal='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy to detach.
            

    :type principal: string
    :param principal: [REQUIRED]
            The principal.
            If the principal is a certificate, specify the certificate ARN. If the principal is an Amazon Cognito identity, specify the identity ID.
            

    """
    pass

def detach_security_profile(securityProfileName=None, securityProfileTargetArn=None):
    """
    Disassociates a Device Defender security profile from a thing group or from this account.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_security_profile(
        securityProfileName='string',
        securityProfileTargetArn='string'
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]
            The security profile that is detached.
            

    :type securityProfileTargetArn: string
    :param securityProfileTargetArn: [REQUIRED]
            The ARN of the thing group from which the security profile is detached.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def detach_thing_principal(thingName=None, principal=None):
    """
    Detaches the specified principal from the specified thing.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_thing_principal(
        thingName='string',
        principal='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing.
            

    :type principal: string
    :param principal: [REQUIRED]
            If the principal is a certificate, this value must be ARN of the certificate. If the principal is an Amazon Cognito identity, this value must be the ID of the Amazon Cognito identity.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def disable_topic_rule(ruleName=None):
    """
    Disables the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the rule to disable.
            

    """
    pass

def enable_topic_rule(ruleName=None):
    """
    Enables the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the topic rule to enable.
            

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

def get_effective_policies(principal=None, cognitoIdentityPoolId=None, thingName=None):
    """
    Gets a list of the policies that have an effect on the authorization behavior of the specified device when it connects to the AWS IoT device gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.get_effective_policies(
        principal='string',
        cognitoIdentityPoolId='string',
        thingName='string'
    )
    
    
    :type principal: string
    :param principal: The principal.

    :type cognitoIdentityPoolId: string
    :param cognitoIdentityPoolId: The Cognito identity pool ID.

    :type thingName: string
    :param thingName: The thing name.

    :rtype: dict
    :return: {
        'effectivePolicies': [
            {
                'policyName': 'string',
                'policyArn': 'string',
                'policyDocument': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_indexing_configuration():
    """
    Gets the search configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.get_indexing_configuration()
    
    
    :rtype: dict
    :return: {
        'thingIndexingConfiguration': {
            'thingIndexingMode': 'OFF'|'REGISTRY'|'REGISTRY_AND_SHADOW',
            'thingConnectivityIndexingMode': 'OFF'|'STATUS'
        },
        'thingGroupIndexingConfiguration': {
            'thingGroupIndexingMode': 'OFF'|'ON'
        }
    }
    
    
    :returns: 
    STATUS  Your thing index will contain connectivity status. In order to enable thing connectivity indexing, thingIndexMode must not be set to OFF.
    OFF - Thing connectivity status indexing is disabled.
    
    """
    pass

def get_job_document(jobId=None):
    """
    Gets a job document.
    See also: AWS API Documentation
    
    
    :example: response = client.get_job_document(
        jobId='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique identifier you assigned to this job when it was created.
            

    :rtype: dict
    :return: {
        'document': 'string'
    }
    
    
    """
    pass

def get_logging_options():
    """
    Gets the logging options.
    NOTE: use of this command is not recommended. Use GetV2LoggingOptions instead.
    See also: AWS API Documentation
    
    
    :example: response = client.get_logging_options()
    
    
    :rtype: dict
    :return: {
        'roleArn': 'string',
        'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
    }
    
    
    """
    pass

def get_ota_update(otaUpdateId=None):
    """
    Gets an OTA update.
    See also: AWS API Documentation
    
    
    :example: response = client.get_ota_update(
        otaUpdateId='string'
    )
    
    
    :type otaUpdateId: string
    :param otaUpdateId: [REQUIRED]
            The OTA update ID.
            

    :rtype: dict
    :return: {
        'otaUpdateInfo': {
            'otaUpdateId': 'string',
            'otaUpdateArn': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'description': 'string',
            'targets': [
                'string',
            ],
            'awsJobExecutionsRolloutConfig': {
                'maximumPerMinute': 123
            },
            'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
            'otaUpdateFiles': [
                {
                    'fileName': 'string',
                    'fileVersion': 'string',
                    'fileLocation': {
                        'stream': {
                            'streamId': 'string',
                            'fileId': 123
                        },
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'version': 'string'
                        }
                    },
                    'codeSigning': {
                        'awsSignerJobId': 'string',
                        'startSigningJobParameter': {
                            'signingProfileParameter': {
                                'certificateArn': 'string',
                                'platform': 'string',
                                'certificatePathOnDevice': 'string'
                            },
                            'signingProfileName': 'string',
                            'destination': {
                                's3Destination': {
                                    'bucket': 'string',
                                    'prefix': 'string'
                                }
                            }
                        },
                        'customCodeSigning': {
                            'signature': {
                                'inlineDocument': b'bytes'
                            },
                            'certificateChain': {
                                'certificateName': 'string',
                                'inlineDocument': 'string'
                            },
                            'hashAlgorithm': 'string',
                            'signatureAlgorithm': 'string'
                        }
                    },
                    'attributes': {
                        'string': 'string'
                    }
                },
            ],
            'otaUpdateStatus': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED',
            'awsIotJobId': 'string',
            'awsIotJobArn': 'string',
            'errorInfo': {
                'code': 'string',
                'message': 'string'
            },
            'additionalParameters': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
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

def get_policy(policyName=None):
    """
    Gets information about the specified policy with the policy document of the default version.
    See also: AWS API Documentation
    
    
    :example: response = client.get_policy(
        policyName='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy.
            

    :rtype: dict
    :return: {
        'policyName': 'string',
        'policyArn': 'string',
        'policyDocument': 'string',
        'defaultVersionId': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'generationId': 'string'
    }
    
    
    """
    pass

def get_policy_version(policyName=None, policyVersionId=None):
    """
    Gets information about the specified policy version.
    See also: AWS API Documentation
    
    
    :example: response = client.get_policy_version(
        policyName='string',
        policyVersionId='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy.
            

    :type policyVersionId: string
    :param policyVersionId: [REQUIRED]
            The policy version ID.
            

    :rtype: dict
    :return: {
        'policyArn': 'string',
        'policyName': 'string',
        'policyDocument': 'string',
        'policyVersionId': 'string',
        'isDefaultVersion': True|False,
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'generationId': 'string'
    }
    
    
    """
    pass

def get_registration_code():
    """
    Gets a registration code used to register a CA certificate with AWS IoT.
    See also: AWS API Documentation
    
    
    :example: response = client.get_registration_code()
    
    
    :rtype: dict
    :return: {
        'registrationCode': 'string'
    }
    
    
    """
    pass

def get_topic_rule(ruleName=None):
    """
    Gets information about the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.get_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the rule.
            

    :rtype: dict
    :return: {
        'ruleArn': 'string',
        'rule': {
            'ruleName': 'string',
            'sql': 'string',
            'description': 'string',
            'createdAt': datetime(2015, 1, 1),
            'actions': [
                {
                    'dynamoDB': {
                        'tableName': 'string',
                        'roleArn': 'string',
                        'operation': 'string',
                        'hashKeyField': 'string',
                        'hashKeyValue': 'string',
                        'hashKeyType': 'STRING'|'NUMBER',
                        'rangeKeyField': 'string',
                        'rangeKeyValue': 'string',
                        'rangeKeyType': 'STRING'|'NUMBER',
                        'payloadField': 'string'
                    },
                    'dynamoDBv2': {
                        'roleArn': 'string',
                        'putItem': {
                            'tableName': 'string'
                        }
                    },
                    'lambda': {
                        'functionArn': 'string'
                    },
                    'sns': {
                        'targetArn': 'string',
                        'roleArn': 'string',
                        'messageFormat': 'RAW'|'JSON'
                    },
                    'sqs': {
                        'roleArn': 'string',
                        'queueUrl': 'string',
                        'useBase64': True|False
                    },
                    'kinesis': {
                        'roleArn': 'string',
                        'streamName': 'string',
                        'partitionKey': 'string'
                    },
                    'republish': {
                        'roleArn': 'string',
                        'topic': 'string'
                    },
                    's3': {
                        'roleArn': 'string',
                        'bucketName': 'string',
                        'key': 'string',
                        'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                    },
                    'firehose': {
                        'roleArn': 'string',
                        'deliveryStreamName': 'string',
                        'separator': 'string'
                    },
                    'cloudwatchMetric': {
                        'roleArn': 'string',
                        'metricNamespace': 'string',
                        'metricName': 'string',
                        'metricValue': 'string',
                        'metricUnit': 'string',
                        'metricTimestamp': 'string'
                    },
                    'cloudwatchAlarm': {
                        'roleArn': 'string',
                        'alarmName': 'string',
                        'stateReason': 'string',
                        'stateValue': 'string'
                    },
                    'elasticsearch': {
                        'roleArn': 'string',
                        'endpoint': 'string',
                        'index': 'string',
                        'type': 'string',
                        'id': 'string'
                    },
                    'salesforce': {
                        'token': 'string',
                        'url': 'string'
                    },
                    'iotAnalytics': {
                        'channelArn': 'string',
                        'channelName': 'string',
                        'roleArn': 'string'
                    },
                    'iotEvents': {
                        'inputName': 'string',
                        'messageId': 'string',
                        'roleArn': 'string'
                    },
                    'stepFunctions': {
                        'executionNamePrefix': 'string',
                        'stateMachineName': 'string',
                        'roleArn': 'string'
                    }
                },
            ],
            'ruleDisabled': True|False,
            'awsIotSqlVersion': 'string',
            'errorAction': {
                'dynamoDB': {
                    'tableName': 'string',
                    'roleArn': 'string',
                    'operation': 'string',
                    'hashKeyField': 'string',
                    'hashKeyValue': 'string',
                    'hashKeyType': 'STRING'|'NUMBER',
                    'rangeKeyField': 'string',
                    'rangeKeyValue': 'string',
                    'rangeKeyType': 'STRING'|'NUMBER',
                    'payloadField': 'string'
                },
                'dynamoDBv2': {
                    'roleArn': 'string',
                    'putItem': {
                        'tableName': 'string'
                    }
                },
                'lambda': {
                    'functionArn': 'string'
                },
                'sns': {
                    'targetArn': 'string',
                    'roleArn': 'string',
                    'messageFormat': 'RAW'|'JSON'
                },
                'sqs': {
                    'roleArn': 'string',
                    'queueUrl': 'string',
                    'useBase64': True|False
                },
                'kinesis': {
                    'roleArn': 'string',
                    'streamName': 'string',
                    'partitionKey': 'string'
                },
                'republish': {
                    'roleArn': 'string',
                    'topic': 'string'
                },
                's3': {
                    'roleArn': 'string',
                    'bucketName': 'string',
                    'key': 'string',
                    'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                },
                'firehose': {
                    'roleArn': 'string',
                    'deliveryStreamName': 'string',
                    'separator': 'string'
                },
                'cloudwatchMetric': {
                    'roleArn': 'string',
                    'metricNamespace': 'string',
                    'metricName': 'string',
                    'metricValue': 'string',
                    'metricUnit': 'string',
                    'metricTimestamp': 'string'
                },
                'cloudwatchAlarm': {
                    'roleArn': 'string',
                    'alarmName': 'string',
                    'stateReason': 'string',
                    'stateValue': 'string'
                },
                'elasticsearch': {
                    'roleArn': 'string',
                    'endpoint': 'string',
                    'index': 'string',
                    'type': 'string',
                    'id': 'string'
                },
                'salesforce': {
                    'token': 'string',
                    'url': 'string'
                },
                'iotAnalytics': {
                    'channelArn': 'string',
                    'channelName': 'string',
                    'roleArn': 'string'
                },
                'iotEvents': {
                    'inputName': 'string',
                    'messageId': 'string',
                    'roleArn': 'string'
                },
                'stepFunctions': {
                    'executionNamePrefix': 'string',
                    'stateMachineName': 'string',
                    'roleArn': 'string'
                }
            }
        }
    }
    
    
    """
    pass

def get_v2_logging_options():
    """
    Gets the fine grained logging options.
    See also: AWS API Documentation
    
    
    :example: response = client.get_v2_logging_options()
    
    
    :rtype: dict
    :return: {
        'roleArn': 'string',
        'defaultLogLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED',
        'disableAllLogs': True|False
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

def list_active_violations(thingName=None, securityProfileName=None, nextToken=None, maxResults=None):
    """
    Lists the active violations for a given Device Defender security profile.
    See also: AWS API Documentation
    
    
    :example: response = client.list_active_violations(
        thingName='string',
        securityProfileName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type thingName: string
    :param thingName: The name of the thing whose active violations are listed.

    :type securityProfileName: string
    :param securityProfileName: The name of the Device Defender security profile for which violations are listed.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict
    :return: {
        'activeViolations': [
            {
                'violationId': 'string',
                'thingName': 'string',
                'securityProfileName': 'string',
                'behavior': {
                    'name': 'string',
                    'metric': 'string',
                    'criteria': {
                        'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                        'value': {
                            'count': 123,
                            'cidrs': [
                                'string',
                            ],
                            'ports': [
                                123,
                            ]
                        },
                        'durationSeconds': 123
                    }
                },
                'lastViolationValue': {
                    'count': 123,
                    'cidrs': [
                        'string',
                    ],
                    'ports': [
                        123,
                    ]
                },
                'lastViolationTime': datetime(2015, 1, 1),
                'violationStartTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_attached_policies(target=None, recursive=None, marker=None, pageSize=None):
    """
    Lists the policies attached to the specified thing group.
    See also: AWS API Documentation
    
    
    :example: response = client.list_attached_policies(
        target='string',
        recursive=True|False,
        marker='string',
        pageSize=123
    )
    
    
    :type target: string
    :param target: [REQUIRED]
            The group for which the policies will be listed.
            

    :type recursive: boolean
    :param recursive: When true, recursively list attached policies.

    :type marker: string
    :param marker: The token to retrieve the next set of results.

    :type pageSize: integer
    :param pageSize: The maximum number of results to be returned per request.

    :rtype: dict
    :return: {
        'policies': [
            {
                'policyName': 'string',
                'policyArn': 'string'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_audit_findings(taskId=None, checkName=None, resourceIdentifier=None, maxResults=None, nextToken=None, startTime=None, endTime=None):
    """
    Lists the findings (results) of a Device Defender audit or of the audits performed during a specified time period. (Findings are retained for 180 days.)
    See also: AWS API Documentation
    
    
    :example: response = client.list_audit_findings(
        taskId='string',
        checkName='string',
        resourceIdentifier={
            'deviceCertificateId': 'string',
            'caCertificateId': 'string',
            'cognitoIdentityPoolId': 'string',
            'clientId': 'string',
            'policyVersionIdentifier': {
                'policyName': 'string',
                'policyVersionId': 'string'
            },
            'account': 'string'
        },
        maxResults=123,
        nextToken='string',
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1)
    )
    
    
    :type taskId: string
    :param taskId: A filter to limit results to the audit with the specified ID. You must specify either the taskId or the startTime and endTime, but not both.

    :type checkName: string
    :param checkName: A filter to limit results to the findings for the specified audit check.

    :type resourceIdentifier: dict
    :param resourceIdentifier: Information identifying the non-compliant resource.
            deviceCertificateId (string) --The ID of the certificate attached to the resource.
            caCertificateId (string) --The ID of the CA certificate used to authorize the certificate.
            cognitoIdentityPoolId (string) --The ID of the Cognito Identity Pool.
            clientId (string) --The client ID.
            policyVersionIdentifier (dict) --The version of the policy associated with the resource.
            policyName (string) --The name of the policy.
            policyVersionId (string) --The ID of the version of the policy associated with the resource.
            account (string) --The account with which the resource is associated.
            

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time. The default is 25.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type startTime: datetime
    :param startTime: A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both.

    :type endTime: datetime
    :param endTime: A filter to limit results to those found before the specified time. You must specify either the startTime and endTime or the taskId, but not both.

    :rtype: dict
    :return: {
        'findings': [
            {
                'taskId': 'string',
                'checkName': 'string',
                'taskStartTime': datetime(2015, 1, 1),
                'findingTime': datetime(2015, 1, 1),
                'severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW',
                'nonCompliantResource': {
                    'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS',
                    'resourceIdentifier': {
                        'deviceCertificateId': 'string',
                        'caCertificateId': 'string',
                        'cognitoIdentityPoolId': 'string',
                        'clientId': 'string',
                        'policyVersionIdentifier': {
                            'policyName': 'string',
                            'policyVersionId': 'string'
                        },
                        'account': 'string'
                    },
                    'additionalInfo': {
                        'string': 'string'
                    }
                },
                'relatedResources': [
                    {
                        'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS',
                        'resourceIdentifier': {
                            'deviceCertificateId': 'string',
                            'caCertificateId': 'string',
                            'cognitoIdentityPoolId': 'string',
                            'clientId': 'string',
                            'policyVersionIdentifier': {
                                'policyName': 'string',
                                'policyVersionId': 'string'
                            },
                            'account': 'string'
                        },
                        'additionalInfo': {
                            'string': 'string'
                        }
                    },
                ],
                'reasonForNonCompliance': 'string',
                'reasonForNonComplianceCode': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_audit_tasks(startTime=None, endTime=None, taskType=None, taskStatus=None, nextToken=None, maxResults=None):
    """
    Lists the Device Defender audits that have been performed during a given time period.
    See also: AWS API Documentation
    
    
    :example: response = client.list_audit_tasks(
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        taskType='ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK',
        taskStatus='IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
        nextToken='string',
        maxResults=123
    )
    
    
    :type startTime: datetime
    :param startTime: [REQUIRED]
            The beginning of the time period. Note that audit information is retained for a limited time (180 days). Requesting a start time prior to what is retained results in an 'InvalidRequestException'.
            

    :type endTime: datetime
    :param endTime: [REQUIRED]
            The end of the time period.
            

    :type taskType: string
    :param taskType: A filter to limit the output to the specified type of audit: can be one of 'ON_DEMAND_AUDIT_TASK' or 'SCHEDULED__AUDIT_TASK'.

    :type taskStatus: string
    :param taskStatus: A filter to limit the output to audits with the specified completion status: can be one of 'IN_PROGRESS', 'COMPLETED', 'FAILED' or 'CANCELED'.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time. The default is 25.

    :rtype: dict
    :return: {
        'tasks': [
            {
                'taskId': 'string',
                'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
                'taskType': 'ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_authorizers(pageSize=None, marker=None, ascendingOrder=None, status=None):
    """
    Lists the authorizers registered in your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_authorizers(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False,
        status='ACTIVE'|'INACTIVE'
    )
    
    
    :type pageSize: integer
    :param pageSize: The maximum number of results to return at one time.

    :type marker: string
    :param marker: A marker used to get the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Return the list of authorizers in ascending alphabetical order.

    :type status: string
    :param status: The status of the list authorizers request.

    :rtype: dict
    :return: {
        'authorizers': [
            {
                'authorizerName': 'string',
                'authorizerArn': 'string'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_billing_groups(nextToken=None, maxResults=None, namePrefixFilter=None):
    """
    Lists the billing groups you have created.
    See also: AWS API Documentation
    
    
    :example: response = client.list_billing_groups(
        nextToken='string',
        maxResults=123,
        namePrefixFilter='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return per request.

    :type namePrefixFilter: string
    :param namePrefixFilter: Limit the results to billing groups whose names have the given prefix.

    :rtype: dict
    :return: {
        'billingGroups': [
            {
                'groupName': 'string',
                'groupArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_ca_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists the CA certificates registered for your AWS account.
    The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.
    See also: AWS API Documentation
    
    
    :example: response = client.list_ca_certificates(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Determines the order of the results.

    :rtype: dict
    :return: {
        'certificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists the certificates registered in your AWS account.
    The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.
    See also: AWS API Documentation
    
    
    :example: response = client.list_certificates(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

    :rtype: dict
    :return: {
        'certificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_certificates_by_ca(caCertificateId=None, pageSize=None, marker=None, ascendingOrder=None):
    """
    List the device certificates signed by the specified CA certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.list_certificates_by_ca(
        caCertificateId='string',
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type caCertificateId: string
    :param caCertificateId: [REQUIRED]
            The ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.
            

    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

    :rtype: dict
    :return: {
        'certificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_indices(nextToken=None, maxResults=None):
    """
    Lists the search indices.
    See also: AWS API Documentation
    
    
    :example: response = client.list_indices(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token used to get the next set of results, or null if there are no additional results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict
    :return: {
        'indexNames': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_job_executions_for_job(jobId=None, status=None, maxResults=None, nextToken=None):
    """
    Lists the job executions for a job.
    See also: AWS API Documentation
    
    
    :example: response = client.list_job_executions_for_job(
        jobId='string',
        status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique identifier you assigned to this job when it was created.
            

    :type status: string
    :param status: The status of the job.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per request.

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :rtype: dict
    :return: {
        'executionSummaries': [
            {
                'thingArn': 'string',
                'jobExecutionSummary': {
                    'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                    'queuedAt': datetime(2015, 1, 1),
                    'startedAt': datetime(2015, 1, 1),
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'executionNumber': 123
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_job_executions_for_thing(thingName=None, status=None, maxResults=None, nextToken=None):
    """
    Lists the job executions for the specified thing.
    See also: AWS API Documentation
    
    
    :example: response = client.list_job_executions_for_thing(
        thingName='string',
        status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The thing name.
            

    :type status: string
    :param status: An optional filter that lets you search for jobs that have the specified status.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per request.

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :rtype: dict
    :return: {
        'executionSummaries': [
            {
                'jobId': 'string',
                'jobExecutionSummary': {
                    'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                    'queuedAt': datetime(2015, 1, 1),
                    'startedAt': datetime(2015, 1, 1),
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'executionNumber': 123
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_jobs(status=None, targetSelection=None, maxResults=None, nextToken=None, thingGroupName=None, thingGroupId=None):
    """
    Lists jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.list_jobs(
        status='IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
        targetSelection='CONTINUOUS'|'SNAPSHOT',
        maxResults=123,
        nextToken='string',
        thingGroupName='string',
        thingGroupId='string'
    )
    
    
    :type status: string
    :param status: An optional filter that lets you search for jobs that have the specified status.

    :type targetSelection: string
    :param targetSelection: Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return per request.

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type thingGroupName: string
    :param thingGroupName: A filter that limits the returned jobs to those for the specified group.

    :type thingGroupId: string
    :param thingGroupId: A filter that limits the returned jobs to those for the specified group.

    :rtype: dict
    :return: {
        'jobs': [
            {
                'jobArn': 'string',
                'jobId': 'string',
                'thingGroupId': 'string',
                'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
                'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'completedAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_ota_updates(maxResults=None, nextToken=None, otaUpdateStatus=None):
    """
    Lists OTA updates.
    See also: AWS API Documentation
    
    
    :example: response = client.list_ota_updates(
        maxResults=123,
        nextToken='string',
        otaUpdateStatus='CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type nextToken: string
    :param nextToken: A token used to retrieve the next set of results.

    :type otaUpdateStatus: string
    :param otaUpdateStatus: The OTA update job status.

    :rtype: dict
    :return: {
        'otaUpdates': [
            {
                'otaUpdateId': 'string',
                'otaUpdateArn': 'string',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_outgoing_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists certificates that are being transferred but not yet accepted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_outgoing_certificates(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

    :rtype: dict
    :return: {
        'outgoingCertificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'transferredTo': 'string',
                'transferDate': datetime(2015, 1, 1),
                'transferMessage': 'string',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_policies(marker=None, pageSize=None, ascendingOrder=None):
    """
    Lists your policies.
    See also: AWS API Documentation
    
    
    :example: response = client.list_policies(
        marker='string',
        pageSize=123,
        ascendingOrder=True|False
    )
    
    
    :type marker: string
    :param marker: The marker for the next set of results.

    :type pageSize: integer
    :param pageSize: The result page size.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If true, the results are returned in ascending creation order.

    :rtype: dict
    :return: {
        'policies': [
            {
                'policyName': 'string',
                'policyArn': 'string'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_policy_principals(policyName=None, marker=None, pageSize=None, ascendingOrder=None):
    """
    Lists the principals associated with the specified policy.
    See also: AWS API Documentation
    
    
    :example: response = client.list_policy_principals(
        policyName='string',
        marker='string',
        pageSize=123,
        ascendingOrder=True|False
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type marker: string
    :param marker: The marker for the next set of results.

    :type pageSize: integer
    :param pageSize: The result page size.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If true, the results are returned in ascending creation order.

    :rtype: dict
    :return: {
        'principals': [
            'string',
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_policy_versions(policyName=None):
    """
    Lists the versions of the specified policy and identifies the default version.
    See also: AWS API Documentation
    
    
    :example: response = client.list_policy_versions(
        policyName='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :rtype: dict
    :return: {
        'policyVersions': [
            {
                'versionId': 'string',
                'isDefaultVersion': True|False,
                'createDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def list_principal_policies(principal=None, marker=None, pageSize=None, ascendingOrder=None):
    """
    Lists the policies attached to the specified principal. If you use an Cognito identity, the ID must be in AmazonCognito Identity format .
    See also: AWS API Documentation
    
    
    :example: response = client.list_principal_policies(
        principal='string',
        marker='string',
        pageSize=123,
        ascendingOrder=True|False
    )
    
    
    :type principal: string
    :param principal: [REQUIRED]
            The principal.
            

    :type marker: string
    :param marker: The marker for the next set of results.

    :type pageSize: integer
    :param pageSize: The result page size.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If true, results are returned in ascending creation order.

    :rtype: dict
    :return: {
        'policies': [
            {
                'policyName': 'string',
                'policyArn': 'string'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_principal_things(nextToken=None, maxResults=None, principal=None):
    """
    Lists the things associated with the specified principal.
    See also: AWS API Documentation
    
    
    :example: response = client.list_principal_things(
        nextToken='string',
        maxResults=123,
        principal='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this operation.

    :type principal: string
    :param principal: [REQUIRED]
            The principal.
            

    :rtype: dict
    :return: {
        'things': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_role_aliases(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists the role aliases registered in your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_role_aliases(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The maximum number of results to return at one time.

    :type marker: string
    :param marker: A marker used to get the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Return the list of role aliases in ascending alphabetical order.

    :rtype: dict
    :return: {
        'roleAliases': [
            'string',
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_scheduled_audits(nextToken=None, maxResults=None):
    """
    Lists all of your scheduled audits.
    See also: AWS API Documentation
    
    
    :example: response = client.list_scheduled_audits(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time. The default is 25.

    :rtype: dict
    :return: {
        'scheduledAudits': [
            {
                'scheduledAuditName': 'string',
                'scheduledAuditArn': 'string',
                'frequency': 'DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
                'dayOfMonth': 'string',
                'dayOfWeek': 'SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_security_profiles(nextToken=None, maxResults=None):
    """
    Lists the Device Defender security profiles you have created. You can use filters to list only those security profiles associated with a thing group or only those associated with your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_security_profiles(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict
    :return: {
        'securityProfileIdentifiers': [
            {
                'name': 'string',
                'arn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_security_profiles_for_target(nextToken=None, maxResults=None, recursive=None, securityProfileTargetArn=None):
    """
    Lists the Device Defender security profiles attached to a target (thing group).
    See also: AWS API Documentation
    
    
    :example: response = client.list_security_profiles_for_target(
        nextToken='string',
        maxResults=123,
        recursive=True|False,
        securityProfileTargetArn='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type recursive: boolean
    :param recursive: If true, return child groups as well.

    :type securityProfileTargetArn: string
    :param securityProfileTargetArn: [REQUIRED]
            The ARN of the target (thing group) whose attached security profiles you want to get.
            

    :rtype: dict
    :return: {
        'securityProfileTargetMappings': [
            {
                'securityProfileIdentifier': {
                    'name': 'string',
                    'arn': 'string'
                },
                'target': {
                    'arn': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_streams(maxResults=None, nextToken=None, ascendingOrder=None):
    """
    Lists all of the streams in your AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_streams(
        maxResults=123,
        nextToken='string',
        ascendingOrder=True|False
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return at a time.

    :type nextToken: string
    :param nextToken: A token used to get the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Set to true to return the list of streams in ascending order.

    :rtype: dict
    :return: {
        'streams': [
            {
                'streamId': 'string',
                'streamArn': 'string',
                'streamVersion': 123,
                'description': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_tags_for_resource(resourceArn=None, nextToken=None):
    """
    Lists the tags (metadata) you have assigned to the resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string',
        nextToken='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The ARN of the resource.
            

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :rtype: dict
    :return: {
        'tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_targets_for_policy(policyName=None, marker=None, pageSize=None):
    """
    List targets for the specified policy.
    See also: AWS API Documentation
    
    
    :example: response = client.list_targets_for_policy(
        policyName='string',
        marker='string',
        pageSize=123
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type marker: string
    :param marker: A marker used to get the next set of results.

    :type pageSize: integer
    :param pageSize: The maximum number of results to return at one time.

    :rtype: dict
    :return: {
        'targets': [
            'string',
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_targets_for_security_profile(securityProfileName=None, nextToken=None, maxResults=None):
    """
    Lists the targets (thing groups) associated with a given Device Defender security profile.
    See also: AWS API Documentation
    
    
    :example: response = client.list_targets_for_security_profile(
        securityProfileName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]
            The security profile.
            

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict
    :return: {
        'securityProfileTargets': [
            {
                'arn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_thing_groups(nextToken=None, maxResults=None, parentGroup=None, namePrefixFilter=None, recursive=None):
    """
    List the thing groups in your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_thing_groups(
        nextToken='string',
        maxResults=123,
        parentGroup='string',
        namePrefixFilter='string',
        recursive=True|False
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type parentGroup: string
    :param parentGroup: A filter that limits the results to those with the specified parent group.

    :type namePrefixFilter: string
    :param namePrefixFilter: A filter that limits the results to those with the specified name prefix.

    :type recursive: boolean
    :param recursive: If true, return child groups as well.

    :rtype: dict
    :return: {
        'thingGroups': [
            {
                'groupName': 'string',
                'groupArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_thing_groups_for_thing(thingName=None, nextToken=None, maxResults=None):
    """
    List the thing groups to which the specified thing belongs.
    See also: AWS API Documentation
    
    
    :example: response = client.list_thing_groups_for_thing(
        thingName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The thing name.
            

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict
    :return: {
        'thingGroups': [
            {
                'groupName': 'string',
                'groupArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_thing_principals(thingName=None):
    """
    Lists the principals associated with the specified thing.
    See also: AWS API Documentation
    
    
    :example: response = client.list_thing_principals(
        thingName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing.
            

    :rtype: dict
    :return: {
        'principals': [
            'string',
        ]
    }
    
    
    """
    pass

def list_thing_registration_task_reports(taskId=None, reportType=None, nextToken=None, maxResults=None):
    """
    Information about the thing registration tasks.
    See also: AWS API Documentation
    
    
    :example: response = client.list_thing_registration_task_reports(
        taskId='string',
        reportType='ERRORS'|'RESULTS',
        nextToken='string',
        maxResults=123
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]
            The id of the task.
            

    :type reportType: string
    :param reportType: [REQUIRED]
            The type of task report.
            

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return per request.

    :rtype: dict
    :return: {
        'resourceLinks': [
            'string',
        ],
        'reportType': 'ERRORS'|'RESULTS',
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_thing_registration_tasks(nextToken=None, maxResults=None, status=None):
    """
    List bulk thing provisioning tasks.
    See also: AWS API Documentation
    
    
    :example: response = client.list_thing_registration_tasks(
        nextToken='string',
        maxResults=123,
        status='InProgress'|'Completed'|'Failed'|'Cancelled'|'Cancelling'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type status: string
    :param status: The status of the bulk thing provisioning task.

    :rtype: dict
    :return: {
        'taskIds': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_thing_types(nextToken=None, maxResults=None, thingTypeName=None):
    """
    Lists the existing thing types.
    See also: AWS API Documentation
    
    
    :example: response = client.list_thing_types(
        nextToken='string',
        maxResults=123,
        thingTypeName='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this operation.

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type.

    :rtype: dict
    :return: {
        'thingTypes': [
            {
                'thingTypeName': 'string',
                'thingTypeArn': 'string',
                'thingTypeProperties': {
                    'thingTypeDescription': 'string',
                    'searchableAttributes': [
                        'string',
                    ]
                },
                'thingTypeMetadata': {
                    'deprecated': True|False,
                    'deprecationDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1)
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_things(nextToken=None, maxResults=None, attributeName=None, attributeValue=None, thingTypeName=None):
    """
    Lists your things. Use the attributeName and attributeValue parameters to filter your things. For example, calling ListThings with attributeName=Color and attributeValue=Red retrieves all things in the registry that contain an attribute Color with the value Red .
    See also: AWS API Documentation
    
    
    :example: response = client.list_things(
        nextToken='string',
        maxResults=123,
        attributeName='string',
        attributeValue='string',
        thingTypeName='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this operation.

    :type attributeName: string
    :param attributeName: The attribute name used to search for things.

    :type attributeValue: string
    :param attributeValue: The attribute value used to search for things.

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type used to search for things.

    :rtype: dict
    :return: {
        'things': [
            {
                'thingName': 'string',
                'thingTypeName': 'string',
                'thingArn': 'string',
                'attributes': {
                    'string': 'string'
                },
                'version': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_things_in_billing_group(billingGroupName=None, nextToken=None, maxResults=None):
    """
    Lists the things you have added to the given billing group.
    See also: AWS API Documentation
    
    
    :example: response = client.list_things_in_billing_group(
        billingGroupName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: [REQUIRED]
            The name of the billing group.
            

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return per request.

    :rtype: dict
    :return: {
        'things': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_things_in_thing_group(thingGroupName=None, recursive=None, nextToken=None, maxResults=None):
    """
    Lists the things in the specified group.
    See also: AWS API Documentation
    
    
    :example: response = client.list_things_in_thing_group(
        thingGroupName='string',
        recursive=True|False,
        nextToken='string',
        maxResults=123
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]
            The thing group name.
            

    :type recursive: boolean
    :param recursive: When true, list things in this thing group and in all child groups as well.

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict
    :return: {
        'things': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_topic_rules(topic=None, maxResults=None, nextToken=None, ruleDisabled=None):
    """
    Lists the rules for the specific topic.
    See also: AWS API Documentation
    
    
    :example: response = client.list_topic_rules(
        topic='string',
        maxResults=123,
        nextToken='string',
        ruleDisabled=True|False
    )
    
    
    :type topic: string
    :param topic: The topic.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return.

    :type nextToken: string
    :param nextToken: A token used to retrieve the next value.

    :type ruleDisabled: boolean
    :param ruleDisabled: Specifies whether the rule is disabled.

    :rtype: dict
    :return: {
        'rules': [
            {
                'ruleArn': 'string',
                'ruleName': 'string',
                'topicPattern': 'string',
                'createdAt': datetime(2015, 1, 1),
                'ruleDisabled': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_v2_logging_levels(targetType=None, nextToken=None, maxResults=None):
    """
    Lists logging levels.
    See also: AWS API Documentation
    
    
    :example: response = client.list_v2_logging_levels(
        targetType='DEFAULT'|'THING_GROUP',
        nextToken='string',
        maxResults=123
    )
    
    
    :type targetType: string
    :param targetType: The type of resource for which you are configuring logging. Must be THING_Group .

    :type nextToken: string
    :param nextToken: The token used to get the next set of results, or null if there are no additional results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict
    :return: {
        'logTargetConfigurations': [
            {
                'logTarget': {
                    'targetType': 'DEFAULT'|'THING_GROUP',
                    'targetName': 'string'
                },
                'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_violation_events(startTime=None, endTime=None, thingName=None, securityProfileName=None, nextToken=None, maxResults=None):
    """
    Lists the Device Defender security profile violations discovered during the given time period. You can use filters to limit the results to those alerts issued for a particular security profile, behavior or thing (device).
    See also: AWS API Documentation
    
    
    :example: response = client.list_violation_events(
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        thingName='string',
        securityProfileName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type startTime: datetime
    :param startTime: [REQUIRED]
            The start time for the alerts to be listed.
            

    :type endTime: datetime
    :param endTime: [REQUIRED]
            The end time for the alerts to be listed.
            

    :type thingName: string
    :param thingName: A filter to limit results to those alerts caused by the specified thing.

    :type securityProfileName: string
    :param securityProfileName: A filter to limit results to those alerts generated by the specified security profile.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict
    :return: {
        'violationEvents': [
            {
                'violationId': 'string',
                'thingName': 'string',
                'securityProfileName': 'string',
                'behavior': {
                    'name': 'string',
                    'metric': 'string',
                    'criteria': {
                        'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                        'value': {
                            'count': 123,
                            'cidrs': [
                                'string',
                            ],
                            'ports': [
                                123,
                            ]
                        },
                        'durationSeconds': 123
                    }
                },
                'metricValue': {
                    'count': 123,
                    'cidrs': [
                        'string',
                    ],
                    'ports': [
                        123,
                    ]
                },
                'violationEventType': 'in-alarm'|'alarm-cleared'|'alarm-invalidated',
                'violationEventTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def register_ca_certificate(caCertificate=None, verificationCertificate=None, setAsActive=None, allowAutoRegistration=None, registrationConfig=None):
    """
    Registers a CA certificate with AWS IoT. This CA certificate can then be used to sign device certificates, which can be then registered with AWS IoT. You can register up to 10 CA certificates per AWS account that have the same subject field. This enables you to have up to 10 certificate authorities sign your device certificates. If you have more than one CA certificate registered, make sure you pass the CA certificate when you register your device certificates with the RegisterCertificate API.
    See also: AWS API Documentation
    
    
    :example: response = client.register_ca_certificate(
        caCertificate='string',
        verificationCertificate='string',
        setAsActive=True|False,
        allowAutoRegistration=True|False,
        registrationConfig={
            'templateBody': 'string',
            'roleArn': 'string'
        }
    )
    
    
    :type caCertificate: string
    :param caCertificate: [REQUIRED]
            The CA certificate.
            

    :type verificationCertificate: string
    :param verificationCertificate: [REQUIRED]
            The private key verification certificate.
            

    :type setAsActive: boolean
    :param setAsActive: A boolean value that specifies if the CA certificate is set to active.

    :type allowAutoRegistration: boolean
    :param allowAutoRegistration: Allows this CA certificate to be used for auto registration of device certificates.

    :type registrationConfig: dict
    :param registrationConfig: Information about the registration configuration.
            templateBody (string) --The template body.
            roleArn (string) --The ARN of the role.
            

    :rtype: dict
    :return: {
        'certificateArn': 'string',
        'certificateId': 'string'
    }
    
    
    """
    pass

def register_certificate(certificatePem=None, caCertificatePem=None, setAsActive=None, status=None):
    """
    Registers a device certificate with AWS IoT. If you have more than one CA certificate that has the same subject field, you must specify the CA certificate that was used to sign the device certificate being registered.
    See also: AWS API Documentation
    
    
    :example: response = client.register_certificate(
        certificatePem='string',
        caCertificatePem='string',
        setAsActive=True|False,
        status='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
    )
    
    
    :type certificatePem: string
    :param certificatePem: [REQUIRED]
            The certificate data, in PEM format.
            

    :type caCertificatePem: string
    :param caCertificatePem: The CA certificate used to sign the device certificate being registered.

    :type setAsActive: boolean
    :param setAsActive: A boolean value that specifies if the CA certificate is set to active.

    :type status: string
    :param status: The status of the register certificate request.

    :rtype: dict
    :return: {
        'certificateArn': 'string',
        'certificateId': 'string'
    }
    
    
    """
    pass

def register_thing(templateBody=None, parameters=None):
    """
    Provisions a thing.
    See also: AWS API Documentation
    
    
    :example: response = client.register_thing(
        templateBody='string',
        parameters={
            'string': 'string'
        }
    )
    
    
    :type templateBody: string
    :param templateBody: [REQUIRED]
            The provisioning template. See Programmatic Provisioning for more information.
            

    :type parameters: dict
    :param parameters: The parameters for provisioning a thing. See Programmatic Provisioning for more information.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'certificatePem': 'string',
        'resourceArns': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def reject_certificate_transfer(certificateId=None, rejectReason=None):
    """
    Rejects a pending certificate transfer. After AWS IoT rejects a certificate transfer, the certificate status changes from PENDING_TRANSFER to INACTIVE .
    To check for pending certificate transfers, call  ListCertificates to enumerate your certificates.
    This operation can only be called by the transfer destination. After it is called, the certificate will be returned to the source's account in the INACTIVE state.
    See also: AWS API Documentation
    
    
    :example: response = client.reject_certificate_transfer(
        certificateId='string',
        rejectReason='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
            

    :type rejectReason: string
    :param rejectReason: The reason the certificate transfer was rejected.

    """
    pass

def remove_thing_from_billing_group(billingGroupName=None, billingGroupArn=None, thingName=None, thingArn=None):
    """
    Removes the given thing from the billing group.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_thing_from_billing_group(
        billingGroupName='string',
        billingGroupArn='string',
        thingName='string',
        thingArn='string'
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: The name of the billing group.

    :type billingGroupArn: string
    :param billingGroupArn: The ARN of the billing group.

    :type thingName: string
    :param thingName: The name of the thing to be removed from the billing group.

    :type thingArn: string
    :param thingArn: The ARN of the thing to be removed from the billing group.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def remove_thing_from_thing_group(thingGroupName=None, thingGroupArn=None, thingName=None, thingArn=None):
    """
    Remove the specified thing from the specified group.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_thing_from_thing_group(
        thingGroupName='string',
        thingGroupArn='string',
        thingName='string',
        thingArn='string'
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: The group name.

    :type thingGroupArn: string
    :param thingGroupArn: The group ARN.

    :type thingName: string
    :param thingName: The name of the thing to remove from the group.

    :type thingArn: string
    :param thingArn: The ARN of the thing to remove from the group.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def replace_topic_rule(ruleName=None, topicRulePayload=None):
    """
    Replaces the rule. You must specify all parameters for the new rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.replace_topic_rule(
        ruleName='string',
        topicRulePayload={
            'sql': 'string',
            'description': 'string',
            'actions': [
                {
                    'dynamoDB': {
                        'tableName': 'string',
                        'roleArn': 'string',
                        'operation': 'string',
                        'hashKeyField': 'string',
                        'hashKeyValue': 'string',
                        'hashKeyType': 'STRING'|'NUMBER',
                        'rangeKeyField': 'string',
                        'rangeKeyValue': 'string',
                        'rangeKeyType': 'STRING'|'NUMBER',
                        'payloadField': 'string'
                    },
                    'dynamoDBv2': {
                        'roleArn': 'string',
                        'putItem': {
                            'tableName': 'string'
                        }
                    },
                    'lambda': {
                        'functionArn': 'string'
                    },
                    'sns': {
                        'targetArn': 'string',
                        'roleArn': 'string',
                        'messageFormat': 'RAW'|'JSON'
                    },
                    'sqs': {
                        'roleArn': 'string',
                        'queueUrl': 'string',
                        'useBase64': True|False
                    },
                    'kinesis': {
                        'roleArn': 'string',
                        'streamName': 'string',
                        'partitionKey': 'string'
                    },
                    'republish': {
                        'roleArn': 'string',
                        'topic': 'string'
                    },
                    's3': {
                        'roleArn': 'string',
                        'bucketName': 'string',
                        'key': 'string',
                        'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                    },
                    'firehose': {
                        'roleArn': 'string',
                        'deliveryStreamName': 'string',
                        'separator': 'string'
                    },
                    'cloudwatchMetric': {
                        'roleArn': 'string',
                        'metricNamespace': 'string',
                        'metricName': 'string',
                        'metricValue': 'string',
                        'metricUnit': 'string',
                        'metricTimestamp': 'string'
                    },
                    'cloudwatchAlarm': {
                        'roleArn': 'string',
                        'alarmName': 'string',
                        'stateReason': 'string',
                        'stateValue': 'string'
                    },
                    'elasticsearch': {
                        'roleArn': 'string',
                        'endpoint': 'string',
                        'index': 'string',
                        'type': 'string',
                        'id': 'string'
                    },
                    'salesforce': {
                        'token': 'string',
                        'url': 'string'
                    },
                    'iotAnalytics': {
                        'channelArn': 'string',
                        'channelName': 'string',
                        'roleArn': 'string'
                    },
                    'iotEvents': {
                        'inputName': 'string',
                        'messageId': 'string',
                        'roleArn': 'string'
                    },
                    'stepFunctions': {
                        'executionNamePrefix': 'string',
                        'stateMachineName': 'string',
                        'roleArn': 'string'
                    }
                },
            ],
            'ruleDisabled': True|False,
            'awsIotSqlVersion': 'string',
            'errorAction': {
                'dynamoDB': {
                    'tableName': 'string',
                    'roleArn': 'string',
                    'operation': 'string',
                    'hashKeyField': 'string',
                    'hashKeyValue': 'string',
                    'hashKeyType': 'STRING'|'NUMBER',
                    'rangeKeyField': 'string',
                    'rangeKeyValue': 'string',
                    'rangeKeyType': 'STRING'|'NUMBER',
                    'payloadField': 'string'
                },
                'dynamoDBv2': {
                    'roleArn': 'string',
                    'putItem': {
                        'tableName': 'string'
                    }
                },
                'lambda': {
                    'functionArn': 'string'
                },
                'sns': {
                    'targetArn': 'string',
                    'roleArn': 'string',
                    'messageFormat': 'RAW'|'JSON'
                },
                'sqs': {
                    'roleArn': 'string',
                    'queueUrl': 'string',
                    'useBase64': True|False
                },
                'kinesis': {
                    'roleArn': 'string',
                    'streamName': 'string',
                    'partitionKey': 'string'
                },
                'republish': {
                    'roleArn': 'string',
                    'topic': 'string'
                },
                's3': {
                    'roleArn': 'string',
                    'bucketName': 'string',
                    'key': 'string',
                    'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                },
                'firehose': {
                    'roleArn': 'string',
                    'deliveryStreamName': 'string',
                    'separator': 'string'
                },
                'cloudwatchMetric': {
                    'roleArn': 'string',
                    'metricNamespace': 'string',
                    'metricName': 'string',
                    'metricValue': 'string',
                    'metricUnit': 'string',
                    'metricTimestamp': 'string'
                },
                'cloudwatchAlarm': {
                    'roleArn': 'string',
                    'alarmName': 'string',
                    'stateReason': 'string',
                    'stateValue': 'string'
                },
                'elasticsearch': {
                    'roleArn': 'string',
                    'endpoint': 'string',
                    'index': 'string',
                    'type': 'string',
                    'id': 'string'
                },
                'salesforce': {
                    'token': 'string',
                    'url': 'string'
                },
                'iotAnalytics': {
                    'channelArn': 'string',
                    'channelName': 'string',
                    'roleArn': 'string'
                },
                'iotEvents': {
                    'inputName': 'string',
                    'messageId': 'string',
                    'roleArn': 'string'
                },
                'stepFunctions': {
                    'executionNamePrefix': 'string',
                    'stateMachineName': 'string',
                    'roleArn': 'string'
                }
            }
        }
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the rule.
            

    :type topicRulePayload: dict
    :param topicRulePayload: [REQUIRED]
            The rule payload.
            sql (string) -- [REQUIRED]The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference in the AWS IoT Developer Guide .
            description (string) --The description of the rule.
            actions (list) -- [REQUIRED]The actions associated with the rule.
            (dict) --Describes the actions associated with a rule.
            dynamoDB (dict) --Write to a DynamoDB table.
            tableName (string) -- [REQUIRED]The name of the DynamoDB table.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.
            operation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .
            hashKeyField (string) -- [REQUIRED]The hash key name.
            hashKeyValue (string) -- [REQUIRED]The hash key value.
            hashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'
            rangeKeyField (string) --The range key name.
            rangeKeyValue (string) --The range key value.
            rangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'
            payloadField (string) --The action payload. This name can be customized.
            dynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
            roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.
            putItem (dict) --Specifies the DynamoDB table to which the message data will be written. For example:
            { 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }
            Each attribute in the message payload will be written to a separate column in the DynamoDB database.
            tableName (string) -- [REQUIRED]The table where the message data will be written
            
            lambda (dict) --Invoke a Lambda function.
            functionArn (string) -- [REQUIRED]The ARN of the Lambda function.
            sns (dict) --Publish to an Amazon SNS topic.
            targetArn (string) -- [REQUIRED]The ARN of the SNS topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            messageFormat (string) --(Optional) The message format of the message to publish. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see http://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.
            sqs (dict) --Publish to an Amazon SQS queue.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            queueUrl (string) -- [REQUIRED]The URL of the Amazon SQS queue.
            useBase64 (boolean) --Specifies whether to use Base64 encoding.
            kinesis (dict) --Write data to an Amazon Kinesis stream.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the Amazon Kinesis stream.
            streamName (string) -- [REQUIRED]The name of the Amazon Kinesis stream.
            partitionKey (string) --The partition key.
            republish (dict) --Publish to another MQTT topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            topic (string) -- [REQUIRED]The name of the MQTT topic.
            s3 (dict) --Write to an Amazon S3 bucket.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            bucketName (string) -- [REQUIRED]The Amazon S3 bucket.
            key (string) -- [REQUIRED]The object key.
            cannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .
            firehose (dict) --Write to an Amazon Kinesis Firehose stream.
            roleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehose stream.
            deliveryStreamName (string) -- [REQUIRED]The delivery stream name.
            separator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: 'n' (newline), 't' (tab), 'rn' (Windows newline), ',' (comma).
            cloudwatchMetric (dict) --Capture a CloudWatch metric.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch metric.
            metricNamespace (string) -- [REQUIRED]The CloudWatch metric namespace name.
            metricName (string) -- [REQUIRED]The CloudWatch metric name.
            metricValue (string) -- [REQUIRED]The CloudWatch metric value.
            metricUnit (string) -- [REQUIRED]The metric unit supported by CloudWatch.
            metricTimestamp (string) --An optional Unix timestamp .
            cloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch alarm.
            alarmName (string) -- [REQUIRED]The CloudWatch alarm name.
            stateReason (string) -- [REQUIRED]The reason for the alarm change.
            stateValue (string) -- [REQUIRED]The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
            elasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.
            roleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.
            endpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.
            index (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.
            type (string) -- [REQUIRED]The type of document you are storing.
            id (string) -- [REQUIRED]The unique identifier for the document you are storing.
            salesforce (dict) --Send a message to a Salesforce IoT Cloud Input Stream.
            token (string) -- [REQUIRED]The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
            url (string) -- [REQUIRED]The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
            iotAnalytics (dict) --Sends message data to an AWS IoT Analytics channel.
            channelArn (string) --(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
            channelName (string) --The name of the IoT Analytics channel to which message data will be sent.
            roleArn (string) --The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
            iotEvents (dict) --Sends an input to an AWS IoT Events detector.
            inputName (string) -- [REQUIRED]The name of the AWS IoT Events input.
            messageId (string) --[Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ('Action':'iotevents:BatchPutMessage').
            stepFunctions (dict) --Starts execution of a Step Functions state machine.
            executionNamePrefix (string) --(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
            stateMachineName (string) -- [REQUIRED]The name of the Step Functions state machine whose execution will be started.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants IoT permission to start execution of a state machine ('Action':'states:StartExecution').
            
            ruleDisabled (boolean) --Specifies whether the rule is disabled.
            awsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.
            errorAction (dict) --The action to take when an error occurs.
            dynamoDB (dict) --Write to a DynamoDB table.
            tableName (string) -- [REQUIRED]The name of the DynamoDB table.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.
            operation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .
            hashKeyField (string) -- [REQUIRED]The hash key name.
            hashKeyValue (string) -- [REQUIRED]The hash key value.
            hashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'
            rangeKeyField (string) --The range key name.
            rangeKeyValue (string) --The range key value.
            rangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'
            payloadField (string) --The action payload. This name can be customized.
            dynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
            roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.
            putItem (dict) --Specifies the DynamoDB table to which the message data will be written. For example:
            { 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }
            Each attribute in the message payload will be written to a separate column in the DynamoDB database.
            tableName (string) -- [REQUIRED]The table where the message data will be written
            
            lambda (dict) --Invoke a Lambda function.
            functionArn (string) -- [REQUIRED]The ARN of the Lambda function.
            sns (dict) --Publish to an Amazon SNS topic.
            targetArn (string) -- [REQUIRED]The ARN of the SNS topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            messageFormat (string) --(Optional) The message format of the message to publish. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see http://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.
            sqs (dict) --Publish to an Amazon SQS queue.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            queueUrl (string) -- [REQUIRED]The URL of the Amazon SQS queue.
            useBase64 (boolean) --Specifies whether to use Base64 encoding.
            kinesis (dict) --Write data to an Amazon Kinesis stream.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the Amazon Kinesis stream.
            streamName (string) -- [REQUIRED]The name of the Amazon Kinesis stream.
            partitionKey (string) --The partition key.
            republish (dict) --Publish to another MQTT topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            topic (string) -- [REQUIRED]The name of the MQTT topic.
            s3 (dict) --Write to an Amazon S3 bucket.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            bucketName (string) -- [REQUIRED]The Amazon S3 bucket.
            key (string) -- [REQUIRED]The object key.
            cannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .
            firehose (dict) --Write to an Amazon Kinesis Firehose stream.
            roleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehose stream.
            deliveryStreamName (string) -- [REQUIRED]The delivery stream name.
            separator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: 'n' (newline), 't' (tab), 'rn' (Windows newline), ',' (comma).
            cloudwatchMetric (dict) --Capture a CloudWatch metric.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch metric.
            metricNamespace (string) -- [REQUIRED]The CloudWatch metric namespace name.
            metricName (string) -- [REQUIRED]The CloudWatch metric name.
            metricValue (string) -- [REQUIRED]The CloudWatch metric value.
            metricUnit (string) -- [REQUIRED]The metric unit supported by CloudWatch.
            metricTimestamp (string) --An optional Unix timestamp .
            cloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch alarm.
            alarmName (string) -- [REQUIRED]The CloudWatch alarm name.
            stateReason (string) -- [REQUIRED]The reason for the alarm change.
            stateValue (string) -- [REQUIRED]The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
            elasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.
            roleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.
            endpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.
            index (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.
            type (string) -- [REQUIRED]The type of document you are storing.
            id (string) -- [REQUIRED]The unique identifier for the document you are storing.
            salesforce (dict) --Send a message to a Salesforce IoT Cloud Input Stream.
            token (string) -- [REQUIRED]The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
            url (string) -- [REQUIRED]The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
            iotAnalytics (dict) --Sends message data to an AWS IoT Analytics channel.
            channelArn (string) --(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
            channelName (string) --The name of the IoT Analytics channel to which message data will be sent.
            roleArn (string) --The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
            iotEvents (dict) --Sends an input to an AWS IoT Events detector.
            inputName (string) -- [REQUIRED]The name of the AWS IoT Events input.
            messageId (string) --[Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ('Action':'iotevents:BatchPutMessage').
            stepFunctions (dict) --Starts execution of a Step Functions state machine.
            executionNamePrefix (string) --(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
            stateMachineName (string) -- [REQUIRED]The name of the Step Functions state machine whose execution will be started.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants IoT permission to start execution of a state machine ('Action':'states:StartExecution').
            
            

    """
    pass

def search_index(indexName=None, queryString=None, nextToken=None, maxResults=None, queryVersion=None):
    """
    The query search index.
    See also: AWS API Documentation
    
    
    :example: response = client.search_index(
        indexName='string',
        queryString='string',
        nextToken='string',
        maxResults=123,
        queryVersion='string'
    )
    
    
    :type indexName: string
    :param indexName: The search index name.

    :type queryString: string
    :param queryString: [REQUIRED]
            The search query string.
            

    :type nextToken: string
    :param nextToken: The token used to get the next set of results, or null if there are no additional results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type queryVersion: string
    :param queryVersion: The query version.

    :rtype: dict
    :return: {
        'nextToken': 'string',
        'things': [
            {
                'thingName': 'string',
                'thingId': 'string',
                'thingTypeName': 'string',
                'thingGroupNames': [
                    'string',
                ],
                'attributes': {
                    'string': 'string'
                },
                'shadow': 'string',
                'connectivity': {
                    'connected': True|False,
                    'timestamp': 123
                }
            },
        ],
        'thingGroups': [
            {
                'thingGroupName': 'string',
                'thingGroupId': 'string',
                'thingGroupDescription': 'string',
                'attributes': {
                    'string': 'string'
                },
                'parentGroupNames': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def set_default_authorizer(authorizerName=None):
    """
    Sets the default authorizer. This will be used if a websocket connection is made without specifying an authorizer.
    See also: AWS API Documentation
    
    
    :example: response = client.set_default_authorizer(
        authorizerName='string'
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]
            The authorizer name.
            

    :rtype: dict
    :return: {
        'authorizerName': 'string',
        'authorizerArn': 'string'
    }
    
    
    """
    pass

def set_default_policy_version(policyName=None, policyVersionId=None):
    """
    Sets the specified version of the specified policy as the policy's default (operative) version. This action affects all certificates to which the policy is attached. To list the principals the policy is attached to, use the ListPrincipalPolicy API.
    See also: AWS API Documentation
    
    
    :example: response = client.set_default_policy_version(
        policyName='string',
        policyVersionId='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type policyVersionId: string
    :param policyVersionId: [REQUIRED]
            The policy version ID.
            

    """
    pass

def set_logging_options(loggingOptionsPayload=None):
    """
    Sets the logging options.
    NOTE: use of this command is not recommended. Use SetV2LoggingOptions instead.
    See also: AWS API Documentation
    
    
    :example: response = client.set_logging_options(
        loggingOptionsPayload={
            'roleArn': 'string',
            'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
        }
    )
    
    
    :type loggingOptionsPayload: dict
    :param loggingOptionsPayload: [REQUIRED]
            The logging options payload.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            logLevel (string) --The log level.
            

    """
    pass

def set_v2_logging_level(logTarget=None, logLevel=None):
    """
    Sets the logging level.
    See also: AWS API Documentation
    
    
    :example: response = client.set_v2_logging_level(
        logTarget={
            'targetType': 'DEFAULT'|'THING_GROUP',
            'targetName': 'string'
        },
        logLevel='DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
    )
    
    
    :type logTarget: dict
    :param logTarget: [REQUIRED]
            The log target.
            targetType (string) -- [REQUIRED]The target type.
            targetName (string) --The target name.
            

    :type logLevel: string
    :param logLevel: [REQUIRED]
            The log level.
            

    """
    pass

def set_v2_logging_options(roleArn=None, defaultLogLevel=None, disableAllLogs=None):
    """
    Sets the logging options for the V2 logging service.
    See also: AWS API Documentation
    
    
    :example: response = client.set_v2_logging_options(
        roleArn='string',
        defaultLogLevel='DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED',
        disableAllLogs=True|False
    )
    
    
    :type roleArn: string
    :param roleArn: The ARN of the role that allows IoT to write to Cloudwatch logs.

    :type defaultLogLevel: string
    :param defaultLogLevel: The default logging level.

    :type disableAllLogs: boolean
    :param disableAllLogs: If true all logs are disabled. The default is false.

    """
    pass

def start_on_demand_audit_task(targetCheckNames=None):
    """
    Starts an on-demand Device Defender audit.
    See also: AWS API Documentation
    
    
    :example: response = client.start_on_demand_audit_task(
        targetCheckNames=[
            'string',
        ]
    )
    
    
    :type targetCheckNames: list
    :param targetCheckNames: [REQUIRED]
            Which checks are performed during the audit. The checks you specify must be enabled for your account or an exception occurs. Use DescribeAccountAuditConfiguration to see the list of all checks including those that are enabled or UpdateAccountAuditConfiguration to select which checks are enabled.
            (string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks including those that are enabled or UpdateAccountAuditConfiguration to select which checks are enabled.)
            

    :rtype: dict
    :return: {
        'taskId': 'string'
    }
    
    
    """
    pass

def start_thing_registration_task(templateBody=None, inputFileBucket=None, inputFileKey=None, roleArn=None):
    """
    Creates a bulk thing provisioning task.
    See also: AWS API Documentation
    
    
    :example: response = client.start_thing_registration_task(
        templateBody='string',
        inputFileBucket='string',
        inputFileKey='string',
        roleArn='string'
    )
    
    
    :type templateBody: string
    :param templateBody: [REQUIRED]
            The provisioning template.
            

    :type inputFileBucket: string
    :param inputFileBucket: [REQUIRED]
            The S3 bucket that contains the input file.
            

    :type inputFileKey: string
    :param inputFileKey: [REQUIRED]
            The name of input file within the S3 bucket. This file contains a newline delimited JSON file. Each line contains the parameter values to provision one device (thing).
            

    :type roleArn: string
    :param roleArn: [REQUIRED]
            The IAM role ARN that grants permission the input file.
            

    :rtype: dict
    :return: {
        'taskId': 'string'
    }
    
    
    """
    pass

def stop_thing_registration_task(taskId=None):
    """
    Cancels a bulk thing provisioning task.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_thing_registration_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]
            The bulk thing provisioning task ID.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The ARN of the resource.
            

    :type tags: list
    :param tags: [REQUIRED]
            The new or modified tags for the resource.
            (dict) --A set of key/value pairs that are used to manage the resource.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def test_authorization(principal=None, cognitoIdentityPoolId=None, authInfos=None, clientId=None, policyNamesToAdd=None, policyNamesToSkip=None):
    """
    Tests if a specified principal is authorized to perform an AWS IoT action on a specified resource. Use this to test and debug the authorization behavior of devices that connect to the AWS IoT device gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.test_authorization(
        principal='string',
        cognitoIdentityPoolId='string',
        authInfos=[
            {
                'actionType': 'PUBLISH'|'SUBSCRIBE'|'RECEIVE'|'CONNECT',
                'resources': [
                    'string',
                ]
            },
        ],
        clientId='string',
        policyNamesToAdd=[
            'string',
        ],
        policyNamesToSkip=[
            'string',
        ]
    )
    
    
    :type principal: string
    :param principal: The principal.

    :type cognitoIdentityPoolId: string
    :param cognitoIdentityPoolId: The Cognito identity pool ID.

    :type authInfos: list
    :param authInfos: [REQUIRED]
            A list of authorization info objects. Simulating authorization will create a response for each authInfo object in the list.
            (dict) --A collection of authorization information.
            actionType (string) --The type of action for which the principal is being authorized.
            resources (list) --The resources for which the principal is being authorized to perform the specified action.
            (string) --
            
            

    :type clientId: string
    :param clientId: The MQTT client ID.

    :type policyNamesToAdd: list
    :param policyNamesToAdd: When testing custom authorization, the policies specified here are treated as if they are attached to the principal being authorized.
            (string) --
            

    :type policyNamesToSkip: list
    :param policyNamesToSkip: When testing custom authorization, the policies specified here are treated as if they are not attached to the principal being authorized.
            (string) --
            

    :rtype: dict
    :return: {
        'authResults': [
            {
                'authInfo': {
                    'actionType': 'PUBLISH'|'SUBSCRIBE'|'RECEIVE'|'CONNECT',
                    'resources': [
                        'string',
                    ]
                },
                'allowed': {
                    'policies': [
                        {
                            'policyName': 'string',
                            'policyArn': 'string'
                        },
                    ]
                },
                'denied': {
                    'implicitDeny': {
                        'policies': [
                            {
                                'policyName': 'string',
                                'policyArn': 'string'
                            },
                        ]
                    },
                    'explicitDeny': {
                        'policies': [
                            {
                                'policyName': 'string',
                                'policyArn': 'string'
                            },
                        ]
                    }
                },
                'authDecision': 'ALLOWED'|'EXPLICIT_DENY'|'IMPLICIT_DENY',
                'missingContextValues': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def test_invoke_authorizer(authorizerName=None, token=None, tokenSignature=None):
    """
    Tests a custom authorization behavior by invoking a specified custom authorizer. Use this to test and debug the custom authorization behavior of devices that connect to the AWS IoT device gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.test_invoke_authorizer(
        authorizerName='string',
        token='string',
        tokenSignature='string'
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]
            The custom authorizer name.
            

    :type token: string
    :param token: [REQUIRED]
            The token returned by your custom authentication service.
            

    :type tokenSignature: string
    :param tokenSignature: [REQUIRED]
            The signature made with the token and your custom authentication service's private key.
            

    :rtype: dict
    :return: {
        'isAuthenticated': True|False,
        'principalId': 'string',
        'policyDocuments': [
            'string',
        ],
        'refreshAfterInSeconds': 123,
        'disconnectAfterInSeconds': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def transfer_certificate(certificateId=None, targetAwsAccount=None, transferMessage=None):
    """
    Transfers the specified certificate to the specified AWS account.
    You can cancel the transfer until it is acknowledged by the recipient.
    No notification is sent to the transfer destination's account. It is up to the caller to notify the transfer target.
    The certificate being transferred must not be in the ACTIVE state. You can use the UpdateCertificate API to deactivate it.
    The certificate must not have any policies attached to it. You can use the DetachPrincipalPolicy API to detach them.
    See also: AWS API Documentation
    
    
    :example: response = client.transfer_certificate(
        certificateId='string',
        targetAwsAccount='string',
        transferMessage='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
            

    :type targetAwsAccount: string
    :param targetAwsAccount: [REQUIRED]
            The AWS account.
            

    :type transferMessage: string
    :param transferMessage: The transfer message.

    :rtype: dict
    :return: {
        'transferredCertificateArn': 'string'
    }
    
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes the given tags (metadata) from the resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The ARN of the resource.
            

    :type tagKeys: list
    :param tagKeys: [REQUIRED]
            A list of the keys of the tags to be removed from the resource.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_account_audit_configuration(roleArn=None, auditNotificationTargetConfigurations=None, auditCheckConfigurations=None):
    """
    Configures or reconfigures the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.
    See also: AWS API Documentation
    
    
    :example: response = client.update_account_audit_configuration(
        roleArn='string',
        auditNotificationTargetConfigurations={
            'string': {
                'targetArn': 'string',
                'roleArn': 'string',
                'enabled': True|False
            }
        },
        auditCheckConfigurations={
            'string': {
                'enabled': True|False
            }
        }
    )
    
    
    :type roleArn: string
    :param roleArn: The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as necessary when performing an audit.

    :type auditNotificationTargetConfigurations: dict
    :param auditNotificationTargetConfigurations: Information about the targets to which audit notifications are sent.
            (string) --
            (dict) --Information about the targets to which audit notifications are sent.
            targetArn (string) --The ARN of the target (SNS topic) to which audit notifications are sent.
            roleArn (string) --The ARN of the role that grants permission to send notifications to the target.
            enabled (boolean) --True if notifications to the target are enabled.
            
            

    :type auditCheckConfigurations: dict
    :param auditCheckConfigurations: Specifies which audit checks are enabled and disabled for this account. Use DescribeAccountAuditConfiguration to see the list of all checks including those that are currently enabled.
            Note that some data collection may begin immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted.
            You cannot disable a check if it is used by any scheduled audit. You must first delete the check from the scheduled audit or delete the scheduled audit itself.
            On the first call to UpdateAccountAuditConfiguration this parameter is required and must specify at least one enabled check.
            (string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks including those that are enabled or UpdateAccountAuditConfiguration to select which checks are enabled.)
            (dict) --Which audit checks are enabled and disabled for this account.
            enabled (boolean) --True if this audit check is enabled for this account.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_authorizer(authorizerName=None, authorizerFunctionArn=None, tokenKeyName=None, tokenSigningPublicKeys=None, status=None):
    """
    Updates an authorizer.
    See also: AWS API Documentation
    
    
    :example: response = client.update_authorizer(
        authorizerName='string',
        authorizerFunctionArn='string',
        tokenKeyName='string',
        tokenSigningPublicKeys={
            'string': 'string'
        },
        status='ACTIVE'|'INACTIVE'
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]
            The authorizer name.
            

    :type authorizerFunctionArn: string
    :param authorizerFunctionArn: The ARN of the authorizer's Lambda function.

    :type tokenKeyName: string
    :param tokenKeyName: The key used to extract the token from the HTTP headers.

    :type tokenSigningPublicKeys: dict
    :param tokenSigningPublicKeys: The public keys used to verify the token signature.
            (string) --
            (string) --
            

    :type status: string
    :param status: The status of the update authorizer request.

    :rtype: dict
    :return: {
        'authorizerName': 'string',
        'authorizerArn': 'string'
    }
    
    
    """
    pass

def update_billing_group(billingGroupName=None, billingGroupProperties=None, expectedVersion=None):
    """
    Updates information about the billing group.
    See also: AWS API Documentation
    
    
    :example: response = client.update_billing_group(
        billingGroupName='string',
        billingGroupProperties={
            'billingGroupDescription': 'string'
        },
        expectedVersion=123
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: [REQUIRED]
            The name of the billing group.
            

    :type billingGroupProperties: dict
    :param billingGroupProperties: [REQUIRED]
            The properties of the billing group.
            billingGroupDescription (string) --The description of the billing group.
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the billing group. If the version of the billing group does not match the expected version specified in the request, the UpdateBillingGroup request is rejected with a VersionConflictException .

    :rtype: dict
    :return: {
        'version': 123
    }
    
    
    """
    pass

def update_ca_certificate(certificateId=None, newStatus=None, newAutoRegistrationStatus=None, registrationConfig=None, removeAutoRegistration=None):
    """
    Updates a registered CA certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.update_ca_certificate(
        certificateId='string',
        newStatus='ACTIVE'|'INACTIVE',
        newAutoRegistrationStatus='ENABLE'|'DISABLE',
        registrationConfig={
            'templateBody': 'string',
            'roleArn': 'string'
        },
        removeAutoRegistration=True|False
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The CA certificate identifier.
            

    :type newStatus: string
    :param newStatus: The updated status of the CA certificate.
            Note: The status value REGISTER_INACTIVE is deprecated and should not be used.
            

    :type newAutoRegistrationStatus: string
    :param newAutoRegistrationStatus: The new value for the auto registration status. Valid values are: 'ENABLE' or 'DISABLE'.

    :type registrationConfig: dict
    :param registrationConfig: Information about the registration configuration.
            templateBody (string) --The template body.
            roleArn (string) --The ARN of the role.
            

    :type removeAutoRegistration: boolean
    :param removeAutoRegistration: If true, remove auto registration.

    """
    pass

def update_certificate(certificateId=None, newStatus=None):
    """
    Updates the status of the specified certificate. This operation is idempotent.
    Moving a certificate from the ACTIVE state (including REVOKED) will not disconnect currently connected devices, but these devices will be unable to reconnect.
    The ACTIVE state is required to authenticate devices connecting to AWS IoT using a certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.update_certificate(
        certificateId='string',
        newStatus='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
            

    :type newStatus: string
    :param newStatus: [REQUIRED]
            The new status.
            Note: Setting the status to PENDING_TRANSFER will result in an exception being thrown. PENDING_TRANSFER is a status used internally by AWS IoT. It is not intended for developer use.Note: The status value REGISTER_INACTIVE is deprecated and should not be used.
            

    """
    pass

def update_dynamic_thing_group(thingGroupName=None, thingGroupProperties=None, expectedVersion=None, indexName=None, queryString=None, queryVersion=None):
    """
    Updates a dynamic thing group.
    See also: AWS API Documentation
    
    
    :example: response = client.update_dynamic_thing_group(
        thingGroupName='string',
        thingGroupProperties={
            'thingGroupDescription': 'string',
            'attributePayload': {
                'attributes': {
                    'string': 'string'
                },
                'merge': True|False
            }
        },
        expectedVersion=123,
        indexName='string',
        queryString='string',
        queryVersion='string'
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]
            The name of the dynamic thing group to update.
            

    :type thingGroupProperties: dict
    :param thingGroupProperties: [REQUIRED]
            The dynamic thing group properties to update.
            thingGroupDescription (string) --The thing group description.
            attributePayload (dict) --The thing group attributes in JSON format.
            attributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:
            {\'attributes\':{\'string1\':\'string2\'}}
            (string) --
            (string) --
            
            merge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.
            To remove an attribute, call UpdateThing with an empty attribute value.
            Note
            The merge attribute is only valid when calling UpdateThing .
            
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the dynamic thing group to update.

    :type indexName: string
    :param indexName: The dynamic thing group index to update.
            Note
            Currently one index is supported: 'AWS_Things'.
            

    :type queryString: string
    :param queryString: The dynamic thing group search query string to update.

    :type queryVersion: string
    :param queryVersion: The dynamic thing group query version to update.
            Note
            Currently one query version is supported: '2017-09-30'. If not specified, the query version defaults to this value.
            

    :rtype: dict
    :return: {
        'version': 123
    }
    
    
    """
    pass

def update_event_configurations(eventConfigurations=None):
    """
    Updates the event configurations.
    See also: AWS API Documentation
    
    
    :example: response = client.update_event_configurations(
        eventConfigurations={
            'string': {
                'Enabled': True|False
            }
        }
    )
    
    
    :type eventConfigurations: dict
    :param eventConfigurations: The new event configuration values.
            (string) --
            (dict) --Configuration.
            Enabled (boolean) --True to enable the configuration.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_indexing_configuration(thingIndexingConfiguration=None, thingGroupIndexingConfiguration=None):
    """
    Updates the search configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.update_indexing_configuration(
        thingIndexingConfiguration={
            'thingIndexingMode': 'OFF'|'REGISTRY'|'REGISTRY_AND_SHADOW',
            'thingConnectivityIndexingMode': 'OFF'|'STATUS'
        },
        thingGroupIndexingConfiguration={
            'thingGroupIndexingMode': 'OFF'|'ON'
        }
    )
    
    
    :type thingIndexingConfiguration: dict
    :param thingIndexingConfiguration: Thing indexing configuration.
            thingIndexingMode (string) -- [REQUIRED]Thing indexing mode. Valid values are:
            REGISTRY   Your thing index will contain only registry data.
            REGISTRY_AND_SHADOW - Your thing index will contain registry and shadow data.
            OFF - Thing indexing is disabled.
            thingConnectivityIndexingMode (string) --Thing connectivity indexing mode. Valid values are:
            STATUS   Your thing index will contain connectivity status. In order to enable thing connectivity indexing, thingIndexMode must not be set to OFF.
            OFF - Thing connectivity status indexing is disabled.
            

    :type thingGroupIndexingConfiguration: dict
    :param thingGroupIndexingConfiguration: Thing group indexing configuration.
            thingGroupIndexingMode (string) -- [REQUIRED]Thing group indexing mode.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_job(jobId=None, description=None, presignedUrlConfig=None, jobExecutionsRolloutConfig=None, abortConfig=None, timeoutConfig=None):
    """
    Updates supported fields of the specified job.
    See also: AWS API Documentation
    
    
    :example: response = client.update_job(
        jobId='string',
        description='string',
        presignedUrlConfig={
            'roleArn': 'string',
            'expiresInSec': 123
        },
        jobExecutionsRolloutConfig={
            'maximumPerMinute': 123,
            'exponentialRate': {
                'baseRatePerMinute': 123,
                'incrementFactor': 123.0,
                'rateIncreaseCriteria': {
                    'numberOfNotifiedThings': 123,
                    'numberOfSucceededThings': 123
                }
            }
        },
        abortConfig={
            'criteriaList': [
                {
                    'failureType': 'FAILED'|'REJECTED'|'TIMED_OUT'|'ALL',
                    'action': 'CANCEL',
                    'thresholdPercentage': 123.0,
                    'minNumberOfExecutedThings': 123
                },
            ]
        },
        timeoutConfig={
            'inProgressTimeoutInMinutes': 123
        }
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The ID of the job to be updated.
            

    :type description: string
    :param description: A short text description of the job.

    :type presignedUrlConfig: dict
    :param presignedUrlConfig: Configuration information for pre-signed S3 URLs.
            roleArn (string) --The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.
            expiresInSec (integer) --How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.
            

    :type jobExecutionsRolloutConfig: dict
    :param jobExecutionsRolloutConfig: Allows you to create a staged rollout of the job.
            maximumPerMinute (integer) --The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.
            exponentialRate (dict) --The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.
            baseRatePerMinute (integer) -- [REQUIRED]The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.
            incrementFactor (float) -- [REQUIRED]The exponential factor to increase the rate of rollout for a job.
            rateIncreaseCriteria (dict) -- [REQUIRED]The criteria to initiate the increase in rate of rollout for a job.
            AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).
            numberOfNotifiedThings (integer) --The threshold for number of notified things that will initiate the increase in rate of rollout.
            numberOfSucceededThings (integer) --The threshold for number of succeeded things that will initiate the increase in rate of rollout.
            
            

    :type abortConfig: dict
    :param abortConfig: Allows you to create criteria to abort a job.
            criteriaList (list) -- [REQUIRED]The list of abort criteria to define rules to abort the job.
            (dict) --Details of abort criteria to define rules to abort the job.
            failureType (string) -- [REQUIRED]The type of job execution failure to define a rule to initiate a job abort.
            action (string) -- [REQUIRED]The type of abort action to initiate a job abort.
            thresholdPercentage (float) -- [REQUIRED]The threshold as a percentage of the total number of executed things that will initiate a job abort.
            AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).
            minNumberOfExecutedThings (integer) -- [REQUIRED]Minimum number of executed things before evaluating an abort rule.
            
            

    :type timeoutConfig: dict
    :param timeoutConfig: Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to IN_PROGRESS . If the job execution status is not set to another terminal state before the time expires, it will be automatically set to TIMED_OUT .
            inProgressTimeoutInMinutes (integer) --Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can't be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal TIMED_OUT status.
            

    """
    pass

def update_role_alias(roleAlias=None, roleArn=None, credentialDurationSeconds=None):
    """
    Updates a role alias.
    See also: AWS API Documentation
    
    
    :example: response = client.update_role_alias(
        roleAlias='string',
        roleArn='string',
        credentialDurationSeconds=123
    )
    
    
    :type roleAlias: string
    :param roleAlias: [REQUIRED]
            The role alias to update.
            

    :type roleArn: string
    :param roleArn: The role ARN.

    :type credentialDurationSeconds: integer
    :param credentialDurationSeconds: The number of seconds the credential will be valid.

    :rtype: dict
    :return: {
        'roleAlias': 'string',
        'roleAliasArn': 'string'
    }
    
    
    """
    pass

def update_scheduled_audit(frequency=None, dayOfMonth=None, dayOfWeek=None, targetCheckNames=None, scheduledAuditName=None):
    """
    Updates a scheduled audit, including what checks are performed and how often the audit takes place.
    See also: AWS API Documentation
    
    
    :example: response = client.update_scheduled_audit(
        frequency='DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
        dayOfMonth='string',
        dayOfWeek='SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT',
        targetCheckNames=[
            'string',
        ],
        scheduledAuditName='string'
    )
    
    
    :type frequency: string
    :param frequency: How often the scheduled audit takes place. Can be one of 'DAILY', 'WEEKLY', 'BIWEEKLY' or 'MONTHLY'. The actual start time of each audit is determined by the system.

    :type dayOfMonth: string
    :param dayOfMonth: The day of the month on which the scheduled audit takes place. Can be '1' through '31' or 'LAST'. This field is required if the 'frequency' parameter is set to 'MONTHLY'. If days 29-31 are specified, and the month does not have that many days, the audit takes place on the 'LAST' day of the month.

    :type dayOfWeek: string
    :param dayOfWeek: The day of the week on which the scheduled audit takes place. Can be one of 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI' or 'SAT'. This field is required if the 'frequency' parameter is set to 'WEEKLY' or 'BIWEEKLY'.

    :type targetCheckNames: list
    :param targetCheckNames: Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks including those that are enabled or UpdateAccountAuditConfiguration to select which checks are enabled.)
            (string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks including those that are enabled or UpdateAccountAuditConfiguration to select which checks are enabled.)
            

    :type scheduledAuditName: string
    :param scheduledAuditName: [REQUIRED]
            The name of the scheduled audit. (Max. 128 chars)
            

    :rtype: dict
    :return: {
        'scheduledAuditArn': 'string'
    }
    
    
    """
    pass

def update_security_profile(securityProfileName=None, securityProfileDescription=None, behaviors=None, alertTargets=None, expectedVersion=None):
    """
    Updates a Device Defender security profile.
    See also: AWS API Documentation
    
    
    :example: response = client.update_security_profile(
        securityProfileName='string',
        securityProfileDescription='string',
        behaviors=[
            {
                'name': 'string',
                'metric': 'string',
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123
                }
            },
        ],
        alertTargets={
            'string': {
                'alertTargetArn': 'string',
                'roleArn': 'string'
            }
        },
        expectedVersion=123
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]
            The name of the security profile you want to update.
            

    :type securityProfileDescription: string
    :param securityProfileDescription: A description of the security profile.

    :type behaviors: list
    :param behaviors: Specifies the behaviors that, when violated by a device (thing), cause an alert.
            (dict) --A Device Defender security profile behavior.
            name (string) -- [REQUIRED]The name you have given to the behavior.
            metric (string) --What is measured by the behavior.
            criteria (dict) --The criteria that determine if a device is behaving normally in regard to the metric .
            comparisonOperator (string) --The operator that relates the thing measured (metric ) to the criteria (value ).
            value (dict) --The value to be compared with the metric .
            count (integer) --If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .
            cidrs (list) --If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .
            (string) --
            ports (list) --If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .
            (integer) --
            
            durationSeconds (integer) --Use this to specify the period of time over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ).
            
            

    :type alertTargets: dict
    :param alertTargets: Where the alerts are sent. (Alerts are always sent to the console.)
            (string) --The type of alert target: one of 'SNS'.
            (dict) --A structure containing the alert target ARN and the role ARN.
            alertTargetArn (string) -- [REQUIRED]The ARN of the notification target to which alerts are sent.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants permission to send alerts to the notification target.
            
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the security profile. A new version is generated whenever the security profile is updated. If you specify a value that is different than the actual version, a VersionConflictException is thrown.

    :rtype: dict
    :return: {
        'securityProfileName': 'string',
        'securityProfileArn': 'string',
        'securityProfileDescription': 'string',
        'behaviors': [
            {
                'name': 'string',
                'metric': 'string',
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123
                }
            },
        ],
        'alertTargets': {
            'string': {
                'alertTargetArn': 'string',
                'roleArn': 'string'
            }
        },
        'version': 123,
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_stream(streamId=None, description=None, files=None, roleArn=None):
    """
    Updates an existing stream. The stream version will be incremented by one.
    See also: AWS API Documentation
    
    
    :example: response = client.update_stream(
        streamId='string',
        description='string',
        files=[
            {
                'fileId': 123,
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'version': 'string'
                }
            },
        ],
        roleArn='string'
    )
    
    
    :type streamId: string
    :param streamId: [REQUIRED]
            The stream ID.
            

    :type description: string
    :param description: The description of the stream.

    :type files: list
    :param files: The files associated with the stream.
            (dict) --Represents a file to stream.
            fileId (integer) --The file ID.
            s3Location (dict) --The location of the file in S3.
            bucket (string) --The S3 bucket.
            key (string) --The S3 key.
            version (string) --The S3 bucket version.
            
            

    :type roleArn: string
    :param roleArn: An IAM role that allows the IoT service principal assumes to access your S3 files.

    :rtype: dict
    :return: {
        'streamId': 'string',
        'streamArn': 'string',
        'description': 'string',
        'streamVersion': 123
    }
    
    
    """
    pass

def update_thing(thingName=None, thingTypeName=None, attributePayload=None, expectedVersion=None, removeThingType=None):
    """
    Updates the data for a thing.
    See also: AWS API Documentation
    
    
    :example: response = client.update_thing(
        thingName='string',
        thingTypeName='string',
        attributePayload={
            'attributes': {
                'string': 'string'
            },
            'merge': True|False
        },
        expectedVersion=123,
        removeThingType=True|False
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing to update.
            

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type.

    :type attributePayload: dict
    :param attributePayload: A list of thing attributes, a JSON string containing name-value pairs. For example:
            {\'attributes\':{\'name1\':\'value2\'}}
            This data is used to add new attributes or update existing attributes.
            attributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:
            {\'attributes\':{\'string1\':\'string2\'}}
            (string) --
            (string) --
            
            merge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.
            To remove an attribute, call UpdateThing with an empty attribute value.
            Note
            The merge attribute is only valid when calling UpdateThing .
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the UpdateThing request is rejected with a VersionConflictException .

    :type removeThingType: boolean
    :param removeThingType: Remove a thing type association. If true , the association is removed.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_thing_group(thingGroupName=None, thingGroupProperties=None, expectedVersion=None):
    """
    Update a thing group.
    See also: AWS API Documentation
    
    
    :example: response = client.update_thing_group(
        thingGroupName='string',
        thingGroupProperties={
            'thingGroupDescription': 'string',
            'attributePayload': {
                'attributes': {
                    'string': 'string'
                },
                'merge': True|False
            }
        },
        expectedVersion=123
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]
            The thing group to update.
            

    :type thingGroupProperties: dict
    :param thingGroupProperties: [REQUIRED]
            The thing group properties.
            thingGroupDescription (string) --The thing group description.
            attributePayload (dict) --The thing group attributes in JSON format.
            attributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:
            {\'attributes\':{\'string1\':\'string2\'}}
            (string) --
            (string) --
            
            merge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.
            To remove an attribute, call UpdateThing with an empty attribute value.
            Note
            The merge attribute is only valid when calling UpdateThing .
            
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the thing group. If this does not match the version of the thing group being updated, the update will fail.

    :rtype: dict
    :return: {
        'version': 123
    }
    
    
    """
    pass

def update_thing_groups_for_thing(thingName=None, thingGroupsToAdd=None, thingGroupsToRemove=None, overrideDynamicGroups=None):
    """
    Updates the groups to which the thing belongs.
    See also: AWS API Documentation
    
    
    :example: response = client.update_thing_groups_for_thing(
        thingName='string',
        thingGroupsToAdd=[
            'string',
        ],
        thingGroupsToRemove=[
            'string',
        ],
        overrideDynamicGroups=True|False
    )
    
    
    :type thingName: string
    :param thingName: The thing whose group memberships will be updated.

    :type thingGroupsToAdd: list
    :param thingGroupsToAdd: The groups to which the thing will be added.
            (string) --
            

    :type thingGroupsToRemove: list
    :param thingGroupsToRemove: The groups from which the thing will be removed.
            (string) --
            

    :type overrideDynamicGroups: boolean
    :param overrideDynamicGroups: Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def validate_security_profile_behaviors(behaviors=None):
    """
    Validates a Device Defender security profile behaviors specification.
    See also: AWS API Documentation
    
    
    :example: response = client.validate_security_profile_behaviors(
        behaviors=[
            {
                'name': 'string',
                'metric': 'string',
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123
                }
            },
        ]
    )
    
    
    :type behaviors: list
    :param behaviors: [REQUIRED]
            Specifies the behaviors that, when violated by a device (thing), cause an alert.
            (dict) --A Device Defender security profile behavior.
            name (string) -- [REQUIRED]The name you have given to the behavior.
            metric (string) --What is measured by the behavior.
            criteria (dict) --The criteria that determine if a device is behaving normally in regard to the metric .
            comparisonOperator (string) --The operator that relates the thing measured (metric ) to the criteria (value ).
            value (dict) --The value to be compared with the metric .
            count (integer) --If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .
            cidrs (list) --If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .
            (string) --
            ports (list) --If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .
            (integer) --
            
            durationSeconds (integer) --Use this to specify the period of time over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ).
            
            

    :rtype: dict
    :return: {
        'valid': True|False,
        'validationErrors': [
            {
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

