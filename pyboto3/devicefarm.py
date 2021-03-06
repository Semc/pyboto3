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

def create_device_pool(projectArn=None, name=None, description=None, rules=None):
    """
    Creates a device pool.
    See also: AWS API Documentation
    
    Examples
    The following example creates a new device pool named MyDevicePool inside an existing project.
    Expected Output:
    
    :example: response = client.create_device_pool(
        projectArn='string',
        name='string',
        description='string',
        rules=[
            {
                'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                'value': 'string'
            },
        ]
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]
            The ARN of the project for the device pool.
            

    :type name: string
    :param name: [REQUIRED]
            The device pool's name.
            

    :type description: string
    :param description: The device pool's description.

    :type rules: list
    :param rules: [REQUIRED]
            The device pool's rules.
            (dict) --Represents a condition for a device pool. It is passed in as the rules parameter to CreateDevicePool and UpdateDevicePool .
            attribute (string) --The rule's attribute. It is the aspect of a device such as platform or model used as selection criteria to create or update a device pool.
            Allowed values include:
            ARN: The Amazon Resource Name (ARN) of a device. For example, 'arn:aws:devicefarm:us-west-2::device:12345Example'.
            PLATFORM: The device platform. Valid values are 'ANDROID' or 'IOS'.
            FORM_FACTOR: The device form factor. Valid values are 'PHONE' or 'TABLET'.
            MANUFACTURER: The device manufacturer. For example, 'Apple'.
            REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are 'TRUE' or 'FALSE'.
            REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are 'TRUE' or 'FALSE'.
            APPIUM_VERSION: The Appium version for the test.
            INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
            INSTANCE_LABELS: The label of the device instance.
            FLEET_TYPE: The fleet type. Valid values are 'PUBLIC' or 'PRIVATE'.
            operator (string) --The rule's operator.
            EQUALS: The equals operator.
            GREATER_THAN: The greater-than operator.
            IN: The in operator.
            LESS_THAN: The less-than operator.
            NOT_IN: The not-in operator.
            CONTAINS: The contains operator.
            value (string) --The rule's value.
            The value must be passed in as a string using escaped quotes.
            For example:
            'value': ''ANDROID''
            
            

    :rtype: dict
    :return: {
        'devicePool': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'rules': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                    'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CURATED: A device pool that is created and managed by AWS Device Farm.
    PRIVATE: A device pool that is created and managed by the device pool developer.
    
    """
    pass

def create_instance_profile(name=None, description=None, packageCleanup=None, excludeAppPackagesFromCleanup=None, rebootAfterUse=None):
    """
    Creates a profile that can be applied to one or more private fleet device instances.
    See also: AWS API Documentation
    
    
    :example: response = client.create_instance_profile(
        name='string',
        description='string',
        packageCleanup=True|False,
        excludeAppPackagesFromCleanup=[
            'string',
        ],
        rebootAfterUse=True|False
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of your instance profile.
            

    :type description: string
    :param description: The description of your instance profile.

    :type packageCleanup: boolean
    :param packageCleanup: When set to true , Device Farm will remove app packages after a test run. The default value is false for private devices.

    :type excludeAppPackagesFromCleanup: list
    :param excludeAppPackagesFromCleanup: An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
            The list of packages is only considered if you set packageCleanup to true .
            (string) --
            

    :type rebootAfterUse: boolean
    :param rebootAfterUse: When set to true , Device Farm will reboot the instance after a test run. The default value is true .

    :rtype: dict
    :return: {
        'instanceProfile': {
            'arn': 'string',
            'packageCleanup': True|False,
            'excludeAppPackagesFromCleanup': [
                'string',
            ],
            'rebootAfterUse': True|False,
            'name': 'string',
            'description': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_network_profile(projectArn=None, name=None, description=None, type=None, uplinkBandwidthBits=None, downlinkBandwidthBits=None, uplinkDelayMs=None, downlinkDelayMs=None, uplinkJitterMs=None, downlinkJitterMs=None, uplinkLossPercent=None, downlinkLossPercent=None):
    """
    Creates a network profile.
    See also: AWS API Documentation
    
    
    :example: response = client.create_network_profile(
        projectArn='string',
        name='string',
        description='string',
        type='CURATED'|'PRIVATE',
        uplinkBandwidthBits=123,
        downlinkBandwidthBits=123,
        uplinkDelayMs=123,
        downlinkDelayMs=123,
        uplinkJitterMs=123,
        downlinkJitterMs=123,
        uplinkLossPercent=123,
        downlinkLossPercent=123
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to create a network profile.
            

    :type name: string
    :param name: [REQUIRED]
            The name you wish to specify for the new network profile.
            

    :type description: string
    :param description: The description of the network profile.

    :type type: string
    :param type: The type of network profile you wish to create. Valid values are listed below.

    :type uplinkBandwidthBits: integer
    :param uplinkBandwidthBits: The data throughput rate in bits per second, as an integer from 0 to 104857600.

    :type downlinkBandwidthBits: integer
    :param downlinkBandwidthBits: The data throughput rate in bits per second, as an integer from 0 to 104857600.

    :type uplinkDelayMs: integer
    :param uplinkDelayMs: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

    :type downlinkDelayMs: integer
    :param downlinkDelayMs: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

    :type uplinkJitterMs: integer
    :param uplinkJitterMs: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

    :type downlinkJitterMs: integer
    :param downlinkJitterMs: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

    :type uplinkLossPercent: integer
    :param uplinkLossPercent: Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

    :type downlinkLossPercent: integer
    :param downlinkLossPercent: Proportion of received packets that fail to arrive from 0 to 100 percent.

    :rtype: dict
    :return: {
        'networkProfile': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'uplinkBandwidthBits': 123,
            'downlinkBandwidthBits': 123,
            'uplinkDelayMs': 123,
            'downlinkDelayMs': 123,
            'uplinkJitterMs': 123,
            'downlinkJitterMs': 123,
            'uplinkLossPercent': 123,
            'downlinkLossPercent': 123
        }
    }
    
    
    """
    pass

def create_project(name=None, defaultJobTimeoutMinutes=None):
    """
    Creates a new project.
    See also: AWS API Documentation
    
    Examples
    The following example creates a new project named MyProject.
    Expected Output:
    
    :example: response = client.create_project(
        name='string',
        defaultJobTimeoutMinutes=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The project's name.
            

    :type defaultJobTimeoutMinutes: integer
    :param defaultJobTimeoutMinutes: Sets the execution timeout value (in minutes) for a project. All test runs in this project will use the specified execution timeout value unless overridden when scheduling a run.

    :rtype: dict
    :return: {
        'project': {
            'arn': 'string',
            'name': 'string',
            'defaultJobTimeoutMinutes': 123,
            'created': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def create_remote_access_session(projectArn=None, deviceArn=None, instanceArn=None, sshPublicKey=None, remoteDebugEnabled=None, remoteRecordEnabled=None, remoteRecordAppArn=None, name=None, clientId=None, configuration=None, interactionMode=None, skipAppResign=None):
    """
    Specifies and starts a remote access session.
    See also: AWS API Documentation
    
    Examples
    The following example creates a remote access session named MySession.
    Expected Output:
    
    :example: response = client.create_remote_access_session(
        projectArn='string',
        deviceArn='string',
        instanceArn='string',
        sshPublicKey='string',
        remoteDebugEnabled=True|False,
        remoteRecordEnabled=True|False,
        remoteRecordAppArn='string',
        name='string',
        clientId='string',
        configuration={
            'billingMethod': 'METERED'|'UNMETERED',
            'vpceConfigurationArns': [
                'string',
            ]
        },
        interactionMode='INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
        skipAppResign=True|False
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to create a remote access session.
            

    :type deviceArn: string
    :param deviceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the device for which you want to create a remote access session.
            

    :type instanceArn: string
    :param instanceArn: The Amazon Resource Name (ARN) of the device instance for which you want to create a remote access session.

    :type sshPublicKey: string
    :param sshPublicKey: The public key of the ssh key pair you want to use for connecting to remote devices in your remote debugging session. This is only required if remoteDebugEnabled is set to true .

    :type remoteDebugEnabled: boolean
    :param remoteDebugEnabled: Set to true if you want to access devices remotely for debugging in your remote access session.

    :type remoteRecordEnabled: boolean
    :param remoteRecordEnabled: Set to true to enable remote recording for the remote access session.

    :type remoteRecordAppArn: string
    :param remoteRecordAppArn: The Amazon Resource Name (ARN) for the app to be recorded in the remote access session.

    :type name: string
    :param name: The name of the remote access session that you wish to create.

    :type clientId: string
    :param clientId: Unique identifier for the client. If you want access to multiple devices on the same client, you should pass the same clientId value in each call to CreateRemoteAccessSession . This is required only if remoteDebugEnabled is set to true .

    :type configuration: dict
    :param configuration: The configuration information for the remote access session request.
            billingMethod (string) --The billing method for the remote access session.
            vpceConfigurationArns (list) --An array of Amazon Resource Names (ARNs) included in the VPC endpoint configuration.
            (string) --
            

    :type interactionMode: string
    :param interactionMode: The interaction mode of the remote access session. Valid values are:
            INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You cannot run XCUITest framework-based tests in this mode.
            NO_VIDEO: You are connected to the device but cannot interact with it or view the screen. This mode has the fastest test execution speed. You can run XCUITest framework-based tests in this mode.
            VIDEO_ONLY: You can view the screen but cannot touch or rotate it. You can run XCUITest framework-based tests and watch the screen in this mode.
            

    :type skipAppResign: boolean
    :param skipAppResign: When set to true , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
            For more information about how Device Farm re-signs your app(s), see Do you modify my app? in the AWS Device Farm FAQs .
            

    :rtype: dict
    :return: {
        'remoteAccessSession': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'message': 'string',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'remoteDebugEnabled': True|False,
            'remoteRecordEnabled': True|False,
            'remoteRecordAppArn': 'string',
            'hostAddress': 'string',
            'clientId': 'string',
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'endpoint': 'string',
            'deviceUdid': 'string',
            'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
            'skipAppResign': True|False
        }
    }
    
    
    :returns: 
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def create_upload(projectArn=None, name=None, type=None, contentType=None):
    """
    Uploads an app or test scripts.
    See also: AWS API Documentation
    
    Examples
    The following example creates a new Appium Python test package upload inside an existing project.
    Expected Output:
    
    :example: response = client.create_upload(
        projectArn='string',
        name='string',
        type='ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
        contentType='string'
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]
            The ARN of the project for the upload.
            

    :type name: string
    :param name: [REQUIRED]
            The upload's file name. The name should not contain the '/' character. If uploading an iOS app, the file name needs to end with the .ipa extension. If uploading an Android app, the file name needs to end with the .apk extension. For all others, the file name must end with the .zip file extension.
            

    :type type: string
    :param type: [REQUIRED]
            The upload's upload type.
            Must be one of the following values:
            ANDROID_APP: An Android upload.
            IOS_APP: An iOS upload.
            WEB_APP: A web application upload.
            EXTERNAL_DATA: An external data upload.
            APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
            APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
            APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
            APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload.
            APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload.
            APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for a web app.
            APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for a web app.
            APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for a web app.
            APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for a web app.
            APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for a web app.
            CALABASH_TEST_PACKAGE: A Calabash test package upload.
            INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
            UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
            UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
            XCTEST_TEST_PACKAGE: An XCode test package upload.
            XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
            APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload.
            APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload.
            APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload.
            APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload.
            APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload.
            APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app.
            APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app.
            APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app.
            APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app.
            APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app.
            INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload.
            XCTEST_UI_TEST_SPEC: An XCode UI test spec upload.
            Note If you call CreateUpload with WEB_APP specified, AWS Device Farm throws an ArgumentException error.
            

    :type contentType: string
    :param contentType: The upload's content type (for example, 'application/octet-stream').

    :rtype: dict
    :return: {
        'upload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string',
            'category': 'CURATED'|'PRIVATE'
        }
    }
    
    
    :returns: 
    ANDROID_APP: An Android upload.
    IOS_APP: An iOS upload.
    WEB_APP: A web appliction upload.
    EXTERNAL_DATA: An external data upload.
    APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
    APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
    APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
    APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload.
    APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for web apps.
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for web apps.
    APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for web apps.
    APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for web apps.
    APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for web apps.
    CALABASH_TEST_PACKAGE: A Calabash test package upload.
    INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
    UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
    UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
    XCTEST_TEST_PACKAGE: An XCode test package upload.
    XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
    APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload.
    APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload.
    APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload.
    APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload.
    APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app.
    APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app.
    APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app.
    APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app.
    APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app.
    INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload.
    XCTEST_UI_TEST_SPEC: An XCode UI test spec upload.
    
    """
    pass

def create_vpce_configuration(vpceConfigurationName=None, vpceServiceName=None, serviceDnsName=None, vpceConfigurationDescription=None):
    """
    Creates a configuration record in Device Farm for your Amazon Virtual Private Cloud (VPC) endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.create_vpce_configuration(
        vpceConfigurationName='string',
        vpceServiceName='string',
        serviceDnsName='string',
        vpceConfigurationDescription='string'
    )
    
    
    :type vpceConfigurationName: string
    :param vpceConfigurationName: [REQUIRED]
            The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.
            

    :type vpceServiceName: string
    :param vpceServiceName: [REQUIRED]
            The name of the VPC endpoint service running inside your AWS account that you want Device Farm to test.
            

    :type serviceDnsName: string
    :param serviceDnsName: [REQUIRED]
            The DNS name of the service running in your VPC that you want Device Farm to test.
            

    :type vpceConfigurationDescription: string
    :param vpceConfigurationDescription: An optional description, providing more details about your VPC endpoint configuration.

    :rtype: dict
    :return: {
        'vpceConfiguration': {
            'arn': 'string',
            'vpceConfigurationName': 'string',
            'vpceServiceName': 'string',
            'serviceDnsName': 'string',
            'vpceConfigurationDescription': 'string'
        }
    }
    
    
    """
    pass

def delete_device_pool(arn=None):
    """
    Deletes a device pool given the pool ARN. Does not allow deletion of curated pools owned by the system.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a specific device pool.
    Expected Output:
    
    :example: response = client.delete_device_pool(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm device pool you wish to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_instance_profile(arn=None):
    """
    Deletes a profile that can be applied to one or more private device instances.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_instance_profile(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the instance profile you are requesting to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_network_profile(arn=None):
    """
    Deletes a network profile.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_network_profile(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the network profile you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_project(arn=None):
    """
    Deletes an AWS Device Farm project, given the project ARN.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a specific project.
    Expected Output:
    
    :example: response = client.delete_project(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm project you wish to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_remote_access_session(arn=None):
    """
    Deletes a completed remote access session and its results.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a specific remote access session.
    Expected Output:
    
    :example: response = client.delete_remote_access_session(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the sesssion for which you want to delete remote access.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_run(arn=None):
    """
    Deletes the run, given the run ARN.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a specific test run.
    Expected Output:
    
    :example: response = client.delete_run(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) for the run you wish to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_upload(arn=None):
    """
    Deletes an upload given the upload ARN.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a specific upload.
    Expected Output:
    
    :example: response = client.delete_upload(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm upload you wish to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_vpce_configuration(arn=None):
    """
    Deletes a configuration for your Amazon Virtual Private Cloud (VPC) endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_vpce_configuration(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to delete.
            

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

def get_account_settings():
    """
    Returns the number of unmetered iOS and/or unmetered Android devices that have been purchased by the account.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about your Device Farm account settings.
    Expected Output:
    
    :example: response = client.get_account_settings()
    
    
    :rtype: dict
    :return: {
        'accountSettings': {
            'awsAccountNumber': 'string',
            'unmeteredDevices': {
                'string': 123
            },
            'unmeteredRemoteAccessDevices': {
                'string': 123
            },
            'maxJobTimeoutMinutes': 123,
            'trialMinutes': {
                'total': 123.0,
                'remaining': 123.0
            },
            'maxSlots': {
                'string': 123
            },
            'defaultJobTimeoutMinutes': 123,
            'skipAppResign': True|False
        }
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def get_device(arn=None):
    """
    Gets information about a unique device type.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about a specific device.
    Expected Output:
    
    :example: response = client.get_device(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The device type's ARN.
            

    :rtype: dict
    :return: {
        'device': {
            'arn': 'string',
            'name': 'string',
            'manufacturer': 'string',
            'model': 'string',
            'modelId': 'string',
            'formFactor': 'PHONE'|'TABLET',
            'platform': 'ANDROID'|'IOS',
            'os': 'string',
            'cpu': {
                'frequency': 'string',
                'architecture': 'string',
                'clock': 123.0
            },
            'resolution': {
                'width': 123,
                'height': 123
            },
            'heapSize': 123,
            'memory': 123,
            'image': 'string',
            'carrier': 'string',
            'radio': 'string',
            'remoteAccessEnabled': True|False,
            'remoteDebugEnabled': True|False,
            'fleetType': 'string',
            'fleetName': 'string',
            'instances': [
                {
                    'arn': 'string',
                    'deviceArn': 'string',
                    'labels': [
                        'string',
                    ],
                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                    'udid': 'string',
                    'instanceProfile': {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    }
                },
            ],
            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
        }
    }
    
    
    :returns: 
    ANDROID: The Android platform.
    IOS: The iOS platform.
    
    """
    pass

def get_device_instance(arn=None):
    """
    Returns information about a device instance belonging to a private device fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.get_device_instance(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the instance you're requesting information about.
            

    :rtype: dict
    :return: {
        'deviceInstance': {
            'arn': 'string',
            'deviceArn': 'string',
            'labels': [
                'string',
            ],
            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
            'udid': 'string',
            'instanceProfile': {
                'arn': 'string',
                'packageCleanup': True|False,
                'excludeAppPackagesFromCleanup': [
                    'string',
                ],
                'rebootAfterUse': True|False,
                'name': 'string',
                'description': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_device_pool(arn=None):
    """
    Gets information about a device pool.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about a specific device pool, given a project ARN.
    Expected Output:
    
    :example: response = client.get_device_pool(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The device pool's ARN.
            

    :rtype: dict
    :return: {
        'devicePool': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'rules': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                    'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    ARN: The Amazon Resource Name (ARN) of a device. For example, "arn:aws:devicefarm:us-west-2::device:12345Example".
    PLATFORM: The device platform. Valid values are "ANDROID" or "IOS".
    FORM_FACTOR: The device form factor. Valid values are "PHONE" or "TABLET".
    MANUFACTURER: The device manufacturer. For example, "Apple".
    REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are "TRUE" or "FALSE".
    REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are "TRUE" or "FALSE".
    APPIUM_VERSION: The Appium version for the test.
    INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
    INSTANCE_LABELS: The label of the device instance.
    FLEET_TYPE: The fleet type. Valid values are "PUBLIC" or "PRIVATE".
    
    """
    pass

def get_device_pool_compatibility(devicePoolArn=None, appArn=None, testType=None, test=None, configuration=None):
    """
    Gets information about compatibility with a device pool.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about the compatibility of a specific device pool, given its ARN.
    Expected Output:
    
    :example: response = client.get_device_pool_compatibility(
        devicePoolArn='string',
        appArn='string',
        testType='BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
        test={
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'testPackageArn': 'string',
            'testSpecArn': 'string',
            'filter': 'string',
            'parameters': {
                'string': 'string'
            }
        },
        configuration={
            'extraDataPackageArn': 'string',
            'networkProfileArn': 'string',
            'locale': 'string',
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'vpceConfigurationArns': [
                'string',
            ],
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'auxiliaryApps': [
                'string',
            ],
            'billingMethod': 'METERED'|'UNMETERED'
        }
    )
    
    
    :type devicePoolArn: string
    :param devicePoolArn: [REQUIRED]
            The device pool's ARN.
            

    :type appArn: string
    :param appArn: The ARN of the app that is associated with the specified device pool.

    :type testType: string
    :param testType: The test type for the specified device pool.
            Allowed values include the following:
            BUILTIN_FUZZ: The built-in fuzz type.
            BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
            APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
            APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
            APPIUM_PYTHON: The Appium Python type.
            APPIUM_NODE: The Appium Node.js type.
            APPIUM_RUBY: The Appium Ruby type.
            APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
            APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
            APPIUM_WEB_PYTHON: The Appium Python type for web apps.
            APPIUM_WEB_NODE: The Appium Node.js type for web apps.
            APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
            CALABASH: The Calabash type.
            INSTRUMENTATION: The Instrumentation type.
            UIAUTOMATION: The uiautomation type.
            UIAUTOMATOR: The uiautomator type.
            XCTEST: The XCode test type.
            XCTEST_UI: The XCode UI test type.
            

    :type test: dict
    :param test: Information about the uploaded test to be run against the device pool.
            type (string) -- [REQUIRED]The test's type.
            Must be one of the following values:
            BUILTIN_FUZZ: The built-in fuzz type.
            BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
            APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
            APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
            APPIUM_PYTHON: The Appium Python type.
            APPIUM_NODE: The Appium Node.js type.
            APPIUM_RUBY: The Appium Ruby type.
            APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
            APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
            APPIUM_WEB_PYTHON: The Appium Python type for web apps.
            APPIUM_WEB_NODE: The Appium Node.js type for web apps.
            APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
            CALABASH: The Calabash type.
            INSTRUMENTATION: The Instrumentation type.
            UIAUTOMATION: The uiautomation type.
            UIAUTOMATOR: The uiautomator type.
            XCTEST: The XCode test type.
            XCTEST_UI: The XCode UI test type.
            testPackageArn (string) --The ARN of the uploaded test that will be run.
            testSpecArn (string) --The ARN of the YAML-formatted test specification.
            filter (string) --The test's filter.
            parameters (dict) --The test's parameters, such as test framework parameters and fixture settings. Parameters are represented by name-value pairs of strings.
            For all tests:
            app_performance_monitoring: Performance monitoring is enabled by default. Set this parameter to 'false' to disable it.
            For Calabash tests:
            profile: A cucumber profile, for example, 'my_profile_name'.
            tags: You can limit execution to features or scenarios that have (or don't have) certain tags, for example, '@smoke' or '@smoke,~@wip'.
            For Appium tests (all types):
            appium_version: The Appium version. Currently supported values are '1.6.5' (and higher), 'latest', and 'default'.
             latest  will run the latest Appium version supported by Device Farm (1.9.1).
            For  default , Device Farm will choose a compatible version of Appium for the device. The current behavior is to run 1.7.2 on Android devices and iOS 9 and earlier, 1.7.2 for iOS 10 and later.
            This behavior is subject to change.
            For Fuzz tests (Android only):
            event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.
            throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.
            seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
            For Explorer tests:
            username: A username to use if the Explorer encounters a login form. If not supplied, no username will be inserted.
            password: A password to use if the Explorer encounters a login form. If not supplied, no password will be inserted.
            For Instrumentation:
            filter: A test filter string. Examples:
            Running a single test case: 'com.android.abc.Test1'
            Running a single test: 'com.android.abc.Test1#smoke'
            Running multiple tests: 'com.android.abc.Test1,com.android.abc.Test2'
            For XCTest and XCTestUI:
            filter: A test filter string. Examples:
            Running a single test class: 'LoginTests'
            Running a multiple test classes: 'LoginTests,SmokeTests'
            Running a single test: 'LoginTests/testValid'
            Running multiple tests: 'LoginTests/testValid,LoginTests/testInvalid'
            For UIAutomator:
            filter: A test filter string. Examples:
            Running a single test case: 'com.android.abc.Test1'
            Running a single test: 'com.android.abc.Test1#smoke'
            Running multiple tests: 'com.android.abc.Test1,com.android.abc.Test2'
            
            (string) --
            (string) --
            
            

    :type configuration: dict
    :param configuration: An object containing information about the settings for a run.
            extraDataPackageArn (string) --The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm will extract to external data for Android or the app's sandbox for iOS.
            networkProfileArn (string) --Reserved for internal use.
            locale (string) --Information about the locale that is used for the run.
            location (dict) --Information about the location that is used for the run.
            latitude (float) -- [REQUIRED]The latitude.
            longitude (float) -- [REQUIRED]The longitude.
            vpceConfigurationArns (list) --An array of Amazon Resource Names (ARNs) for your VPC endpoint configurations.
            (string) --
            customerArtifactPaths (dict) --Input CustomerArtifactPaths object for the scheduled run configuration.
            iosPaths (list) --Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.
            (string) --
            androidPaths (list) --Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.
            (string) --
            deviceHostPaths (list) --Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.
            (string) --
            
            radios (dict) --Information about the radio states for the run.
            wifi (boolean) --True if Wi-Fi is enabled at the beginning of the test; otherwise, false.
            bluetooth (boolean) --True if Bluetooth is enabled at the beginning of the test; otherwise, false.
            nfc (boolean) --True if NFC is enabled at the beginning of the test; otherwise, false.
            gps (boolean) --True if GPS is enabled at the beginning of the test; otherwise, false.
            auxiliaryApps (list) --A list of auxiliary apps for the run.
            (string) --
            billingMethod (string) --Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is metered .
            

    :rtype: dict
    :return: {
        'compatibleDevices': [
            {
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'modelId': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string',
                    'instances': [
                        {
                            'arn': 'string',
                            'deviceArn': 'string',
                            'labels': [
                                'string',
                            ],
                            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                            'udid': 'string',
                            'instanceProfile': {
                                'arn': 'string',
                                'packageCleanup': True|False,
                                'excludeAppPackagesFromCleanup': [
                                    'string',
                                ],
                                'rebootAfterUse': True|False,
                                'name': 'string',
                                'description': 'string'
                            }
                        },
                    ],
                    'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                },
                'compatible': True|False,
                'incompatibilityMessages': [
                    {
                        'message': 'string',
                        'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'
                    },
                ]
            },
        ],
        'incompatibleDevices': [
            {
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'modelId': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string',
                    'instances': [
                        {
                            'arn': 'string',
                            'deviceArn': 'string',
                            'labels': [
                                'string',
                            ],
                            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                            'udid': 'string',
                            'instanceProfile': {
                                'arn': 'string',
                                'packageCleanup': True|False,
                                'excludeAppPackagesFromCleanup': [
                                    'string',
                                ],
                                'rebootAfterUse': True|False,
                                'name': 'string',
                                'description': 'string'
                            }
                        },
                    ],
                    'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                },
                'compatible': True|False,
                'incompatibilityMessages': [
                    {
                        'message': 'string',
                        'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    PHONE: The phone form factor.
    TABLET: The tablet form factor.
    
    """
    pass

def get_instance_profile(arn=None):
    """
    Returns information about the specified instance profile.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_profile(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of your instance profile.
            

    :rtype: dict
    :return: {
        'instanceProfile': {
            'arn': 'string',
            'packageCleanup': True|False,
            'excludeAppPackagesFromCleanup': [
                'string',
            ],
            'rebootAfterUse': True|False,
            'name': 'string',
            'description': 'string'
        }
    }
    
    
    """
    pass

def get_job(arn=None):
    """
    Gets information about a job.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about a specific job.
    Expected Output:
    
    :example: response = client.get_job(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The job's ARN.
            

    :rtype: dict
    :return: {
        'job': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'videoEndpoint': 'string',
            'videoCapture': True|False
        }
    }
    
    
    :returns: 
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def get_network_profile(arn=None):
    """
    Returns information about a network profile.
    See also: AWS API Documentation
    
    
    :example: response = client.get_network_profile(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the network profile you want to return information about.
            

    :rtype: dict
    :return: {
        'networkProfile': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'uplinkBandwidthBits': 123,
            'downlinkBandwidthBits': 123,
            'uplinkDelayMs': 123,
            'downlinkDelayMs': 123,
            'uplinkJitterMs': 123,
            'downlinkJitterMs': 123,
            'uplinkLossPercent': 123,
            'downlinkLossPercent': 123
        }
    }
    
    
    """
    pass

def get_offering_status(nextToken=None):
    """
    Gets the current status and future status of all offerings purchased by an AWS account. The response indicates how many offerings are currently available and the offerings that will be available in the next period. The API returns a NotEligible error if the user is not permitted to invoke the operation. Please contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about Device Farm offerings available to your account.
    Expected Output:
    
    :example: response = client.get_offering_status(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'current': {
            'string': {
                'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                'offering': {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
                'quantity': 123,
                'effectiveOn': datetime(2015, 1, 1)
            }
        },
        'nextPeriod': {
            'string': {
                'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                'offering': {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
                'quantity': 123,
                'effectiveOn': datetime(2015, 1, 1)
            }
        },
        'nextToken': 'string'
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

def get_project(arn=None):
    """
    Gets information about a project.
    See also: AWS API Documentation
    
    Examples
    The following example gets information about a specific project.
    Expected Output:
    
    :example: response = client.get_project(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The project's ARN.
            

    :rtype: dict
    :return: {
        'project': {
            'arn': 'string',
            'name': 'string',
            'defaultJobTimeoutMinutes': 123,
            'created': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_remote_access_session(arn=None):
    """
    Returns a link to a currently running remote access session.
    See also: AWS API Documentation
    
    Examples
    The following example gets a specific remote access session.
    Expected Output:
    
    :example: response = client.get_remote_access_session(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session about which you want to get session information.
            

    :rtype: dict
    :return: {
        'remoteAccessSession': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'message': 'string',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'remoteDebugEnabled': True|False,
            'remoteRecordEnabled': True|False,
            'remoteRecordAppArn': 'string',
            'hostAddress': 'string',
            'clientId': 'string',
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'endpoint': 'string',
            'deviceUdid': 'string',
            'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
            'skipAppResign': True|False
        }
    }
    
    
    :returns: 
    PENDING: A pending condition.
    PASSED: A passing condition.
    WARNED: A warning condition.
    FAILED: A failed condition.
    SKIPPED: A skipped condition.
    ERRORED: An error condition.
    STOPPED: A stopped condition.
    
    """
    pass

def get_run(arn=None):
    """
    Gets information about a run.
    See also: AWS API Documentation
    
    Examples
    The following example gets information about a specific test run.
    Expected Output:
    
    :example: response = client.get_run(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The run's ARN.
            

    :rtype: dict
    :return: {
        'run': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'platform': 'ANDROID'|'IOS',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'totalJobs': 123,
            'completedJobs': 123,
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'networkProfile': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            },
            'parsingResultUrl': 'string',
            'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
            'seed': 123,
            'appUpload': 'string',
            'eventCount': 123,
            'jobTimeoutMinutes': 123,
            'devicePoolArn': 'string',
            'locale': 'string',
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'webUrl': 'string',
            'skipAppResign': True|False,
            'testSpecArn': 'string',
            'deviceSelectionResult': {
                'filters': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                        'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                        'values': [
                            'string',
                        ]
                    },
                ],
                'matchedDevicesCount': 123,
                'maxDevices': 123
            }
        }
    }
    
    
    :returns: 
    ANDROID: The Android platform.
    IOS: The iOS platform.
    
    """
    pass

def get_suite(arn=None):
    """
    Gets information about a suite.
    See also: AWS API Documentation
    
    Examples
    The following example gets information about a specific test suite.
    Expected Output:
    
    :example: response = client.get_suite(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The suite's ARN.
            

    :rtype: dict
    :return: {
        'suite': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            }
        }
    }
    
    
    :returns: 
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def get_test(arn=None):
    """
    Gets information about a test.
    See also: AWS API Documentation
    
    Examples
    The following example gets information about a specific test.
    Expected Output:
    
    :example: response = client.get_test(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The test's ARN.
            

    :rtype: dict
    :return: {
        'test': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            }
        }
    }
    
    
    :returns: 
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def get_upload(arn=None):
    """
    Gets information about an upload.
    See also: AWS API Documentation
    
    Examples
    The following example gets information about a specific upload.
    Expected Output:
    
    :example: response = client.get_upload(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The upload's ARN.
            

    :rtype: dict
    :return: {
        'upload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string',
            'category': 'CURATED'|'PRIVATE'
        }
    }
    
    
    :returns: 
    FAILED: A failed status.
    INITIALIZED: An initialized status.
    PROCESSING: A processing status.
    SUCCEEDED: A succeeded status.
    
    """
    pass

def get_vpce_configuration(arn=None):
    """
    Returns information about the configuration settings for your Amazon Virtual Private Cloud (VPC) endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.get_vpce_configuration(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to describe.
            

    :rtype: dict
    :return: {
        'vpceConfiguration': {
            'arn': 'string',
            'vpceConfigurationName': 'string',
            'vpceServiceName': 'string',
            'serviceDnsName': 'string',
            'vpceConfigurationDescription': 'string'
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

def install_to_remote_access_session(remoteAccessSessionArn=None, appArn=None):
    """
    Installs an application to the device in a remote access session. For Android applications, the file must be in .apk format. For iOS applications, the file must be in .ipa format.
    See also: AWS API Documentation
    
    Examples
    The following example installs a specific app to a device in a specific remote access session.
    Expected Output:
    
    :example: response = client.install_to_remote_access_session(
        remoteAccessSessionArn='string',
        appArn='string'
    )
    
    
    :type remoteAccessSessionArn: string
    :param remoteAccessSessionArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.
            

    :type appArn: string
    :param appArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the app about which you are requesting information.
            

    :rtype: dict
    :return: {
        'appUpload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string',
            'category': 'CURATED'|'PRIVATE'
        }
    }
    
    
    :returns: 
    ANDROID_APP: An Android upload.
    IOS_APP: An iOS upload.
    WEB_APP: A web appliction upload.
    EXTERNAL_DATA: An external data upload.
    APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
    APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
    APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
    APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload.
    APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for web apps.
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for web apps.
    APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for web apps.
    APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for web apps.
    APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for web apps.
    CALABASH_TEST_PACKAGE: A Calabash test package upload.
    INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
    UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
    UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
    XCTEST_TEST_PACKAGE: An XCode test package upload.
    XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
    APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload.
    APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload.
    APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload.
    APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload.
    APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app.
    APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app.
    APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app.
    APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app.
    APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app.
    INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload.
    XCTEST_UI_TEST_SPEC: An XCode UI test spec upload.
    
    """
    pass

def list_artifacts(arn=None, type=None, nextToken=None):
    """
    Gets information about artifacts.
    See also: AWS API Documentation
    
    Examples
    The following example lists screenshot artifacts for a specific run.
    Expected Output:
    
    :example: response = client.list_artifacts(
        arn='string',
        type='SCREENSHOT'|'FILE'|'LOG',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Run, Job, Suite, or Test ARN.
            

    :type type: string
    :param type: [REQUIRED]
            The artifacts' type.
            Allowed values include:
            FILE: The artifacts are files.
            LOG: The artifacts are logs.
            SCREENSHOT: The artifacts are screenshots.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'artifacts': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'UNKNOWN'|'SCREENSHOT'|'DEVICE_LOG'|'MESSAGE_LOG'|'VIDEO_LOG'|'RESULT_LOG'|'SERVICE_LOG'|'WEBKIT_LOG'|'INSTRUMENTATION_OUTPUT'|'EXERCISER_MONKEY_OUTPUT'|'CALABASH_JSON_OUTPUT'|'CALABASH_PRETTY_OUTPUT'|'CALABASH_STANDARD_OUTPUT'|'CALABASH_JAVA_XML_OUTPUT'|'AUTOMATION_OUTPUT'|'APPIUM_SERVER_OUTPUT'|'APPIUM_JAVA_OUTPUT'|'APPIUM_JAVA_XML_OUTPUT'|'APPIUM_PYTHON_OUTPUT'|'APPIUM_PYTHON_XML_OUTPUT'|'EXPLORER_EVENT_LOG'|'EXPLORER_SUMMARY_LOG'|'APPLICATION_CRASH_REPORT'|'XCTEST_LOG'|'VIDEO'|'CUSTOMER_ARTIFACT'|'CUSTOMER_ARTIFACT_LOG'|'TESTSPEC_OUTPUT',
                'extension': 'string',
                'url': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    UNKNOWN: An unknown type.
    SCREENSHOT: The screenshot type.
    DEVICE_LOG: The device log type.
    MESSAGE_LOG: The message log type.
    VIDEO_LOG: The video log type.
    RESULT_LOG: The result log type.
    SERVICE_LOG: The service log type.
    WEBKIT_LOG: The web kit log type.
    INSTRUMENTATION_OUTPUT: The instrumentation type.
    EXERCISER_MONKEY_OUTPUT: For Android, the artifact (log) generated by an Android fuzz test.
    CALABASH_JSON_OUTPUT: The Calabash JSON output type.
    CALABASH_PRETTY_OUTPUT: The Calabash pretty output type.
    CALABASH_STANDARD_OUTPUT: The Calabash standard output type.
    CALABASH_JAVA_XML_OUTPUT: The Calabash Java XML output type.
    AUTOMATION_OUTPUT: The automation output type.
    APPIUM_SERVER_OUTPUT: The Appium server output type.
    APPIUM_JAVA_OUTPUT: The Appium Java output type.
    APPIUM_JAVA_XML_OUTPUT: The Appium Java XML output type.
    APPIUM_PYTHON_OUTPUT: The Appium Python output type.
    APPIUM_PYTHON_XML_OUTPUT: The Appium Python XML output type.
    EXPLORER_EVENT_LOG: The Explorer event log output type.
    EXPLORER_SUMMARY_LOG: The Explorer summary log output type.
    APPLICATION_CRASH_REPORT: The application crash report output type.
    XCTEST_LOG: The XCode test output type.
    VIDEO: The Video output type.
    CUSTOMER_ARTIFACT:The Customer Artifact output type.
    CUSTOMER_ARTIFACT_LOG: The Customer Artifact Log output type.
    TESTSPEC_OUTPUT: The Test Spec Output type.
    
    """
    pass

def list_device_instances(maxResults=None, nextToken=None):
    """
    Returns information about the private device instances associated with one or more AWS accounts.
    See also: AWS API Documentation
    
    
    :example: response = client.list_device_instances(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: An integer specifying the maximum number of items you want to return in the API response.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'deviceInstances': [
            {
                'arn': 'string',
                'deviceArn': 'string',
                'labels': [
                    'string',
                ],
                'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                'udid': 'string',
                'instanceProfile': {
                    'arn': 'string',
                    'packageCleanup': True|False,
                    'excludeAppPackagesFromCleanup': [
                        'string',
                    ],
                    'rebootAfterUse': True|False,
                    'name': 'string',
                    'description': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_device_pools(arn=None, type=None, nextToken=None):
    """
    Gets information about device pools.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about the private device pools in a specific project.
    Expected Output:
    
    :example: response = client.list_device_pools(
        arn='string',
        type='CURATED'|'PRIVATE',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The project ARN.
            

    :type type: string
    :param type: The device pools' type.
            Allowed values include:
            CURATED: A device pool that is created and managed by AWS Device Farm.
            PRIVATE: A device pool that is created and managed by the device pool developer.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'devicePools': [
            {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'rules': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                        'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                        'value': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CURATED: A device pool that is created and managed by AWS Device Farm.
    PRIVATE: A device pool that is created and managed by the device pool developer.
    
    """
    pass

def list_devices(arn=None, nextToken=None, filters=None):
    """
    Gets information about unique device types.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about the available devices in a specific project.
    Expected Output:
    
    :example: response = client.list_devices(
        arn='string',
        nextToken='string',
        filters=[
            {
                'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type arn: string
    :param arn: The Amazon Resource Name (ARN) of the project.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type filters: list
    :param filters: Used to select a set of devices. A filter is made up of an attribute, an operator, and one or more values.
            Attribute: The aspect of a device such as platform or model used as the selction criteria in a device filter. Allowed values include:
            ARN: The Amazon Resource Name (ARN) of the device. For example, 'arn:aws:devicefarm:us-west-2::device:12345Example'.
            PLATFORM: The device platform. Valid values are 'ANDROID' or 'IOS'.
            OS_VERSION: The operating system version. For example, '10.3.2'.
            MODEL: The device model. For example, 'iPad 5th Gen'.
            AVAILABILITY: The current availability of the device. Valid values are 'AVAILABLE', 'HIGHLY_AVAILABLE', 'BUSY', or 'TEMPORARY_NOT_AVAILABLE'.
            FORM_FACTOR: The device form factor. Valid values are 'PHONE' or 'TABLET'.
            MANUFACTURER: The device manufacturer. For example, 'Apple'.
            REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are 'TRUE' or 'FALSE'.
            REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are 'TRUE' or 'FALSE'.
            INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
            INSTANCE_LABELS: The label of the device instance.
            FLEET_TYPE: The fleet type. Valid values are 'PUBLIC' or 'PRIVATE'.
            Operator: The filter operator.
            The EQUALS operator is available for every attribute except INSTANCE_LABELS.
            The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.
            The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.
            The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.
            Values: An array of one or more filter values.
            The IN and NOT_IN operators take a values array that has one or more elements.
            The other operators require an array with a single element.
            In a request, the AVAILABILITY attribute takes 'AVAILABLE', 'HIGHLY_AVAILABLE', 'BUSY', or 'TEMPORARY_NOT_AVAILABLE' as values.
            
            (dict) --Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the deviceSelectionConfiguration parameter to ScheduleRun. For an example of the JSON request syntax, see ScheduleRun .
            It is also passed in as the filters parameter to ListDevices. For an example of the JSON request syntax, see ListDevices .
            attribute (string) --The aspect of a device such as platform or model used as the selection criteria in a device filter.
            Allowed values include:
            ARN: The Amazon Resource Name (ARN) of the device. For example, 'arn:aws:devicefarm:us-west-2::device:12345Example'.
            PLATFORM: The device platform. Valid values are 'ANDROID' or 'IOS'.
            OS_VERSION: The operating system version. For example, '10.3.2'.
            MODEL: The device model. For example, 'iPad 5th Gen'.
            AVAILABILITY: The current availability of the device. Valid values are 'AVAILABLE', 'HIGHLY_AVAILABLE', 'BUSY', or 'TEMPORARY_NOT_AVAILABLE'.
            FORM_FACTOR: The device form factor. Valid values are 'PHONE' or 'TABLET'.
            MANUFACTURER: The device manufacturer. For example, 'Apple'.
            REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are 'TRUE' or 'FALSE'.
            REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are 'TRUE' or 'FALSE'.
            INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
            INSTANCE_LABELS: The label of the device instance.
            FLEET_TYPE: The fleet type. Valid values are 'PUBLIC' or 'PRIVATE'.
            operator (string) --The filter operator.
            The EQUALS operator is available for every attribute except INSTANCE_LABELS.
            The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.
            The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.
            The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.
            values (list) --An array of one or more filter values used in a device filter.
            Operator Values
            The IN and NOT_IN operators can take a values array that has more than one element.
            The other operators require an array with a single element.
            Attribute Values
            The PLATFORM attribute can be set to 'ANDROID' or 'IOS'.
            The AVAILABILITY attribute can be set to 'AVAILABLE', 'HIGHLY_AVAILABLE', 'BUSY', or 'TEMPORARY_NOT_AVAILABLE'.
            The FORM_FACTOR attribute can be set to 'PHONE' or 'TABLET'.
            The FLEET_TYPE attribute can be set to 'PUBLIC' or 'PRIVATE'.
            (string) --
            
            

    :rtype: dict
    :return: {
        'devices': [
            {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    PHONE: The phone form factor.
    TABLET: The tablet form factor.
    
    """
    pass

def list_instance_profiles(maxResults=None, nextToken=None):
    """
    Returns information about all the instance profiles in an AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_instance_profiles(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: An integer specifying the maximum number of items you want to return in the API response.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'instanceProfiles': [
            {
                'arn': 'string',
                'packageCleanup': True|False,
                'excludeAppPackagesFromCleanup': [
                    'string',
                ],
                'rebootAfterUse': True|False,
                'name': 'string',
                'description': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_jobs(arn=None, nextToken=None):
    """
    Gets information about jobs for a given test run.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about jobs in a specific project.
    Expected Output:
    
    :example: response = client.list_jobs(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The run's Amazon Resource Name (ARN).
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'jobs': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'modelId': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string',
                    'instances': [
                        {
                            'arn': 'string',
                            'deviceArn': 'string',
                            'labels': [
                                'string',
                            ],
                            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                            'udid': 'string',
                            'instanceProfile': {
                                'arn': 'string',
                                'packageCleanup': True|False,
                                'excludeAppPackagesFromCleanup': [
                                    'string',
                                ],
                                'rebootAfterUse': True|False,
                                'name': 'string',
                                'description': 'string'
                            }
                        },
                    ],
                    'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                },
                'instanceArn': 'string',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'videoEndpoint': 'string',
                'videoCapture': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    BUILTIN_FUZZ: The built-in fuzz type.
    BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
    APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
    APPIUM_PYTHON: The Appium Python type.
    APPIUM_NODE: The Appium Node.js type.
    APPIUM_RUBY: The Appium Ruby type.
    APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
    APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
    APPIUM_WEB_PYTHON: The Appium Python type for web apps.
    APPIUM_WEB_NODE: The Appium Node.js type for web apps.
    APPIUM_WEB_RUBY: The Appium Ruby test type for web apps.
    CALABASH: The Calabash type.
    INSTRUMENTATION: The Instrumentation type.
    UIAUTOMATION: The uiautomation type.
    UIAUTOMATOR: The uiautomator type.
    XCTEST: The XCode test type.
    XCTEST_UI: The XCode UI test type.
    
    """
    pass

def list_network_profiles(arn=None, type=None, nextToken=None):
    """
    Returns the list of available network profiles.
    See also: AWS API Documentation
    
    
    :example: response = client.list_network_profiles(
        arn='string',
        type='CURATED'|'PRIVATE',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to list network profiles.
            

    :type type: string
    :param type: The type of network profile you wish to return information about. Valid values are listed below.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'networkProfiles': [
            {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_offering_promotions(nextToken=None):
    """
    Returns a list of offering promotions. Each offering promotion record contains the ID and description of the promotion. The API returns a NotEligible error if the caller is not permitted to invoke the operation. Contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
    
    :example: response = client.list_offering_promotions(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'offeringPromotions': [
            {
                'id': 'string',
                'description': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_offering_transactions(nextToken=None):
    """
    Returns a list of all historical purchases, renewals, and system renewal transactions for an AWS account. The list is paginated and ordered by a descending timestamp (most recent transactions are first). The API returns a NotEligible error if the user is not permitted to invoke the operation. Please contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about Device Farm offering transactions.
    Expected Output:
    
    :example: response = client.list_offering_transactions(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'offeringTransactions': [
            {
                'offeringStatus': {
                    'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                    'offering': {
                        'id': 'string',
                        'description': 'string',
                        'type': 'RECURRING',
                        'platform': 'ANDROID'|'IOS',
                        'recurringCharges': [
                            {
                                'cost': {
                                    'amount': 123.0,
                                    'currencyCode': 'USD'
                                },
                                'frequency': 'MONTHLY'
                            },
                        ]
                    },
                    'quantity': 123,
                    'effectiveOn': datetime(2015, 1, 1)
                },
                'transactionId': 'string',
                'offeringPromotionId': 'string',
                'createdOn': datetime(2015, 1, 1),
                'cost': {
                    'amount': 123.0,
                    'currencyCode': 'USD'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_offerings(nextToken=None):
    """
    Returns a list of products or offerings that the user can manage through the API. Each offering record indicates the recurring price per unit and the frequency for that offering. The API returns a NotEligible error if the user is not permitted to invoke the operation. Please contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about available device offerings.
    Expected Output:
    
    :example: response = client.list_offerings(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'offerings': [
            {
                'id': 'string',
                'description': 'string',
                'type': 'RECURRING',
                'platform': 'ANDROID'|'IOS',
                'recurringCharges': [
                    {
                        'cost': {
                            'amount': 123.0,
                            'currencyCode': 'USD'
                        },
                        'frequency': 'MONTHLY'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_projects(arn=None, nextToken=None):
    """
    Gets information about projects.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about the specified project in Device Farm.
    Expected Output:
    
    :example: response = client.list_projects(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: Optional. If no Amazon Resource Name (ARN) is specified, then AWS Device Farm returns a list of all projects for the AWS account. You can also specify a project ARN.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'projects': [
            {
                'arn': 'string',
                'name': 'string',
                'defaultJobTimeoutMinutes': 123,
                'created': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_remote_access_sessions(arn=None, nextToken=None):
    """
    Returns a list of all currently running remote access sessions.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about a specific Device Farm remote access session.
    Expected Output:
    
    :example: response = client.list_remote_access_sessions(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'remoteAccessSessions': [
            {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'message': 'string',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'modelId': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string',
                    'instances': [
                        {
                            'arn': 'string',
                            'deviceArn': 'string',
                            'labels': [
                                'string',
                            ],
                            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                            'udid': 'string',
                            'instanceProfile': {
                                'arn': 'string',
                                'packageCleanup': True|False,
                                'excludeAppPackagesFromCleanup': [
                                    'string',
                                ],
                                'rebootAfterUse': True|False,
                                'name': 'string',
                                'description': 'string'
                            }
                        },
                    ],
                    'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                },
                'instanceArn': 'string',
                'remoteDebugEnabled': True|False,
                'remoteRecordEnabled': True|False,
                'remoteRecordAppArn': 'string',
                'hostAddress': 'string',
                'clientId': 'string',
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'endpoint': 'string',
                'deviceUdid': 'string',
                'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
                'skipAppResign': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def list_runs(arn=None, nextToken=None):
    """
    Gets information about runs, given an AWS Device Farm project ARN.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about a specific test run.
    Expected Output:
    
    :example: response = client.list_runs(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to list runs.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'runs': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                'platform': 'ANDROID'|'IOS',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'totalJobs': 123,
                'completedJobs': 123,
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'networkProfile': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'uplinkBandwidthBits': 123,
                    'downlinkBandwidthBits': 123,
                    'uplinkDelayMs': 123,
                    'downlinkDelayMs': 123,
                    'uplinkJitterMs': 123,
                    'downlinkJitterMs': 123,
                    'uplinkLossPercent': 123,
                    'downlinkLossPercent': 123
                },
                'parsingResultUrl': 'string',
                'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
                'seed': 123,
                'appUpload': 'string',
                'eventCount': 123,
                'jobTimeoutMinutes': 123,
                'devicePoolArn': 'string',
                'locale': 'string',
                'radios': {
                    'wifi': True|False,
                    'bluetooth': True|False,
                    'nfc': True|False,
                    'gps': True|False
                },
                'location': {
                    'latitude': 123.0,
                    'longitude': 123.0
                },
                'customerArtifactPaths': {
                    'iosPaths': [
                        'string',
                    ],
                    'androidPaths': [
                        'string',
                    ],
                    'deviceHostPaths': [
                        'string',
                    ]
                },
                'webUrl': 'string',
                'skipAppResign': True|False,
                'testSpecArn': 'string',
                'deviceSelectionResult': {
                    'filters': [
                        {
                            'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                            'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                            'values': [
                                'string',
                            ]
                        },
                    ],
                    'matchedDevicesCount': 123,
                    'maxDevices': 123
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    BUILTIN_FUZZ: The built-in fuzz type.
    BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
    APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
    APPIUM_PYTHON: The Appium Python type.
    APPIUM_NODE: The Appium Node.js type.
    APPIUM_RUBY: The Appium Ruby type.
    APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
    APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
    APPIUM_WEB_PYTHON: The Appium Python type for web apps.
    APPIUM_WEB_NODE: The Appium Node.js type for web apps.
    APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
    CALABASH: The Calabash type.
    INSTRUMENTATION: The Instrumentation type.
    UIAUTOMATION: The uiautomation type.
    UIAUTOMATOR: The uiautomator type.
    XCTEST: The XCode test type.
    XCTEST_UI: The XCode UI test type.
    
    """
    pass

def list_samples(arn=None, nextToken=None):
    """
    Gets information about samples, given an AWS Device Farm job ARN.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about samples, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_samples(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the job used to list samples.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'samples': [
            {
                'arn': 'string',
                'type': 'CPU'|'MEMORY'|'THREADS'|'RX_RATE'|'TX_RATE'|'RX'|'TX'|'NATIVE_FRAMES'|'NATIVE_FPS'|'NATIVE_MIN_DRAWTIME'|'NATIVE_AVG_DRAWTIME'|'NATIVE_MAX_DRAWTIME'|'OPENGL_FRAMES'|'OPENGL_FPS'|'OPENGL_MIN_DRAWTIME'|'OPENGL_AVG_DRAWTIME'|'OPENGL_MAX_DRAWTIME',
                'url': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CPU: A CPU sample type. This is expressed as the app processing CPU time (including child processes) as reported by process, as a percentage.
    MEMORY: A memory usage sample type. This is expressed as the total proportional set size of an app process, in kilobytes.
    NATIVE_AVG_DRAWTIME
    NATIVE_FPS
    NATIVE_FRAMES
    NATIVE_MAX_DRAWTIME
    NATIVE_MIN_DRAWTIME
    OPENGL_AVG_DRAWTIME
    OPENGL_FPS
    OPENGL_FRAMES
    OPENGL_MAX_DRAWTIME
    OPENGL_MIN_DRAWTIME
    RX
    RX_RATE: The total number of bytes per second (TCP and UDP) that are sent, by app process.
    THREADS: A threads sample type. This is expressed as the total number of threads per app process.
    TX
    TX_RATE: The total number of bytes per second (TCP and UDP) that are received, by app process.
    
    """
    pass

def list_suites(arn=None, nextToken=None):
    """
    Gets information about test suites for a given job.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about suites, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_suites(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The job's Amazon Resource Name (ARN).
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'suites': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    BUILTIN_FUZZ: The built-in fuzz type.
    BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
    APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
    APPIUM_PYTHON: The Appium Python type.
    APPIUM_NODE: The Appium Node.js type.
    APPIUM_RUBY: The Appium Ruby type.
    APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
    APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
    APPIUM_WEB_PYTHON: The Appium Python type for web apps.
    APPIUM_WEB_NODE: The Appium Node.js type for web apps.
    APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
    CALABASH: The Calabash type.
    INSTRUMENTATION: The Instrumentation type.
    UIAUTOMATION: The uiautomation type.
    UIAUTOMATOR: The uiautomator type.
    XCTEST: The XCode test type.
    XCTEST_UI: The XCode UI test type.
    
    """
    pass

def list_tests(arn=None, nextToken=None):
    """
    Gets information about tests in a given test suite.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about tests, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_tests(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The test suite's Amazon Resource Name (ARN).
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'tests': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    BUILTIN_FUZZ: The built-in fuzz type.
    BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
    APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
    APPIUM_PYTHON: The Appium Python type.
    APPIUM_NODE: The Appium Node.js type.
    APPIUM_RUBY: The Appium Ruby type.
    APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
    APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
    APPIUM_WEB_PYTHON: The Appium Python type for web apps.
    APPIUM_WEB_NODE: The Appium Node.js type for web apps.
    APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
    CALABASH: The Calabash type.
    INSTRUMENTATION: The Instrumentation type.
    UIAUTOMATION: The uiautomation type.
    UIAUTOMATOR: The uiautomator type.
    XCTEST: The XCode test type.
    XCTEST_UI: The XCode UI test type.
    
    """
    pass

def list_unique_problems(arn=None, nextToken=None):
    """
    Gets information about unique problems.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about unique problems, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_unique_problems(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The unique problems' ARNs.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'uniqueProblems': {
            'string': [
                {
                    'message': 'string',
                    'problems': [
                        {
                            'run': {
                                'arn': 'string',
                                'name': 'string'
                            },
                            'job': {
                                'arn': 'string',
                                'name': 'string'
                            },
                            'suite': {
                                'arn': 'string',
                                'name': 'string'
                            },
                            'test': {
                                'arn': 'string',
                                'name': 'string'
                            },
                            'device': {
                                'arn': 'string',
                                'name': 'string',
                                'manufacturer': 'string',
                                'model': 'string',
                                'modelId': 'string',
                                'formFactor': 'PHONE'|'TABLET',
                                'platform': 'ANDROID'|'IOS',
                                'os': 'string',
                                'cpu': {
                                    'frequency': 'string',
                                    'architecture': 'string',
                                    'clock': 123.0
                                },
                                'resolution': {
                                    'width': 123,
                                    'height': 123
                                },
                                'heapSize': 123,
                                'memory': 123,
                                'image': 'string',
                                'carrier': 'string',
                                'radio': 'string',
                                'remoteAccessEnabled': True|False,
                                'remoteDebugEnabled': True|False,
                                'fleetType': 'string',
                                'fleetName': 'string',
                                'instances': [
                                    {
                                        'arn': 'string',
                                        'deviceArn': 'string',
                                        'labels': [
                                            'string',
                                        ],
                                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                        'udid': 'string',
                                        'instanceProfile': {
                                            'arn': 'string',
                                            'packageCleanup': True|False,
                                            'excludeAppPackagesFromCleanup': [
                                                'string',
                                            ],
                                            'rebootAfterUse': True|False,
                                            'name': 'string',
                                            'description': 'string'
                                        }
                                    },
                                ],
                                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                            },
                            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                            'message': 'string'
                        },
                    ]
                },
            ]
        },
        'nextToken': 'string'
    }
    
    
    :returns: 
    PENDING: A pending condition.
    PASSED: A passing condition.
    WARNED: A warning condition.
    FAILED: A failed condition.
    SKIPPED: A skipped condition.
    ERRORED: An error condition.
    STOPPED: A stopped condition.
    
    """
    pass

def list_uploads(arn=None, type=None, nextToken=None):
    """
    Gets information about uploads, given an AWS Device Farm project ARN.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about uploads, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_uploads(
        arn='string',
        type='ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to list uploads.
            

    :type type: string
    :param type: The type of upload.
            Must be one of the following values:
            ANDROID_APP: An Android upload.
            IOS_APP: An iOS upload.
            WEB_APP: A web appliction upload.
            EXTERNAL_DATA: An external data upload.
            APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
            APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
            APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
            APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload.
            APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload.
            APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for a web app.
            APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for a web app.
            APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for a web app.
            APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for a web app.
            APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for a web app.
            CALABASH_TEST_PACKAGE: A Calabash test package upload.
            INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
            UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
            UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
            XCTEST_TEST_PACKAGE: An XCode test package upload.
            XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
            APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload.
            APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload.
            APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload.
            APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload.
            APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload.
            APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app.
            APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app.
            APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app.
            APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app.
            APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app.
            INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload.
            XCTEST_UI_TEST_SPEC: An XCode UI test spec upload.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'uploads': [
            {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
                'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                'url': 'string',
                'metadata': 'string',
                'contentType': 'string',
                'message': 'string',
                'category': 'CURATED'|'PRIVATE'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    ANDROID_APP: An Android upload.
    IOS_APP: An iOS upload.
    WEB_APP: A web appliction upload.
    EXTERNAL_DATA: An external data upload.
    APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
    APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
    APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
    APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload.
    APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for web apps.
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for web apps.
    APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for web apps.
    APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for web apps.
    APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for web apps.
    CALABASH_TEST_PACKAGE: A Calabash test package upload.
    INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
    UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
    UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
    XCTEST_TEST_PACKAGE: An XCode test package upload.
    XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
    APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload.
    APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload.
    APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload.
    APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload.
    APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app.
    APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app.
    APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app.
    APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app.
    APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app.
    INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload.
    XCTEST_UI_TEST_SPEC: An XCode UI test spec upload.
    
    """
    pass

def list_vpce_configurations(maxResults=None, nextToken=None):
    """
    Returns information about all Amazon Virtual Private Cloud (VPC) endpoint configurations in the AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_vpce_configurations(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: An integer specifying the maximum number of items you want to return in the API response.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'vpceConfigurations': [
            {
                'arn': 'string',
                'vpceConfigurationName': 'string',
                'vpceServiceName': 'string',
                'serviceDnsName': 'string',
                'vpceConfigurationDescription': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def purchase_offering(offeringId=None, quantity=None, offeringPromotionId=None):
    """
    Immediately purchases offerings for an AWS account. Offerings renew with the latest total purchased quantity for an offering, unless the renewal was overridden. The API returns a NotEligible error if the user is not permitted to invoke the operation. Please contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
    Examples
    The following example purchases a specific device slot offering.
    Expected Output:
    
    :example: response = client.purchase_offering(
        offeringId='string',
        quantity=123,
        offeringPromotionId='string'
    )
    
    
    :type offeringId: string
    :param offeringId: The ID of the offering.

    :type quantity: integer
    :param quantity: The number of device slots you wish to purchase in an offering request.

    :type offeringPromotionId: string
    :param offeringPromotionId: The ID of the offering promotion to be applied to the purchase.

    :rtype: dict
    :return: {
        'offeringTransaction': {
            'offeringStatus': {
                'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                'offering': {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
                'quantity': 123,
                'effectiveOn': datetime(2015, 1, 1)
            },
            'transactionId': 'string',
            'offeringPromotionId': 'string',
            'createdOn': datetime(2015, 1, 1),
            'cost': {
                'amount': 123.0,
                'currencyCode': 'USD'
            }
        }
    }
    
    
    """
    pass

def renew_offering(offeringId=None, quantity=None):
    """
    Explicitly sets the quantity of devices to renew for an offering, starting from the effectiveDate of the next period. The API returns a NotEligible error if the user is not permitted to invoke the operation. Please contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
    Examples
    The following example renews a specific device slot offering.
    Expected Output:
    
    :example: response = client.renew_offering(
        offeringId='string',
        quantity=123
    )
    
    
    :type offeringId: string
    :param offeringId: The ID of a request to renew an offering.

    :type quantity: integer
    :param quantity: The quantity requested in an offering renewal.

    :rtype: dict
    :return: {
        'offeringTransaction': {
            'offeringStatus': {
                'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                'offering': {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
                'quantity': 123,
                'effectiveOn': datetime(2015, 1, 1)
            },
            'transactionId': 'string',
            'offeringPromotionId': 'string',
            'createdOn': datetime(2015, 1, 1),
            'cost': {
                'amount': 123.0,
                'currencyCode': 'USD'
            }
        }
    }
    
    
    """
    pass

def schedule_run(projectArn=None, appArn=None, devicePoolArn=None, deviceSelectionConfiguration=None, name=None, test=None, configuration=None, executionConfiguration=None):
    """
    Schedules a run.
    See also: AWS API Documentation
    
    Examples
    The following example schedules a test run named MyRun.
    Expected Output:
    
    :example: response = client.schedule_run(
        projectArn='string',
        appArn='string',
        devicePoolArn='string',
        deviceSelectionConfiguration={
            'filters': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                    'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                    'values': [
                        'string',
                    ]
                },
            ],
            'maxDevices': 123
        },
        name='string',
        test={
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'testPackageArn': 'string',
            'testSpecArn': 'string',
            'filter': 'string',
            'parameters': {
                'string': 'string'
            }
        },
        configuration={
            'extraDataPackageArn': 'string',
            'networkProfileArn': 'string',
            'locale': 'string',
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'vpceConfigurationArns': [
                'string',
            ],
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'auxiliaryApps': [
                'string',
            ],
            'billingMethod': 'METERED'|'UNMETERED'
        },
        executionConfiguration={
            'jobTimeoutMinutes': 123,
            'accountsCleanup': True|False,
            'appPackagesCleanup': True|False,
            'videoCapture': True|False,
            'skipAppResign': True|False
        }
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]
            The ARN of the project for the run to be scheduled.
            

    :type appArn: string
    :param appArn: The ARN of the app to schedule a run.

    :type devicePoolArn: string
    :param devicePoolArn: The ARN of the device pool for the run to be scheduled.
            Either ** devicePoolArn ** or ** deviceSelectionConfiguration ** is required in a request.
            

    :type deviceSelectionConfiguration: dict
    :param deviceSelectionConfiguration: The filter criteria used to dynamically select a set of devices for a test run, as well as the maximum number of devices to be included in the run.
            Either ** devicePoolArn ** or ** deviceSelectionConfiguration ** is required in a request.
            filters (list) -- [REQUIRED]Used to dynamically select a set of devices for a test run. A filter is made up of an attribute, an operator, and one or more values.
            Attribute  The aspect of a device such as platform or model used as the selection criteria in a device filter. Allowed values include:
            ARN: The Amazon Resource Name (ARN) of the device. For example, 'arn:aws:devicefarm:us-west-2::device:12345Example'.
            PLATFORM: The device platform. Valid values are 'ANDROID' or 'IOS'.
            OS_VERSION: The operating system version. For example, '10.3.2'.
            MODEL: The device model. For example, 'iPad 5th Gen'.
            AVAILABILITY: The current availability of the device. Valid values are 'AVAILABLE', 'HIGHLY_AVAILABLE', 'BUSY', or 'TEMPORARY_NOT_AVAILABLE'.
            FORM_FACTOR: The device form factor. Valid values are 'PHONE' or 'TABLET'.
            MANUFACTURER: The device manufacturer. For example, 'Apple'.
            REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are 'TRUE' or 'FALSE'.
            REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are 'TRUE' or 'FALSE'.
            INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
            INSTANCE_LABELS: The label of the device instance.
            FLEET_TYPE: The fleet type. Valid values are 'PUBLIC' or 'PRIVATE'.
            Operator  The filter operator.
            The EQUALS operator is available for every attribute except INSTANCE_LABELS.
            The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.
            The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.
            The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.
            Values  An array of one or more filter values. Operator Values
            The IN and NOT_IN operators can take a values array that has more than one element.
            The other operators require an array with a single element.
            
            Attribute Values
            The PLATFORM attribute can be set to 'ANDROID' or 'IOS'.
            The AVAILABILITY attribute can be set to 'AVAILABLE', 'HIGHLY_AVAILABLE', 'BUSY', or 'TEMPORARY_NOT_AVAILABLE'.
            The FORM_FACTOR attribute can be set to 'PHONE' or 'TABLET'.
            The FLEET_TYPE attribute can be set to 'PUBLIC' or 'PRIVATE'.
            
            (dict) --Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the deviceSelectionConfiguration parameter to ScheduleRun. For an example of the JSON request syntax, see ScheduleRun .
            It is also passed in as the filters parameter to ListDevices. For an example of the JSON request syntax, see ListDevices .
            attribute (string) --The aspect of a device such as platform or model used as the selection criteria in a device filter.
            Allowed values include:
            ARN: The Amazon Resource Name (ARN) of the device. For example, 'arn:aws:devicefarm:us-west-2::device:12345Example'.
            PLATFORM: The device platform. Valid values are 'ANDROID' or 'IOS'.
            OS_VERSION: The operating system version. For example, '10.3.2'.
            MODEL: The device model. For example, 'iPad 5th Gen'.
            AVAILABILITY: The current availability of the device. Valid values are 'AVAILABLE', 'HIGHLY_AVAILABLE', 'BUSY', or 'TEMPORARY_NOT_AVAILABLE'.
            FORM_FACTOR: The device form factor. Valid values are 'PHONE' or 'TABLET'.
            MANUFACTURER: The device manufacturer. For example, 'Apple'.
            REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are 'TRUE' or 'FALSE'.
            REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are 'TRUE' or 'FALSE'.
            INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
            INSTANCE_LABELS: The label of the device instance.
            FLEET_TYPE: The fleet type. Valid values are 'PUBLIC' or 'PRIVATE'.
            operator (string) --The filter operator.
            The EQUALS operator is available for every attribute except INSTANCE_LABELS.
            The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.
            The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.
            The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.
            values (list) --An array of one or more filter values used in a device filter.
            Operator Values
            The IN and NOT_IN operators can take a values array that has more than one element.
            The other operators require an array with a single element.
            Attribute Values
            The PLATFORM attribute can be set to 'ANDROID' or 'IOS'.
            The AVAILABILITY attribute can be set to 'AVAILABLE', 'HIGHLY_AVAILABLE', 'BUSY', or 'TEMPORARY_NOT_AVAILABLE'.
            The FORM_FACTOR attribute can be set to 'PHONE' or 'TABLET'.
            The FLEET_TYPE attribute can be set to 'PUBLIC' or 'PRIVATE'.
            (string) --
            
            maxDevices (integer) -- [REQUIRED]The maximum number of devices to be included in a test run.
            

    :type name: string
    :param name: The name for the run to be scheduled.

    :type test: dict
    :param test: [REQUIRED]
            Information about the test for the run to be scheduled.
            type (string) -- [REQUIRED]The test's type.
            Must be one of the following values:
            BUILTIN_FUZZ: The built-in fuzz type.
            BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
            APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
            APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
            APPIUM_PYTHON: The Appium Python type.
            APPIUM_NODE: The Appium Node.js type.
            APPIUM_RUBY: The Appium Ruby type.
            APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
            APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
            APPIUM_WEB_PYTHON: The Appium Python type for web apps.
            APPIUM_WEB_NODE: The Appium Node.js type for web apps.
            APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
            CALABASH: The Calabash type.
            INSTRUMENTATION: The Instrumentation type.
            UIAUTOMATION: The uiautomation type.
            UIAUTOMATOR: The uiautomator type.
            XCTEST: The XCode test type.
            XCTEST_UI: The XCode UI test type.
            testPackageArn (string) --The ARN of the uploaded test that will be run.
            testSpecArn (string) --The ARN of the YAML-formatted test specification.
            filter (string) --The test's filter.
            parameters (dict) --The test's parameters, such as test framework parameters and fixture settings. Parameters are represented by name-value pairs of strings.
            For all tests:
            app_performance_monitoring: Performance monitoring is enabled by default. Set this parameter to 'false' to disable it.
            For Calabash tests:
            profile: A cucumber profile, for example, 'my_profile_name'.
            tags: You can limit execution to features or scenarios that have (or don't have) certain tags, for example, '@smoke' or '@smoke,~@wip'.
            For Appium tests (all types):
            appium_version: The Appium version. Currently supported values are '1.6.5' (and higher), 'latest', and 'default'.
             latest  will run the latest Appium version supported by Device Farm (1.9.1).
            For  default , Device Farm will choose a compatible version of Appium for the device. The current behavior is to run 1.7.2 on Android devices and iOS 9 and earlier, 1.7.2 for iOS 10 and later.
            This behavior is subject to change.
            For Fuzz tests (Android only):
            event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.
            throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.
            seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
            For Explorer tests:
            username: A username to use if the Explorer encounters a login form. If not supplied, no username will be inserted.
            password: A password to use if the Explorer encounters a login form. If not supplied, no password will be inserted.
            For Instrumentation:
            filter: A test filter string. Examples:
            Running a single test case: 'com.android.abc.Test1'
            Running a single test: 'com.android.abc.Test1#smoke'
            Running multiple tests: 'com.android.abc.Test1,com.android.abc.Test2'
            For XCTest and XCTestUI:
            filter: A test filter string. Examples:
            Running a single test class: 'LoginTests'
            Running a multiple test classes: 'LoginTests,SmokeTests'
            Running a single test: 'LoginTests/testValid'
            Running multiple tests: 'LoginTests/testValid,LoginTests/testInvalid'
            For UIAutomator:
            filter: A test filter string. Examples:
            Running a single test case: 'com.android.abc.Test1'
            Running a single test: 'com.android.abc.Test1#smoke'
            Running multiple tests: 'com.android.abc.Test1,com.android.abc.Test2'
            
            (string) --
            (string) --
            
            

    :type configuration: dict
    :param configuration: Information about the settings for the run to be scheduled.
            extraDataPackageArn (string) --The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm will extract to external data for Android or the app's sandbox for iOS.
            networkProfileArn (string) --Reserved for internal use.
            locale (string) --Information about the locale that is used for the run.
            location (dict) --Information about the location that is used for the run.
            latitude (float) -- [REQUIRED]The latitude.
            longitude (float) -- [REQUIRED]The longitude.
            vpceConfigurationArns (list) --An array of Amazon Resource Names (ARNs) for your VPC endpoint configurations.
            (string) --
            customerArtifactPaths (dict) --Input CustomerArtifactPaths object for the scheduled run configuration.
            iosPaths (list) --Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.
            (string) --
            androidPaths (list) --Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.
            (string) --
            deviceHostPaths (list) --Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.
            (string) --
            
            radios (dict) --Information about the radio states for the run.
            wifi (boolean) --True if Wi-Fi is enabled at the beginning of the test; otherwise, false.
            bluetooth (boolean) --True if Bluetooth is enabled at the beginning of the test; otherwise, false.
            nfc (boolean) --True if NFC is enabled at the beginning of the test; otherwise, false.
            gps (boolean) --True if GPS is enabled at the beginning of the test; otherwise, false.
            auxiliaryApps (list) --A list of auxiliary apps for the run.
            (string) --
            billingMethod (string) --Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is metered .
            

    :type executionConfiguration: dict
    :param executionConfiguration: Specifies configuration information about a test run, such as the execution timeout (in minutes).
            jobTimeoutMinutes (integer) --The number of minutes a test run will execute before it times out.
            accountsCleanup (boolean) --True if account cleanup is enabled at the beginning of the test; otherwise, false.
            appPackagesCleanup (boolean) --True if app package cleanup is enabled at the beginning of the test; otherwise, false.
            videoCapture (boolean) --Set to true to enable video capture; otherwise, set to false. The default is true.
            skipAppResign (boolean) --When set to true , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
            For more information about how Device Farm re-signs your app(s), see Do you modify my app? in the AWS Device Farm FAQs .
            

    :rtype: dict
    :return: {
        'run': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'platform': 'ANDROID'|'IOS',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'totalJobs': 123,
            'completedJobs': 123,
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'networkProfile': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            },
            'parsingResultUrl': 'string',
            'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
            'seed': 123,
            'appUpload': 'string',
            'eventCount': 123,
            'jobTimeoutMinutes': 123,
            'devicePoolArn': 'string',
            'locale': 'string',
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'webUrl': 'string',
            'skipAppResign': True|False,
            'testSpecArn': 'string',
            'deviceSelectionResult': {
                'filters': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                        'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                        'values': [
                            'string',
                        ]
                    },
                ],
                'matchedDevicesCount': 123,
                'maxDevices': 123
            }
        }
    }
    
    
    :returns: 
    BUILTIN_FUZZ: The built-in fuzz type.
    BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
    APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
    APPIUM_PYTHON: The Appium Python type.
    APPIUM_NODE: The Appium Node.js type.
    APPIUM_RUBY: The Appium Ruby type.
    APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
    APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
    APPIUM_WEB_PYTHON: The Appium Python type for web apps.
    APPIUM_WEB_NODE: The Appium Node.js type for web apps.
    APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
    CALABASH: The Calabash type.
    INSTRUMENTATION: The Instrumentation type.
    UIAUTOMATION: The uiautomation type.
    UIAUTOMATOR: The uiautomator type.
    XCTEST: The XCode test type.
    XCTEST_UI: The XCode UI test type.
    
    """
    pass

def stop_job(arn=None):
    """
    Initiates a stop request for the current job. AWS Device Farm will immediately stop the job on the device where tests have not started executing, and you will not be billed for this device. On the device where tests have started executing, Setup Suite and Teardown Suite tests will run to completion before stopping execution on the device. You will be billed for Setup, Teardown, and any tests that were in progress or already completed.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_job(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm job you wish to stop.
            

    :rtype: dict
    :return: {
        'job': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'videoEndpoint': 'string',
            'videoCapture': True|False
        }
    }
    
    
    :returns: 
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def stop_remote_access_session(arn=None):
    """
    Ends a specified remote access session.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_remote_access_session(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session you wish to stop.
            

    :rtype: dict
    :return: {
        'remoteAccessSession': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'message': 'string',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'remoteDebugEnabled': True|False,
            'remoteRecordEnabled': True|False,
            'remoteRecordAppArn': 'string',
            'hostAddress': 'string',
            'clientId': 'string',
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'endpoint': 'string',
            'deviceUdid': 'string',
            'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
            'skipAppResign': True|False
        }
    }
    
    
    :returns: 
    PENDING: A pending condition.
    PASSED: A passing condition.
    WARNED: A warning condition.
    FAILED: A failed condition.
    SKIPPED: A skipped condition.
    ERRORED: An error condition.
    STOPPED: A stopped condition.
    
    """
    pass

def stop_run(arn=None):
    """
    Initiates a stop request for the current test run. AWS Device Farm will immediately stop the run on devices where tests have not started executing, and you will not be billed for these devices. On devices where tests have started executing, Setup Suite and Teardown Suite tests will run to completion before stopping execution on those devices. You will be billed for Setup, Teardown, and any tests that were in progress or already completed.
    See also: AWS API Documentation
    
    Examples
    The following example stops a specific test run.
    Expected Output:
    
    :example: response = client.stop_run(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm run you wish to stop.
            

    :rtype: dict
    :return: {
        'run': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'platform': 'ANDROID'|'IOS',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'totalJobs': 123,
            'completedJobs': 123,
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'networkProfile': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            },
            'parsingResultUrl': 'string',
            'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
            'seed': 123,
            'appUpload': 'string',
            'eventCount': 123,
            'jobTimeoutMinutes': 123,
            'devicePoolArn': 'string',
            'locale': 'string',
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'webUrl': 'string',
            'skipAppResign': True|False,
            'testSpecArn': 'string',
            'deviceSelectionResult': {
                'filters': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                        'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                        'values': [
                            'string',
                        ]
                    },
                ],
                'matchedDevicesCount': 123,
                'maxDevices': 123
            }
        }
    }
    
    
    :returns: 
    ANDROID: The Android platform.
    IOS: The iOS platform.
    
    """
    pass

def update_device_instance(arn=None, profileArn=None, labels=None):
    """
    Updates information about an existing private device instance.
    See also: AWS API Documentation
    
    
    :example: response = client.update_device_instance(
        arn='string',
        profileArn='string',
        labels=[
            'string',
        ]
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the device instance.
            

    :type profileArn: string
    :param profileArn: The Amazon Resource Name (ARN) of the profile that you want to associate with the device instance.

    :type labels: list
    :param labels: An array of strings that you want to associate with the device instance.
            (string) --
            

    :rtype: dict
    :return: {
        'deviceInstance': {
            'arn': 'string',
            'deviceArn': 'string',
            'labels': [
                'string',
            ],
            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
            'udid': 'string',
            'instanceProfile': {
                'arn': 'string',
                'packageCleanup': True|False,
                'excludeAppPackagesFromCleanup': [
                    'string',
                ],
                'rebootAfterUse': True|False,
                'name': 'string',
                'description': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_device_pool(arn=None, name=None, description=None, rules=None):
    """
    Modifies the name, description, and rules in a device pool given the attributes and the pool ARN. Rule updates are all-or-nothing, meaning they can only be updated as a whole (or not at all).
    See also: AWS API Documentation
    
    Examples
    The following example updates the specified device pool with a new name and description. It also enables remote access of devices in the device pool.
    Expected Output:
    
    :example: response = client.update_device_pool(
        arn='string',
        name='string',
        description='string',
        rules=[
            {
                'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                'value': 'string'
            },
        ]
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resourc Name (ARN) of the Device Farm device pool you wish to update.
            

    :type name: string
    :param name: A string representing the name of the device pool you wish to update.

    :type description: string
    :param description: A description of the device pool you wish to update.

    :type rules: list
    :param rules: Represents the rules you wish to modify for the device pool. Updating rules is optional; however, if you choose to update rules for your request, the update will replace the existing rules.
            (dict) --Represents a condition for a device pool. It is passed in as the rules parameter to CreateDevicePool and UpdateDevicePool .
            attribute (string) --The rule's attribute. It is the aspect of a device such as platform or model used as selection criteria to create or update a device pool.
            Allowed values include:
            ARN: The Amazon Resource Name (ARN) of a device. For example, 'arn:aws:devicefarm:us-west-2::device:12345Example'.
            PLATFORM: The device platform. Valid values are 'ANDROID' or 'IOS'.
            FORM_FACTOR: The device form factor. Valid values are 'PHONE' or 'TABLET'.
            MANUFACTURER: The device manufacturer. For example, 'Apple'.
            REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are 'TRUE' or 'FALSE'.
            REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are 'TRUE' or 'FALSE'.
            APPIUM_VERSION: The Appium version for the test.
            INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
            INSTANCE_LABELS: The label of the device instance.
            FLEET_TYPE: The fleet type. Valid values are 'PUBLIC' or 'PRIVATE'.
            operator (string) --The rule's operator.
            EQUALS: The equals operator.
            GREATER_THAN: The greater-than operator.
            IN: The in operator.
            LESS_THAN: The less-than operator.
            NOT_IN: The not-in operator.
            CONTAINS: The contains operator.
            value (string) --The rule's value.
            The value must be passed in as a string using escaped quotes.
            For example:
            'value': ''ANDROID''
            
            

    :rtype: dict
    :return: {
        'devicePool': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'rules': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                    'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CURATED: A device pool that is created and managed by AWS Device Farm.
    PRIVATE: A device pool that is created and managed by the device pool developer.
    
    """
    pass

def update_instance_profile(arn=None, name=None, description=None, packageCleanup=None, excludeAppPackagesFromCleanup=None, rebootAfterUse=None):
    """
    Updates information about an existing private device instance profile.
    See also: AWS API Documentation
    
    
    :example: response = client.update_instance_profile(
        arn='string',
        name='string',
        description='string',
        packageCleanup=True|False,
        excludeAppPackagesFromCleanup=[
            'string',
        ],
        rebootAfterUse=True|False
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the instance profile.
            

    :type name: string
    :param name: The updated name for your instance profile.

    :type description: string
    :param description: The updated description for your instance profile.

    :type packageCleanup: boolean
    :param packageCleanup: The updated choice for whether you want to specify package cleanup. The default value is false for private devices.

    :type excludeAppPackagesFromCleanup: list
    :param excludeAppPackagesFromCleanup: An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
            The list of packages is only considered if you set packageCleanup to true .
            (string) --
            

    :type rebootAfterUse: boolean
    :param rebootAfterUse: The updated choice for whether you want to reboot the device after use. The default value is true .

    :rtype: dict
    :return: {
        'instanceProfile': {
            'arn': 'string',
            'packageCleanup': True|False,
            'excludeAppPackagesFromCleanup': [
                'string',
            ],
            'rebootAfterUse': True|False,
            'name': 'string',
            'description': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_network_profile(arn=None, name=None, description=None, type=None, uplinkBandwidthBits=None, downlinkBandwidthBits=None, uplinkDelayMs=None, downlinkDelayMs=None, uplinkJitterMs=None, downlinkJitterMs=None, uplinkLossPercent=None, downlinkLossPercent=None):
    """
    Updates the network profile with specific settings.
    See also: AWS API Documentation
    
    
    :example: response = client.update_network_profile(
        arn='string',
        name='string',
        description='string',
        type='CURATED'|'PRIVATE',
        uplinkBandwidthBits=123,
        downlinkBandwidthBits=123,
        uplinkDelayMs=123,
        downlinkDelayMs=123,
        uplinkJitterMs=123,
        downlinkJitterMs=123,
        uplinkLossPercent=123,
        downlinkLossPercent=123
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to update network profile settings.
            

    :type name: string
    :param name: The name of the network profile about which you are returning information.

    :type description: string
    :param description: The descriptoin of the network profile about which you are returning information.

    :type type: string
    :param type: The type of network profile you wish to return information about. Valid values are listed below.

    :type uplinkBandwidthBits: integer
    :param uplinkBandwidthBits: The data throughput rate in bits per second, as an integer from 0 to 104857600.

    :type downlinkBandwidthBits: integer
    :param downlinkBandwidthBits: The data throughput rate in bits per second, as an integer from 0 to 104857600.

    :type uplinkDelayMs: integer
    :param uplinkDelayMs: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

    :type downlinkDelayMs: integer
    :param downlinkDelayMs: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

    :type uplinkJitterMs: integer
    :param uplinkJitterMs: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

    :type downlinkJitterMs: integer
    :param downlinkJitterMs: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

    :type uplinkLossPercent: integer
    :param uplinkLossPercent: Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

    :type downlinkLossPercent: integer
    :param downlinkLossPercent: Proportion of received packets that fail to arrive from 0 to 100 percent.

    :rtype: dict
    :return: {
        'networkProfile': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'uplinkBandwidthBits': 123,
            'downlinkBandwidthBits': 123,
            'uplinkDelayMs': 123,
            'downlinkDelayMs': 123,
            'uplinkJitterMs': 123,
            'downlinkJitterMs': 123,
            'uplinkLossPercent': 123,
            'downlinkLossPercent': 123
        }
    }
    
    
    """
    pass

def update_project(arn=None, name=None, defaultJobTimeoutMinutes=None):
    """
    Modifies the specified project name, given the project ARN and a new name.
    See also: AWS API Documentation
    
    Examples
    The following example updates the specified project with a new name.
    Expected Output:
    
    :example: response = client.update_project(
        arn='string',
        name='string',
        defaultJobTimeoutMinutes=123
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project whose name you wish to update.
            

    :type name: string
    :param name: A string representing the new name of the project that you are updating.

    :type defaultJobTimeoutMinutes: integer
    :param defaultJobTimeoutMinutes: The number of minutes a test run in the project will execute before it times out.

    :rtype: dict
    :return: {
        'project': {
            'arn': 'string',
            'name': 'string',
            'defaultJobTimeoutMinutes': 123,
            'created': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def update_upload(arn=None, name=None, contentType=None, editContent=None):
    """
    Update an uploaded test specification (test spec).
    See also: AWS API Documentation
    
    
    :example: response = client.update_upload(
        arn='string',
        name='string',
        contentType='string',
        editContent=True|False
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the uploaded test spec.
            

    :type name: string
    :param name: The upload's test spec file name. The name should not contain the '/' character. The test spec file name must end with the .yaml or .yml file extension.

    :type contentType: string
    :param contentType: The upload's content type (for example, 'application/x-yaml').

    :type editContent: boolean
    :param editContent: Set to true if the YAML file has changed and needs to be updated; otherwise, set to false.

    :rtype: dict
    :return: {
        'upload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string',
            'category': 'CURATED'|'PRIVATE'
        }
    }
    
    
    :returns: 
    ANDROID_APP: An Android upload.
    IOS_APP: An iOS upload.
    WEB_APP: A web appliction upload.
    EXTERNAL_DATA: An external data upload.
    APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
    APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
    APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
    APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload.
    APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for web apps.
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for web apps.
    APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for web apps.
    APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for web apps.
    APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for web apps.
    CALABASH_TEST_PACKAGE: A Calabash test package upload.
    INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
    UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
    UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
    XCTEST_TEST_PACKAGE: An XCode test package upload.
    XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
    APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload.
    APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload.
    APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload.
    APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload.
    APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app.
    APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app.
    APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app.
    APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app.
    APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app.
    INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload.
    XCTEST_UI_TEST_SPEC: An XCode UI test spec upload.
    
    """
    pass

def update_vpce_configuration(arn=None, vpceConfigurationName=None, vpceServiceName=None, serviceDnsName=None, vpceConfigurationDescription=None):
    """
    Updates information about an existing Amazon Virtual Private Cloud (VPC) endpoint configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.update_vpce_configuration(
        arn='string',
        vpceConfigurationName='string',
        vpceServiceName='string',
        serviceDnsName='string',
        vpceConfigurationDescription='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to update.
            

    :type vpceConfigurationName: string
    :param vpceConfigurationName: The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.

    :type vpceServiceName: string
    :param vpceServiceName: The name of the VPC endpoint service running inside your AWS account that you want Device Farm to test.

    :type serviceDnsName: string
    :param serviceDnsName: The DNS (domain) name used to connect to your private service in your Amazon VPC. The DNS name must not already be in use on the Internet.

    :type vpceConfigurationDescription: string
    :param vpceConfigurationDescription: An optional description, providing more details about your VPC endpoint configuration.

    :rtype: dict
    :return: {
        'vpceConfiguration': {
            'arn': 'string',
            'vpceConfigurationName': 'string',
            'vpceServiceName': 'string',
            'serviceDnsName': 'string',
            'vpceConfigurationDescription': 'string'
        }
    }
    
    
    """
    pass

