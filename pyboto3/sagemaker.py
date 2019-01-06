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

def add_tags(ResourceArn=None, Tags=None):
    """
    Adds or overwrites one or more tags for the specified Amazon SageMaker resource. You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, models, endpoint configurations, and endpoints.
    Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see For more information, see AWS Tagging Strategies .
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource that you want to tag.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            An array of Tag objects. Each tag is a key-value pair. Only the key parameter is required. If you don't specify a value, Amazon SageMaker sets the value to an empty string.
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
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

def create_algorithm(AlgorithmName=None, AlgorithmDescription=None, TrainingSpecification=None, InferenceSpecification=None, ValidationSpecification=None, CertifyForMarketplace=None):
    """
    Create a machine learning algorithm that you can use in Amazon SageMaker and list in the AWS Marketplace.
    See also: AWS API Documentation
    
    
    :example: response = client.create_algorithm(
        AlgorithmName='string',
        AlgorithmDescription='string',
        TrainingSpecification={
            'TrainingImage': 'string',
            'TrainingImageDigest': 'string',
            'SupportedHyperParameters': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'Integer'|'Continuous'|'Categorical'|'FreeText',
                    'Range': {
                        'IntegerParameterRangeSpecification': {
                            'MinValue': 'string',
                            'MaxValue': 'string'
                        },
                        'ContinuousParameterRangeSpecification': {
                            'MinValue': 'string',
                            'MaxValue': 'string'
                        },
                        'CategoricalParameterRangeSpecification': {
                            'Values': [
                                'string',
                            ]
                        }
                    },
                    'IsTunable': True|False,
                    'IsRequired': True|False,
                    'DefaultValue': 'string'
                },
            ],
            'SupportedTrainingInstanceTypes': [
                'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
            ],
            'SupportsDistributedTraining': True|False,
            'MetricDefinitions': [
                {
                    'Name': 'string',
                    'Regex': 'string'
                },
            ],
            'TrainingChannels': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'IsRequired': True|False,
                    'SupportedContentTypes': [
                        'string',
                    ],
                    'SupportedCompressionTypes': [
                        'None'|'Gzip',
                    ],
                    'SupportedInputModes': [
                        'Pipe'|'File',
                    ]
                },
            ],
            'SupportedTuningJobObjectiveMetrics': [
                {
                    'Type': 'Maximize'|'Minimize',
                    'MetricName': 'string'
                },
            ]
        },
        InferenceSpecification={
            'Containers': [
                {
                    'ContainerHostname': 'string',
                    'Image': 'string',
                    'ImageDigest': 'string',
                    'ModelDataUrl': 'string',
                    'ProductId': 'string'
                },
            ],
            'SupportedTransformInstanceTypes': [
                'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
            ],
            'SupportedRealtimeInferenceInstanceTypes': [
                'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
            ],
            'SupportedContentTypes': [
                'string',
            ],
            'SupportedResponseMIMETypes': [
                'string',
            ]
        },
        ValidationSpecification={
            'ValidationRole': 'string',
            'ValidationProfiles': [
                {
                    'ProfileName': 'string',
                    'TrainingJobDefinition': {
                        'TrainingInputMode': 'Pipe'|'File',
                        'HyperParameters': {
                            'string': 'string'
                        },
                        'InputDataConfig': [
                            {
                                'ChannelName': 'string',
                                'DataSource': {
                                    'S3DataSource': {
                                        'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                        'S3Uri': 'string',
                                        'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key',
                                        'AttributeNames': [
                                            'string',
                                        ]
                                    }
                                },
                                'ContentType': 'string',
                                'CompressionType': 'None'|'Gzip',
                                'RecordWrapperType': 'None'|'RecordIO',
                                'InputMode': 'Pipe'|'File',
                                'ShuffleConfig': {
                                    'Seed': 123
                                }
                            },
                        ],
                        'OutputDataConfig': {
                            'KmsKeyId': 'string',
                            'S3OutputPath': 'string'
                        },
                        'ResourceConfig': {
                            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                            'InstanceCount': 123,
                            'VolumeSizeInGB': 123,
                            'VolumeKmsKeyId': 'string'
                        },
                        'StoppingCondition': {
                            'MaxRuntimeInSeconds': 123
                        }
                    },
                    'TransformJobDefinition': {
                        'MaxConcurrentTransforms': 123,
                        'MaxPayloadInMB': 123,
                        'BatchStrategy': 'MultiRecord'|'SingleRecord',
                        'Environment': {
                            'string': 'string'
                        },
                        'TransformInput': {
                            'DataSource': {
                                'S3DataSource': {
                                    'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                    'S3Uri': 'string'
                                }
                            },
                            'ContentType': 'string',
                            'CompressionType': 'None'|'Gzip',
                            'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
                        },
                        'TransformOutput': {
                            'S3OutputPath': 'string',
                            'Accept': 'string',
                            'AssembleWith': 'None'|'Line',
                            'KmsKeyId': 'string'
                        },
                        'TransformResources': {
                            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                            'InstanceCount': 123,
                            'VolumeKmsKeyId': 'string'
                        }
                    }
                },
            ]
        },
        CertifyForMarketplace=True|False
    )
    
    
    :type AlgorithmName: string
    :param AlgorithmName: [REQUIRED]
            The name of the algorithm.
            

    :type AlgorithmDescription: string
    :param AlgorithmDescription: A description of the algorithm.

    :type TrainingSpecification: dict
    :param TrainingSpecification: [REQUIRED]
            Specifies details about training jobs run by this algorithm, including the following:
            The Amazon ECR path of the container and the version digest of the algorithm.
            The hyperparameters that the algorithm supports.
            The instance types that the algorithm supports for training.
            Whether the algorithm supports distributed training.
            The metrics that the algorithm emits to Amazon CloudWatch.
            Which metrics that the algorithm emits can be used as the objective metric for hyperparameter tuning jobs.
            The input channels that the algorithm supports for training data. For example, an algorithm might support train , validation , and test channels.
            TrainingImage (string) -- [REQUIRED]The Amazon Amazon ECR registry path of the Docker image that contains the training algorithm.
            TrainingImageDigest (string) --An MD5 hash of the training algorithm that identifies the Docker image used for training.
            SupportedHyperParameters (list) --A list of the HyperParameterSpecification objects, that define the supported hyperparameters. This is required if the algorithm supports automatic model tuning.>
            (dict) --Defines a hyperparameter to be used by an algorithm.
            Name (string) -- [REQUIRED]The name of this hyperparameter. The name must be unique.
            Description (string) --A brief description of the hyperparameter.
            Type (string) -- [REQUIRED]The type of this hyperparameter. The valid types are Integer , Continuous , Categorical , and FreeText .
            Range (dict) --The allowed range for this hyperparameter.
            IntegerParameterRangeSpecification (dict) --A IntegerParameterRangeSpecification object that defines the possible values for an integer hyperparameter.
            MinValue (string) -- [REQUIRED]The minimum integer value allowed.
            MaxValue (string) -- [REQUIRED]The maximum integer value allowed.
            ContinuousParameterRangeSpecification (dict) --A ContinuousParameterRangeSpecification object that defines the possible values for a continuous hyperparameter.
            MinValue (string) -- [REQUIRED]The minimum floating-point value allowed.
            MaxValue (string) -- [REQUIRED]The maximum floating-point value allowed.
            CategoricalParameterRangeSpecification (dict) --A CategoricalParameterRangeSpecification object that defines the possible values for a categorical hyperparameter.
            Values (list) -- [REQUIRED]The allowed categories for the hyperparameter.
            (string) --
            
            IsTunable (boolean) --Indicates whether this hyperparameter is tunable in a hyperparameter tuning job.
            IsRequired (boolean) --Indicates whether this hyperparameter is required.
            DefaultValue (string) --The default value for this hyperparameter. If a default value is specified, a hyperparameter cannot be required.
            
            SupportedTrainingInstanceTypes (list) -- [REQUIRED]A list of the instance types that this algorithm can use for training.
            (string) --
            SupportsDistributedTraining (boolean) --Indicates whether the algorithm supports distributed training. If set to false, buyers can t request more than one instance during training.
            MetricDefinitions (list) --A list of MetricDefinition objects, which are used for parsing metrics generated by the algorithm.
            (dict) --Specifies a metric that the training algorithm writes to stderr or stdout . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
            Name (string) -- [REQUIRED]The name of the metric.
            Regex (string) -- [REQUIRED]A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see Defining Objective Metrics .
            
            TrainingChannels (list) -- [REQUIRED]A list of ChannelSpecification objects, which specify the input sources to be used by the algorithm.
            (dict) --Defines a named input source, called a channel, to be used by an algorithm.
            Name (string) -- [REQUIRED]The name of the channel.
            Description (string) --A brief description of the channel.
            IsRequired (boolean) --Indicates whether the channel is required by the algorithm.
            SupportedContentTypes (list) -- [REQUIRED]The supported MIME types for the data.
            (string) --
            SupportedCompressionTypes (list) --The allowed compression types, if data compression is used.
            (string) --
            SupportedInputModes (list) -- [REQUIRED]The allowed input mode, either FILE or PIPE.
            In FILE mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode.
            In PIPE mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.
            (string) --
            
            SupportedTuningJobObjectiveMetrics (list) --A list of the metrics that the algorithm emits that can be used as the objective metric in a hyperparameter tuning job.
            (dict) --Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the Type parameter.
            Type (string) -- [REQUIRED]Whether to minimize or maximize the objective metric.
            MetricName (string) -- [REQUIRED]The name of the metric to use for the objective metric.
            
            

    :type InferenceSpecification: dict
    :param InferenceSpecification: Specifies details about inference jobs that the algorithm runs, including the following:
            The Amazon ECR paths of containers that contain the inference code and model artifacts.
            The instance types that the algorithm supports for transform jobs and real-time endpoints used for inference.
            The input and output content formats that the algorithm supports for inference.
            Containers (list) -- [REQUIRED]The Amazon ECR registry path of the Docker image that contains the inference code.
            (dict) --Describes the Docker container for the model package.
            ContainerHostname (string) --The DNS host name for the Docker container.
            Image (string) -- [REQUIRED]The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored.
            If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both registry/repository[:tag] and registry/repository[@digest] image path formats. For more information, see Using Your Own Algorithms with Amazon SageMaker .
            ImageDigest (string) --An MD5 hash of the training algorithm that identifies the Docker image used for training.
            ModelDataUrl (string) --The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
            ProductId (string) --The AWS Marketplace product ID of the model package.
            
            SupportedTransformInstanceTypes (list) -- [REQUIRED]A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.
            (string) --
            SupportedRealtimeInferenceInstanceTypes (list) -- [REQUIRED]A list of the instance types that are used to generate inferences in real-time.
            (string) --
            SupportedContentTypes (list) -- [REQUIRED]The supported MIME types for the input data.
            (string) --
            SupportedResponseMIMETypes (list) -- [REQUIRED]The supported MIME types for the output data.
            (string) --
            

    :type ValidationSpecification: dict
    :param ValidationSpecification: Specifies configurations for one or more training jobs and that Amazon SageMaker runs to test the algorithm's training code and, optionally, one or more batch transform jobs that Amazon SageMaker runs to test the algorithm's inference code.
            ValidationRole (string) -- [REQUIRED]The IAM roles that Amazon SageMaker uses to run the training jobs.
            ValidationProfiles (list) -- [REQUIRED]An array of AlgorithmValidationProfile objects, each of which specifies a training job and batch transform job that Amazon SageMaker runs to validate your algorithm.
            (dict) --Defines a training job and a batch transform job that Amazon SageMaker runs to validate your algorithm.
            The data provided in the validation profile is made available to your buyers on AWS Marketplace.
            ProfileName (string) -- [REQUIRED]The name of the profile for the algorithm. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
            TrainingJobDefinition (dict) -- [REQUIRED]The TrainingJobDefinition object that describes the training job that Amazon SageMaker runs to validate your algorithm.
            TrainingInputMode (string) -- [REQUIRED]The input mode used by the algorithm for the training job. For the input modes that Amazon SageMaker algorithms support, see Algorithms .
            If an algorithm supports the File input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the Pipe input mode, Amazon SageMaker streams data directly from S3 to the container.
            HyperParameters (dict) --The hyperparameters used for the training job.
            (string) --
            (string) --
            
            InputDataConfig (list) -- [REQUIRED]An array of Channel objects, each of which specifies an input source.
            (dict) --A channel is a named input source that training algorithms can consume.
            ChannelName (string) -- [REQUIRED]The name of the channel.
            DataSource (dict) -- [REQUIRED]The location of the channel data.
            S3DataSource (dict) -- [REQUIRED]The S3 location of the data source that is associated with a channel.
            S3DataType (string) -- [REQUIRED]If you choose S3Prefix , S3Uri identifies a key name prefix. Amazon SageMaker uses all objects that match the specified key name prefix for model training.
            If you choose ManifestFile , S3Uri identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training.
            If you choose AugmentedManifestFile , S3Uri identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. AugmentedManifestFile can only be used if the Channel's input mode is Pipe .
            S3Uri (string) -- [REQUIRED]Depending on the value specified for the S3DataType , identifies either a key name prefix or a manifest. For example:
            A key name prefix might look like this: s3://bucketname/exampleprefix .
            A manifest might look like this: s3://bucketname/example.manifest  The manifest is an S3 object which is a JSON file with the following format:  [ {'prefix': 's3://customer_bucket/some/prefix/'}, 'relative/path/to/custdata-1', 'relative/path/custdata-2', ... ]  The preceding JSON matches the following s3Uris :  s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-2 ...  The complete set of s3uris in this manifest is the input data for the channel for this datasource. The object that each s3uris points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
            S3DataDistributionType (string) --If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify FullyReplicated .
            If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ShardedByS3Key . If there are n ML compute instances launched for a training job, each instance gets approximately 1/n of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.
            Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.
            In distributed training, where you use multiple ML compute EC2 instances, you might choose ShardedByS3Key . If the algorithm requires copying training data to the ML storage volume (when TrainingInputMode is set to File ), this copies 1/n of the number of objects.
            AttributeNames (list) --A list of one or more attribute names to use that are found in a specified augmented manifest file.
            (string) --
            
            ContentType (string) --The MIME type of the data.
            CompressionType (string) --If training data is compressed, the compression type. The default value is None . CompressionType is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
            RecordWrapperType (string) --Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see Create a Dataset Using RecordIO .
            In File mode, leave this field unset or set it to None.
            InputMode (string) --(Optional) The input mode to use for the data channel in a training job. If you don't set a value for InputMode , Amazon SageMaker uses the value set for TrainingInputMode . Use this parameter to override the TrainingInputMode setting in a AlgorithmSpecification request when you have a channel that needs a different input mode from the training job's general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use File input mode. To stream data directly from Amazon S3 to the container, choose Pipe input mode.
            To use a model for incremental training, choose File input model.
            ShuffleConfig (dict) --A configuration for a shuffle option for input data in a channel. If you use S3Prefix for S3DataType , this shuffles the results of the S3 key prefix matches. If you use ManifestFile , the order of the S3 object references in the ManifestFile is shuffled. If you use AugmentedManifestFile , the order of the JSON lines in the AugmentedManifestFile is shuffled. The shuffling order is determined using the Seed value.
            For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with S3DataDistributionType of ShardedByS3Key , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.
            Seed (integer) -- [REQUIRED]Determines the shuffling order in ShuffleConfig value.
            
            OutputDataConfig (dict) -- [REQUIRED]the path to the S3 bucket where you want to store model artifacts. Amazon SageMaker creates subfolders for the artifacts.
            KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The KmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            // KMS Key Alias 'alias/ExampleAlias'
            // Amazon Resource Name (ARN) of a KMS Key Alias 'arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias'
            If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see KMS-Managed Encryption Keys in the Amazon Simple Storage Service Developer Guide.
            The KMS key policy must grant permission to the IAM role that you specify in your CreateTramsformJob request. For more information, see Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide .
            S3OutputPath (string) -- [REQUIRED]Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, s3://bucket-name/key-name-prefix .
            ResourceConfig (dict) -- [REQUIRED]The resources, including the ML compute instances and ML storage volumes, to use for model training.
            InstanceType (string) -- [REQUIRED]The ML compute instance type.
            InstanceCount (integer) -- [REQUIRED]The number of ML compute instances to use. For distributed training, provide a value greater than 1.
            VolumeSizeInGB (integer) -- [REQUIRED]The size of the ML storage volume that you want to provision.
            ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose File as the TrainingInputMode in the algorithm specification.
            You must specify sufficient ML storage for your scenario.
            Note
            Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type.
            VolumeKmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job. The VolumeKmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            
            StoppingCondition (dict) -- [REQUIRED]Sets a duration for training. Use this parameter to cap model training costs.
            To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
            MaxRuntimeInSeconds (integer) --The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
            
            TransformJobDefinition (dict) --The TransformJobDefinition object that describes the transform job that Amazon SageMaker runs to validate your algorithm.
            MaxConcurrentTransforms (integer) --The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.
            MaxPayloadInMB (integer) --The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).
            BatchStrategy (string) --A string that determines the number of records included in a single mini-batch.
            SingleRecord means only one record is used per mini-batch. MultiRecord means a mini-batch is set to contain as many records that can fit within the MaxPayloadInMB limit.
            Environment (dict) --The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
            (string) --
            (string) --
            
            TransformInput (dict) -- [REQUIRED]A description of the input source and the way the transform job consumes it.
            DataSource (dict) -- [REQUIRED]Describes the location of the channel data, meaning the S3 location of the input data that the model can consume.
            S3DataSource (dict) -- [REQUIRED]The S3 location of the data source that is associated with a channel.
            S3DataType (string) -- [REQUIRED]If you choose S3Prefix , S3Uri identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform.
            If you choose ManifestFile , S3Uri identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform.
            S3Uri (string) -- [REQUIRED]Depending on the value specified for the S3DataType , identifies either a key name prefix or a manifest. For example:
            A key name prefix might look like this: s3://bucketname/exampleprefix .
            A manifest might look like this: s3://bucketname/example.manifest  The manifest is an S3 object which is a JSON file with the following format:  [ {'prefix': 's3://customer_bucket/some/prefix/'}, 'relative/path/to/custdata-1', 'relative/path/custdata-2', ... ]  The preceding JSON matches the following S3Uris :  s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-1 ...  The complete set of S3Uris in this manifest constitutes the input data for the channel for this datasource. The object that each S3Uris points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
            
            ContentType (string) --The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.
            CompressionType (string) --Compressing data helps save on storage space. If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is None .
            SplitType (string) --The method to use to split the transform job's data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for SplitType is None , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to Line to split records on a newline character boundary. SplitType also supports a number of record-oriented binary data formats.
            When splitting is enabled, the size of a mini-batch depends on the values of the BatchStrategy and MaxPayloadInMB parameters. When the value of BatchStrategy is MultiRecord , Amazon SageMaker sends the maximum number of records in each request, up to the MaxPayloadInMB limit. If the value of BatchStrategy is SingleRecord , Amazon SageMaker sends individual records in each request.
            Note
            Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of BatchStrategy is set to SingleRecord . Padding is not removed if the value of BatchStrategy is set to MultiRecord .
            For more information about the RecordIO data format, see Data Format in the MXNet documentation. For more information about the TFRecord fofmat, see Consuming TFRecord data in the TensorFlow documentation.
            TransformOutput (dict) -- [REQUIRED]Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
            S3OutputPath (string) -- [REQUIRED]The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, s3://bucket-name/key-name-prefix .
            For every S3 object used as input for the transform job, the transformed data is stored in a corresponding subfolder in the location under the output prefix. For example, the input data s3://bucket-name/input-name-prefix/dataset01/data.csv will have the transformed data stored at s3://bucket-name/key-name-prefix/dataset01/ , based on the original name, as a series of .part files (.part0001, part0002, etc).
            Accept (string) --The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
            AssembleWith (string) --Defines how to assemble the results of the transform job as a single S3 object. You should select a format that is most convenient to you. To concatenate the results in binary format, specify None . To add a newline character at the end of every transformed record, specify Line .
            KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The KmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            // KMS Key Alias 'alias/ExampleAlias'
            // Amazon Resource Name (ARN) of a KMS Key Alias 'arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias'
            If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see KMS-Managed Encryption Keys in the Amazon Simple Storage Service Developer Guide.
            The KMS key policy must grant permission to the IAM role that you specify in your CreateTramsformJob request. For more information, see Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide .
            TransformResources (dict) -- [REQUIRED]Identifies the ML compute instances for the transform job.
            InstanceType (string) -- [REQUIRED]The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ml.m5.large should suffice. There is no default value for InstanceType .
            InstanceCount (integer) -- [REQUIRED]The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is 1 .
            VolumeKmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The VolumeKmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            
            
            

    :type CertifyForMarketplace: boolean
    :param CertifyForMarketplace: Whether to certify the algorithm so that it can be listed in AWS Marektplace.

    :rtype: dict
    :return: {
        'AlgorithmArn': 'string'
    }
    
    
    """
    pass

def create_code_repository(CodeRepositoryName=None, GitConfig=None):
    """
    Create a git repository as a resource in your Amazon SageMaker account. You can associate the repository with notebook instances so that you can use git source control for the notebooks you create. The git repository is a resource in your Amazon SageMaker account, so it can be associated with more than one notebook instance, and it persists independently from the lifecycle of any notebook instances it is associated with.
    The repository can be hosted either in AWS CodeCommit or in any other git repository.
    See also: AWS API Documentation
    
    
    :example: response = client.create_code_repository(
        CodeRepositoryName='string',
        GitConfig={
            'RepositoryUrl': 'string',
            'Branch': 'string',
            'SecretArn': 'string'
        }
    )
    
    
    :type CodeRepositoryName: string
    :param CodeRepositoryName: [REQUIRED]
            The name of the git repository. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
            

    :type GitConfig: dict
    :param GitConfig: [REQUIRED]
            Specifies details about the repository, including the URL where the repository is located, the default branch, and credentials to use to access the repository.
            RepositoryUrl (string) -- [REQUIRED]The URL where the git repository is located.
            Branch (string) --The default beach for the git repository.
            SecretArn (string) --The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of AWSCURRENT and must be in the following format:
            {'username': *UserName* , 'password': *Password* }
            

    :rtype: dict
    :return: {
        'CodeRepositoryArn': 'string'
    }
    
    
    """
    pass

def create_compilation_job(CompilationJobName=None, RoleArn=None, InputConfig=None, OutputConfig=None, StoppingCondition=None):
    """
    Starts a model compilation job. After the model has been compiled, Amazon SageMaker saves the resulting model artifacts to an Amazon Simple Storage Service (Amazon S3) bucket that you specify.
    If you choose to host your model using Amazon SageMaker hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts with AWS IoT Greengrass. In that case, deploy them as an ML resource.
    In the request body, you provide the following:
    You can also provide a Tag to track the model compilation job's resource use and costs. The response body contains the CompilationJobArn for the compiled job.
    To stop a model compilation job, use  StopCompilationJob . To get information about a particular model compilation job, use  DescribeCompilationJob . To get information about multiple model compilation jobs, use  ListCompilationJobs .
    See also: AWS API Documentation
    
    
    :example: response = client.create_compilation_job(
        CompilationJobName='string',
        RoleArn='string',
        InputConfig={
            'S3Uri': 'string',
            'DataInputConfig': 'string',
            'Framework': 'TENSORFLOW'|'MXNET'|'ONNX'|'PYTORCH'|'XGBOOST'
        },
        OutputConfig={
            'S3OutputLocation': 'string',
            'TargetDevice': 'ml_m4'|'ml_m5'|'ml_c4'|'ml_c5'|'ml_p2'|'ml_p3'|'jetson_tx1'|'jetson_tx2'|'rasp3b'|'deeplens'
        },
        StoppingCondition={
            'MaxRuntimeInSeconds': 123
        }
    )
    
    
    :type CompilationJobName: string
    :param CompilationJobName: [REQUIRED]
            A name for the model compilation job. The name must be unique within the AWS Region and within your AWS account.
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of an IIAMAM role that enables Amazon SageMaker to perform tasks on your behalf.
            During model compilation, Amazon SageMaker needs your permission to:
            Read input data from an S3 bucket
            Write model artifacts to an S3 bucket
            Write logs to Amazon CloudWatch Logs
            Publish metrics to Amazon CloudWatch
            You grant permissions for all of these tasks to an IAM role. To pass this role to Amazon SageMaker, the caller of this API must have the iam:PassRole permission. For more information, see Amazon SageMaker Roles.
            

    :type InputConfig: dict
    :param InputConfig: [REQUIRED]
            Provides information about the location of input model artifacts, the name and shape of the expected data inputs, and the framework in which the model was trained.
            S3Uri (string) -- [REQUIRED]The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
            DataInputConfig (string) -- [REQUIRED]Specifies the name and shape of the expected data inputs for your trained model with a JSON dictionary form. The data inputs are InputConfig$Framework specific.
            TensorFlow : You must specify the name and shape (NHWC format) of the expected data inputs using a dictionary format for your trained model. The dictionary formats required for the console and CLI are different.
            Examples for one input:
            If using the console, {'input':[1,1024,1024,3]}
            If using the CLI, {\'input\':[1,1024,1024,3]}
            Examples for two inputs:
            If using the console, {'data1': [1,28,28,1], 'data2':[1,28,28,1]}
            If using the CLI, {\'data1\': [1,28,28,1], \'data2\':[1,28,28,1]}
            
            MXNET/ONNX : You must specify the name and shape (NCHW format) of the expected data inputs in order using a dictionary format for your trained model. The dictionary formats required for the console and CLI are different.
            Examples for one input:
            If using the console, {'data':[1,3,1024,1024]}
            If using the CLI, {\'data\':[1,3,1024,1024]}
            Examples for two inputs:
            If using the console, {'var1': [1,1,28,28], 'var2':[1,1,28,28]}
            If using the CLI, {\'var1\': [1,1,28,28], \'var2\':[1,1,28,28]}
            
            PyTorch : You can either specify the name and shape (NCHW format) of expected data inputs in order using a dictionary format for your trained model or you can specify the shape only using a list format. The dictionary formats required for the console and CLI are different. The list formats for the console and CLI are the same.
            Examples for one input in dictionary format:
            If using the console, {'input0':[1,3,224,224]}
            If using the CLI, {\'input0\':[1,3,224,224]}
            Example for one input in list format: [[1,3,224,224]]
            Examples for two inputs in dictionary format:
            If using the console, {'input0':[1,3,224,224], 'input1':[1,3,224,224]}
            If using the CLI, {\'input0\':[1,3,224,224], \'input1\':[1,3,224,224]}
            Example for two inputs in list format: [[1,3,224,224], [1,3,224,224]]
            XGBOOST : input data name and shape are not needed.
            Framework (string) -- [REQUIRED]Identifies the framework in which the model was trained. For example: TENSORFLOW.
            

    :type OutputConfig: dict
    :param OutputConfig: [REQUIRED]
            Provides information about the output location for the compiled model and the target device the model runs on.
            S3OutputLocation (string) -- [REQUIRED]Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, s3://bucket-name/key-name-prefix.
            TargetDevice (string) -- [REQUIRED]Identifies the device that you want to run your model on after it has been compiled. For example: ml_c5.
            

    :type StoppingCondition: dict
    :param StoppingCondition: [REQUIRED]
            The duration allowed for model compilation.
            MaxRuntimeInSeconds (integer) --The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
            

    :rtype: dict
    :return: {
        'CompilationJobArn': 'string'
    }
    
    
    :returns: 
    CompilationJobName (string) -- [REQUIRED]
    A name for the model compilation job. The name must be unique within the AWS Region and within your AWS account.
    
    RoleArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of an IIAMAM role that enables Amazon SageMaker to perform tasks on your behalf.
    During model compilation, Amazon SageMaker needs your permission to:
    
    Read input data from an S3 bucket
    Write model artifacts to an S3 bucket
    Write logs to Amazon CloudWatch Logs
    Publish metrics to Amazon CloudWatch
    
    You grant permissions for all of these tasks to an IAM role. To pass this role to Amazon SageMaker, the caller of this API must have the iam:PassRole permission. For more information, see Amazon SageMaker Roles.
    
    InputConfig (dict) -- [REQUIRED]
    Provides information about the location of input model artifacts, the name and shape of the expected data inputs, and the framework in which the model was trained.
    
    S3Uri (string) -- [REQUIRED]The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
    
    DataInputConfig (string) -- [REQUIRED]Specifies the name and shape of the expected data inputs for your trained model with a JSON dictionary form. The data inputs are  InputConfig$Framework specific.
    
    TensorFlow : You must specify the name and shape (NHWC format) of the expected data inputs using a dictionary format for your trained model. The dictionary formats required for the console and CLI are different.
    Examples for one input:
    If using the console, {"input":[1,1024,1024,3]}
    If using the CLI, {\"input\":[1,1024,1024,3]}
    
    
    Examples for two inputs:
    If using the console, {"data1": [1,28,28,1], "data2":[1,28,28,1]}
    If using the CLI, {\"data1\": [1,28,28,1], \"data2\":[1,28,28,1]}
    
    
    
    
    MXNET/ONNX : You must specify the name and shape (NCHW format) of the expected data inputs in order using a dictionary format for your trained model. The dictionary formats required for the console and CLI are different.
    Examples for one input:
    If using the console, {"data":[1,3,1024,1024]}
    If using the CLI, {\"data\":[1,3,1024,1024]}
    
    
    Examples for two inputs:
    If using the console, {"var1": [1,1,28,28], "var2":[1,1,28,28]}
    If using the CLI, {\"var1\": [1,1,28,28], \"var2\":[1,1,28,28]}
    
    
    
    
    PyTorch : You can either specify the name and shape (NCHW format) of expected data inputs in order using a dictionary format for your trained model or you can specify the shape only using a list format. The dictionary formats required for the console and CLI are different. The list formats for the console and CLI are the same.
    Examples for one input in dictionary format:
    If using the console, {"input0":[1,3,224,224]}
    If using the CLI, {\"input0\":[1,3,224,224]}
    
    
    Example for one input in list format: [[1,3,224,224]]
    Examples for two inputs in dictionary format:
    If using the console, {"input0":[1,3,224,224], "input1":[1,3,224,224]}
    If using the CLI, {\"input0\":[1,3,224,224], \"input1\":[1,3,224,224]}
    
    
    Example for two inputs in list format: [[1,3,224,224], [1,3,224,224]]
    
    
    XGBOOST : input data name and shape are not needed.
    
    
    Framework (string) -- [REQUIRED]Identifies the framework in which the model was trained. For example: TENSORFLOW.
    
    
    
    OutputConfig (dict) -- [REQUIRED]
    Provides information about the output location for the compiled model and the target device the model runs on.
    
    S3OutputLocation (string) -- [REQUIRED]Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, s3://bucket-name/key-name-prefix.
    
    TargetDevice (string) -- [REQUIRED]Identifies the device that you want to run your model on after it has been compiled. For example: ml_c5.
    
    
    
    StoppingCondition (dict) -- [REQUIRED]
    The duration allowed for model compilation.
    
    MaxRuntimeInSeconds (integer) --The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
    
    
    
    
    """
    pass

def create_endpoint(EndpointName=None, EndpointConfigName=None, Tags=None):
    """
    Creates an endpoint using the endpoint configuration specified in the request. Amazon SageMaker uses the endpoint to provision resources and deploy models. You create the endpoint configuration with the CreateEndpointConfig API.
    The endpoint name must be unique within an AWS Region in your AWS account.
    When it receives the request, Amazon SageMaker creates the endpoint, launches the resources (ML compute instances), and deploys the model(s) on them.
    When Amazon SageMaker receives the request, it sets the endpoint status to Creating . After it creates the endpoint, it sets the status to InService . Amazon SageMaker can then process incoming requests for inferences. To check the status of an endpoint, use the DescribeEndpoint API.
    For an example, see Exercise 1: Using the K-Means Algorithm Provided by Amazon SageMaker .
    If any of the models hosted at this endpoint get model data from an Amazon S3 location, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provided. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see Activating and Deactivating AWS STS i an AWS Region in the AWS Identity and Access Management User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_endpoint(
        EndpointName='string',
        EndpointConfigName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of the endpoint. The name must be unique within an AWS Region in your AWS account.
            

    :type EndpointConfigName: string
    :param EndpointConfigName: [REQUIRED]
            The name of an endpoint configuration. For more information, see CreateEndpointConfig .
            

    :type Tags: list
    :param Tags: An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :rtype: dict
    :return: {
        'EndpointArn': 'string'
    }
    
    
    """
    pass

def create_endpoint_config(EndpointConfigName=None, ProductionVariants=None, Tags=None, KmsKeyId=None):
    """
    Creates an endpoint configuration that Amazon SageMaker hosting services uses to deploy models. In the configuration, you identify one or more models, created using the CreateModel API, to deploy and the resources that you want Amazon SageMaker to provision. Then you call the CreateEndpoint API.
    In the request, you define one or more ProductionVariant s, each of which identifies a model. Each ProductionVariant parameter also describes the resources that you want Amazon SageMaker to provision. This includes the number and type of ML compute instances to deploy.
    If you are hosting multiple models, you also assign a VariantWeight to specify how much traffic you want to allocate to each model. For example, suppose that you want to host two models, A and B, and you assign traffic weight 2 for model A and 1 for model B. Amazon SageMaker distributes two-thirds of the traffic to Model A, and one-third to model B.
    See also: AWS API Documentation
    
    
    :example: response = client.create_endpoint_config(
        EndpointConfigName='string',
        ProductionVariants=[
            {
                'VariantName': 'string',
                'ModelName': 'string',
                'InitialInstanceCount': 123,
                'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                'InitialVariantWeight': ...,
                'AcceleratorType': 'ml.eia1.medium'|'ml.eia1.large'|'ml.eia1.xlarge'
            },
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        KmsKeyId='string'
    )
    
    
    :type EndpointConfigName: string
    :param EndpointConfigName: [REQUIRED]
            The name of the endpoint configuration. You specify this name in a CreateEndpoint request.
            

    :type ProductionVariants: list
    :param ProductionVariants: [REQUIRED]
            An array of ProductionVariant objects, one for each model that you want to host at this endpoint.
            (dict) --Identifies a model that you want to host and the resources to deploy for hosting it. If you are deploying multiple models, tell Amazon SageMaker how to distribute traffic among the models by specifying variant weights.
            VariantName (string) -- [REQUIRED]The name of the production variant.
            ModelName (string) -- [REQUIRED]The name of the model that you want to host. This is the name that you specified when creating the model.
            InitialInstanceCount (integer) -- [REQUIRED]Number of instances to launch initially.
            InstanceType (string) -- [REQUIRED]The ML compute instance type.
            InitialVariantWeight (float) --Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the VariantWeight to the sum of all VariantWeight values across all ProductionVariants. If unspecified, it defaults to 1.0.
            AcceleratorType (string) --The size of the Elastic Inference (EI) instance to use for the production variant. EI instances provide on-demand GPU computing for inference. For more information, see Using Elastic Inference in Amazon SageMaker . For more information, see Using Elastic Inference in Amazon SageMaker .
            
            

    :type Tags: list
    :param Tags: An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :type KmsKeyId: string
    :param KmsKeyId: The Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.

    :rtype: dict
    :return: {
        'EndpointConfigArn': 'string'
    }
    
    
    """
    pass

def create_hyper_parameter_tuning_job(HyperParameterTuningJobName=None, HyperParameterTuningJobConfig=None, TrainingJobDefinition=None, WarmStartConfig=None, Tags=None):
    """
    Starts a hyperparameter tuning job. A hyperparameter tuning job finds the best version of a model by running many training jobs on your dataset using the algorithm you choose and values for hyperparameters within ranges that you specify. It then chooses the hyperparameter values that result in a model that performs the best, as measured by an objective metric that you choose.
    See also: AWS API Documentation
    
    
    :example: response = client.create_hyper_parameter_tuning_job(
        HyperParameterTuningJobName='string',
        HyperParameterTuningJobConfig={
            'Strategy': 'Bayesian',
            'HyperParameterTuningJobObjective': {
                'Type': 'Maximize'|'Minimize',
                'MetricName': 'string'
            },
            'ResourceLimits': {
                'MaxNumberOfTrainingJobs': 123,
                'MaxParallelTrainingJobs': 123
            },
            'ParameterRanges': {
                'IntegerParameterRanges': [
                    {
                        'Name': 'string',
                        'MinValue': 'string',
                        'MaxValue': 'string'
                    },
                ],
                'ContinuousParameterRanges': [
                    {
                        'Name': 'string',
                        'MinValue': 'string',
                        'MaxValue': 'string'
                    },
                ],
                'CategoricalParameterRanges': [
                    {
                        'Name': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ]
            },
            'TrainingJobEarlyStoppingType': 'Off'|'Auto'
        },
        TrainingJobDefinition={
            'StaticHyperParameters': {
                'string': 'string'
            },
            'AlgorithmSpecification': {
                'TrainingImage': 'string',
                'TrainingInputMode': 'Pipe'|'File',
                'AlgorithmName': 'string',
                'MetricDefinitions': [
                    {
                        'Name': 'string',
                        'Regex': 'string'
                    },
                ]
            },
            'RoleArn': 'string',
            'InputDataConfig': [
                {
                    'ChannelName': 'string',
                    'DataSource': {
                        'S3DataSource': {
                            'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                            'S3Uri': 'string',
                            'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key',
                            'AttributeNames': [
                                'string',
                            ]
                        }
                    },
                    'ContentType': 'string',
                    'CompressionType': 'None'|'Gzip',
                    'RecordWrapperType': 'None'|'RecordIO',
                    'InputMode': 'Pipe'|'File',
                    'ShuffleConfig': {
                        'Seed': 123
                    }
                },
            ],
            'VpcConfig': {
                'SecurityGroupIds': [
                    'string',
                ],
                'Subnets': [
                    'string',
                ]
            },
            'OutputDataConfig': {
                'KmsKeyId': 'string',
                'S3OutputPath': 'string'
            },
            'ResourceConfig': {
                'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                'InstanceCount': 123,
                'VolumeSizeInGB': 123,
                'VolumeKmsKeyId': 'string'
            },
            'StoppingCondition': {
                'MaxRuntimeInSeconds': 123
            },
            'EnableNetworkIsolation': True|False
        },
        WarmStartConfig={
            'ParentHyperParameterTuningJobs': [
                {
                    'HyperParameterTuningJobName': 'string'
                },
            ],
            'WarmStartType': 'IdenticalDataAndAlgorithm'|'TransferLearning'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type HyperParameterTuningJobName: string
    :param HyperParameterTuningJobName: [REQUIRED]
            The name of the tuning job. This name is the prefix for the names of all training jobs that this tuning job launches. The name must be unique within the same AWS account and AWS Region. The name must have { } to { } characters. Valid characters are a-z, A-Z, 0-9, and : + = @ _ % - (hyphen). The name is not case sensitive.
            

    :type HyperParameterTuningJobConfig: dict
    :param HyperParameterTuningJobConfig: [REQUIRED]
            The HyperParameterTuningJobConfig object that describes the tuning job, including the search strategy, the objective metric used to evaluate training jobs, ranges of parameters to search, and resource limits for the tuning job. For more information, see automatic-model-tuning
            Strategy (string) -- [REQUIRED]Specifies the search strategy for hyperparameters. Currently, the only valid value is Bayesian .
            HyperParameterTuningJobObjective (dict) -- [REQUIRED]The HyperParameterTuningJobObjective object that specifies the objective metric for this tuning job.
            Type (string) -- [REQUIRED]Whether to minimize or maximize the objective metric.
            MetricName (string) -- [REQUIRED]The name of the metric to use for the objective metric.
            ResourceLimits (dict) -- [REQUIRED]The ResourceLimits object that specifies the maximum number of training jobs and parallel training jobs for this tuning job.
            MaxNumberOfTrainingJobs (integer) -- [REQUIRED]The maximum number of training jobs that a hyperparameter tuning job can launch.
            MaxParallelTrainingJobs (integer) -- [REQUIRED]The maximum number of concurrent training jobs that a hyperparameter tuning job can launch.
            ParameterRanges (dict) -- [REQUIRED]The ParameterRanges object that specifies the ranges of hyperparameters that this tuning job searches.
            IntegerParameterRanges (list) --The array of IntegerParameterRange objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.
            (dict) --For a hyperparameter of the integer type, specifies the range that a hyperparameter tuning job searches.
            Name (string) -- [REQUIRED]The name of the hyperparameter to search.
            MinValue (string) -- [REQUIRED]The minimum value of the hyperparameter to search.
            MaxValue (string) -- [REQUIRED]The maximum value of the hyperparameter to search.
            
            ContinuousParameterRanges (list) --The array of ContinuousParameterRange objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.
            (dict) --A list of continuous hyperparameters to tune.
            Name (string) -- [REQUIRED]The name of the continuous hyperparameter to tune.
            MinValue (string) -- [REQUIRED]The minimum value for the hyperparameter. The tuning job uses floating-point values between this value and MaxValue for tuning.
            MaxValue (string) -- [REQUIRED]The maximum value for the hyperparameter. The tuning job uses floating-point values between MinValue value and this value for tuning.
            
            CategoricalParameterRanges (list) --The array of CategoricalParameterRange objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.
            (dict) --A list of categorical hyperparameters to tune.
            Name (string) -- [REQUIRED]The name of the categorical hyperparameter to tune.
            Values (list) -- [REQUIRED]A list of the categories for the hyperparameter.
            (string) --
            
            
            TrainingJobEarlyStoppingType (string) --Specifies whether to use early stopping for training jobs launched by the hyperparameter tuning job. This can be one of the following values (the default value is OFF ):
            OFF
            Training jobs launched by the hyperparameter tuning job do not use early stopping.
            AUTO
            Amazon SageMaker stops training jobs launched by the hyperparameter tuning job when they are unlikely to perform better than previously completed training jobs. For more information, see Stop Training Jobs Early .
            

    :type TrainingJobDefinition: dict
    :param TrainingJobDefinition: [REQUIRED]
            The HyperParameterTrainingJobDefinition object that describes the training jobs that this tuning job launches, including static hyperparameters, input data configuration, output data configuration, resource configuration, and stopping condition.
            StaticHyperParameters (dict) --Specifies the values of hyperparameters that do not change for the tuning job.
            (string) --
            (string) --
            
            AlgorithmSpecification (dict) -- [REQUIRED]The HyperParameterAlgorithmSpecification object that specifies the resource algorithm to use for the training jobs that the tuning job launches.
            TrainingImage (string) --The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see Algorithms Provided by Amazon SageMaker: Common Parameters .
            TrainingInputMode (string) -- [REQUIRED]The input mode that the algorithm supports: File or Pipe. In File input mode, Amazon SageMaker downloads the training data from Amazon S3 to the storage volume that is attached to the training instance and mounts the directory to the Docker volume for the training container. In Pipe input mode, Amazon SageMaker streams data directly from Amazon S3 to the container.
            If you specify File mode, make sure that you provision the storage volume that is attached to the training instance with enough capacity to accommodate the training data downloaded from Amazon S3, the model artifacts, and intermediate information.
            For more information about input modes, see Algorithms .
            AlgorithmName (string) --The name of the resource algorithm to use for the hyperparameter tuning job. If you specify a value for this parameter, do not specify a value for TrainingImage .
            MetricDefinitions (list) --An array of MetricDefinition objects that specify the metrics that the algorithm emits.
            (dict) --Specifies a metric that the training algorithm writes to stderr or stdout . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
            Name (string) -- [REQUIRED]The name of the metric.
            Regex (string) -- [REQUIRED]A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see Defining Objective Metrics .
            
            RoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the IAM role associated with the training jobs that the tuning job launches.
            InputDataConfig (list) --An array of Channel objects that specify the input for the training jobs that the tuning job launches.
            (dict) --A channel is a named input source that training algorithms can consume.
            ChannelName (string) -- [REQUIRED]The name of the channel.
            DataSource (dict) -- [REQUIRED]The location of the channel data.
            S3DataSource (dict) -- [REQUIRED]The S3 location of the data source that is associated with a channel.
            S3DataType (string) -- [REQUIRED]If you choose S3Prefix , S3Uri identifies a key name prefix. Amazon SageMaker uses all objects that match the specified key name prefix for model training.
            If you choose ManifestFile , S3Uri identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training.
            If you choose AugmentedManifestFile , S3Uri identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. AugmentedManifestFile can only be used if the Channel's input mode is Pipe .
            S3Uri (string) -- [REQUIRED]Depending on the value specified for the S3DataType , identifies either a key name prefix or a manifest. For example:
            A key name prefix might look like this: s3://bucketname/exampleprefix .
            A manifest might look like this: s3://bucketname/example.manifest  The manifest is an S3 object which is a JSON file with the following format:  [ {'prefix': 's3://customer_bucket/some/prefix/'}, 'relative/path/to/custdata-1', 'relative/path/custdata-2', ... ]  The preceding JSON matches the following s3Uris :  s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-2 ...  The complete set of s3uris in this manifest is the input data for the channel for this datasource. The object that each s3uris points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
            S3DataDistributionType (string) --If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify FullyReplicated .
            If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ShardedByS3Key . If there are n ML compute instances launched for a training job, each instance gets approximately 1/n of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.
            Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.
            In distributed training, where you use multiple ML compute EC2 instances, you might choose ShardedByS3Key . If the algorithm requires copying training data to the ML storage volume (when TrainingInputMode is set to File ), this copies 1/n of the number of objects.
            AttributeNames (list) --A list of one or more attribute names to use that are found in a specified augmented manifest file.
            (string) --
            
            ContentType (string) --The MIME type of the data.
            CompressionType (string) --If training data is compressed, the compression type. The default value is None . CompressionType is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
            RecordWrapperType (string) --Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see Create a Dataset Using RecordIO .
            In File mode, leave this field unset or set it to None.
            InputMode (string) --(Optional) The input mode to use for the data channel in a training job. If you don't set a value for InputMode , Amazon SageMaker uses the value set for TrainingInputMode . Use this parameter to override the TrainingInputMode setting in a AlgorithmSpecification request when you have a channel that needs a different input mode from the training job's general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use File input mode. To stream data directly from Amazon S3 to the container, choose Pipe input mode.
            To use a model for incremental training, choose File input model.
            ShuffleConfig (dict) --A configuration for a shuffle option for input data in a channel. If you use S3Prefix for S3DataType , this shuffles the results of the S3 key prefix matches. If you use ManifestFile , the order of the S3 object references in the ManifestFile is shuffled. If you use AugmentedManifestFile , the order of the JSON lines in the AugmentedManifestFile is shuffled. The shuffling order is determined using the Seed value.
            For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with S3DataDistributionType of ShardedByS3Key , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.
            Seed (integer) -- [REQUIRED]Determines the shuffling order in ShuffleConfig value.
            
            VpcConfig (dict) --The VpcConfig object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see Protect Training Jobs by Using an Amazon Virtual Private Cloud .
            SecurityGroupIds (list) -- [REQUIRED]The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the Subnets field.
            (string) --
            Subnets (list) -- [REQUIRED]The ID of the subnets in the VPC to which you want to connect your training job or model.
            (string) --
            
            OutputDataConfig (dict) -- [REQUIRED]Specifies the path to the Amazon S3 bucket where you store model artifacts from the training jobs that the tuning job launches.
            KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The KmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            // KMS Key Alias 'alias/ExampleAlias'
            // Amazon Resource Name (ARN) of a KMS Key Alias 'arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias'
            If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see KMS-Managed Encryption Keys in the Amazon Simple Storage Service Developer Guide.
            The KMS key policy must grant permission to the IAM role that you specify in your CreateTramsformJob request. For more information, see Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide .
            S3OutputPath (string) -- [REQUIRED]Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, s3://bucket-name/key-name-prefix .
            ResourceConfig (dict) -- [REQUIRED]The resources, including the compute instances and storage volumes, to use for the training jobs that the tuning job launches.
            Storage volumes store model artifacts and incremental states. Training algorithms might also use storage volumes for scratch space. If you want Amazon SageMaker to use the storage volume to store the training data, choose File as the TrainingInputMode in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.
            InstanceType (string) -- [REQUIRED]The ML compute instance type.
            InstanceCount (integer) -- [REQUIRED]The number of ML compute instances to use. For distributed training, provide a value greater than 1.
            VolumeSizeInGB (integer) -- [REQUIRED]The size of the ML storage volume that you want to provision.
            ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose File as the TrainingInputMode in the algorithm specification.
            You must specify sufficient ML storage for your scenario.
            Note
            Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type.
            VolumeKmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job. The VolumeKmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            
            StoppingCondition (dict) -- [REQUIRED]Sets a maximum duration for the training jobs that the tuning job launches. Use this parameter to limit model training costs.
            To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal. This delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
            When Amazon SageMaker terminates a job because the stopping condition has been met, training algorithms provided by Amazon SageMaker save the intermediate results of the job.
            MaxRuntimeInSeconds (integer) --The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
            EnableNetworkIsolation (boolean) --Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, Amazon SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.
            Note
            The Semantic Segmentation built-in algorithm does not support network isolation.
            

    :type WarmStartConfig: dict
    :param WarmStartConfig: Specifies configuration for starting the hyperparameter tuning job using one or more previous tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.
            All training jobs launched by the new hyperparameter tuning job are evaluated by using the objective metric. If you specify IDENTICAL_DATA_AND_ALGORITHM as the WarmStartType for the warm start configuration, the training job that performs the best in the new tuning job is compared to the best training jobs from the parent tuning jobs. From these, the training job that performs the best as measured by the objective metric is returned as the overall best training job.
            Note
            All training jobs launched by parent hyperparameter tuning jobs and the new hyperparameter tuning jobs count against the limit of training jobs for the tuning job.
            ParentHyperParameterTuningJobs (list) -- [REQUIRED]An array of hyperparameter tuning jobs that are used as the starting point for the new hyperparameter tuning job. For more information about warm starting a hyperparameter tuning job, see Using a Previous Hyperparameter Tuning Job as a Starting Point .
            Hyperparameter tuning jobs created before October 1, 2018 cannot be used as parent jobs for warm start tuning jobs.
            (dict) --A previously completed or stopped hyperparameter tuning job to be used as a starting point for a new hyperparameter tuning job.
            HyperParameterTuningJobName (string) --The name of the hyperparameter tuning job to be used as a starting point for a new hyperparameter tuning job.
            
            WarmStartType (string) -- [REQUIRED]Specifies one of the following:
            IDENTICAL_DATA_AND_ALGORITHM
            The new hyperparameter tuning job uses the same input data and training image as the parent tuning jobs. You can change the hyperparameter ranges to search and the maximum number of training jobs that the hyperparameter tuning job launches. You cannot use a new version of the training algorithm, unless the changes in the new version do not affect the algorithm itself. For example, changes that improve logging or adding support for a different data format are allowed. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.
            TRANSFER_LEARNING
            The new hyperparameter tuning job can include input data, hyperparameter ranges, maximum number of concurrent training jobs, and maximum number of training jobs that are different than those of its parent hyperparameter tuning jobs. The training image can also be a different version from the version used in the parent hyperparameter tuning job. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.
            

    :type Tags: list
    :param Tags: An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see AWS Tagging Strategies .
            Tags that you specify for the tuning job are also added to all training jobs that the tuning job launches.
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :rtype: dict
    :return: {
        'HyperParameterTuningJobArn': 'string'
    }
    
    
    """
    pass

def create_labeling_job(LabelingJobName=None, LabelAttributeName=None, InputConfig=None, OutputConfig=None, RoleArn=None, LabelCategoryConfigS3Uri=None, StoppingConditions=None, LabelingJobAlgorithmsConfig=None, HumanTaskConfig=None, Tags=None):
    """
    Creates a job that uses workers to label the data objects in your input dataset. You can use the labeled data to train machine learning models.
    You can select your workforce from one of three providers:
    You can also use automated data labeling to reduce the number of data objects that need to be labeled by a human. Automated data labeling uses active learning to determine if a data object can be labeled by machine or if it needs to be sent to a human worker. For more information, see Using Automated Data Labeling .
    The data objects to be labeled are contained in an Amazon S3 bucket. You create a manifest file that describes the location of each object. For more information, see Using Input and Output Data .
    The output can be used as the manifest file for another labeling job or as training data for your machine learning models.
    See also: AWS API Documentation
    
    
    :example: response = client.create_labeling_job(
        LabelingJobName='string',
        LabelAttributeName='string',
        InputConfig={
            'DataSource': {
                'S3DataSource': {
                    'ManifestS3Uri': 'string'
                }
            },
            'DataAttributes': {
                'ContentClassifiers': [
                    'FreeOfPersonallyIdentifiableInformation'|'FreeOfAdultContent',
                ]
            }
        },
        OutputConfig={
            'S3OutputPath': 'string',
            'KmsKeyId': 'string'
        },
        RoleArn='string',
        LabelCategoryConfigS3Uri='string',
        StoppingConditions={
            'MaxHumanLabeledObjectCount': 123,
            'MaxPercentageOfInputDatasetLabeled': 123
        },
        LabelingJobAlgorithmsConfig={
            'LabelingJobAlgorithmSpecificationArn': 'string',
            'InitialActiveLearningModelArn': 'string',
            'LabelingJobResourceConfig': {
                'VolumeKmsKeyId': 'string'
            }
        },
        HumanTaskConfig={
            'WorkteamArn': 'string',
            'UiConfig': {
                'UiTemplateS3Uri': 'string'
            },
            'PreHumanTaskLambdaArn': 'string',
            'TaskKeywords': [
                'string',
            ],
            'TaskTitle': 'string',
            'TaskDescription': 'string',
            'NumberOfHumanWorkersPerDataObject': 123,
            'TaskTimeLimitInSeconds': 123,
            'TaskAvailabilityLifetimeInSeconds': 123,
            'MaxConcurrentTaskCount': 123,
            'AnnotationConsolidationConfig': {
                'AnnotationConsolidationLambdaArn': 'string'
            },
            'PublicWorkforceTaskPrice': {
                'AmountInUsd': {
                    'Dollars': 123,
                    'Cents': 123,
                    'TenthFractionsOfACent': 123
                }
            }
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type LabelingJobName: string
    :param LabelingJobName: [REQUIRED]
            The name of the labeling job. This name is used to identify the job in a list of labeling jobs.
            

    :type LabelAttributeName: string
    :param LabelAttributeName: [REQUIRED]
            The attribute name to use for the label in the output manifest file. This is the key for the key/value pair formed with the label that a worker assigns to the object. The name can't end with '-metadata'. If you are running a semantic segmentation labeling job, the attribute name must end with '-ref'. If you are running any other kind of labeling job, the attribute name must not end with '-ref'.
            

    :type InputConfig: dict
    :param InputConfig: [REQUIRED]
            Input data for the labeling job, such as the Amazon S3 location of the data objects and the location of the manifest file that describes the data objects.
            DataSource (dict) -- [REQUIRED]The location of the input data.
            S3DataSource (dict) -- [REQUIRED]The Amazon S3 location of the input data objects.
            ManifestS3Uri (string) -- [REQUIRED]The Amazon S3 location of the manifest file that describes the input data objects.
            
            DataAttributes (dict) --Attributes of the data specified by the customer.
            ContentClassifiers (list) --Declares that your content is free of personally identifiable information or adult content. Amazon SageMaker may restrict the Amazon Mechanical Turk workers that can view your task based on this information.
            (string) --
            
            

    :type OutputConfig: dict
    :param OutputConfig: [REQUIRED]
            The location of the output data and the AWS Key Management Service key ID for the key used to encrypt the output data, if any.
            S3OutputPath (string) -- [REQUIRED]The Amazon S3 location to write output data.
            KmsKeyId (string) --The AWS Key Management Service ID of the key used to encrypt the output data, if any.
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Number (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during data labeling. You must grant this role the necessary permissions so that Amazon SageMaker can successfully complete data labeling.
            

    :type LabelCategoryConfigS3Uri: string
    :param LabelCategoryConfigS3Uri: The S3 URL of the file that defines the categories used to label the data objects.
            The file is a JSON structure in the following format:
            {'document-version': '2018-11-28'
            'labels': [
            {
            'label': '*label 1* '
            },
            {
            'label': '*label 2* '
            },
            ...
            {
            'label': '*label n* '
            }
            ]
            }
            

    :type StoppingConditions: dict
    :param StoppingConditions: A set of conditions for stopping the labeling job. If any of the conditions are met, the job is automatically stopped. You can use these conditions to control the cost of data labeling.
            MaxHumanLabeledObjectCount (integer) --The maximum number of objects that can be labeled by human workers.
            MaxPercentageOfInputDatasetLabeled (integer) --The maximum number of input data objects that should be labeled.
            

    :type LabelingJobAlgorithmsConfig: dict
    :param LabelingJobAlgorithmsConfig: Configures the information required to perform automated data labeling.
            LabelingJobAlgorithmSpecificationArn (string) -- [REQUIRED]Specifies the Amazon Resource Name (ARN) of the algorithm used for auto-labeling. You must select one of the following ARNs:
            Image classification arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/image-classification
            Text classification arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/text-classification
            Object detection arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/object-detection
            InitialActiveLearningModelArn (string) --At the end of an auto-label job Amazon SageMaker Ground Truth sends the Amazon Resource Nam (ARN) of the final model used for auto-labeling. You can use this model as the starting point for subsequent similar jobs by providing the ARN of the model here.
            LabelingJobResourceConfig (dict) --Provides configuration information for a labeling job.
            VolumeKmsKeyId (string) --The AWS Key Management Service key ID for the key used to encrypt the output data, if any.
            
            

    :type HumanTaskConfig: dict
    :param HumanTaskConfig: [REQUIRED]
            Configures the information required for human workers to complete a labeling task.
            WorkteamArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the work team assigned to complete the tasks.
            UiConfig (dict) -- [REQUIRED]Information about the user interface that workers use to complete the labeling task.
            UiTemplateS3Uri (string) -- [REQUIRED]The Amazon S3 bucket location of the UI template. For more information about the contents of a UI template, see Creating Your Custom Labeling Task Template .
            PreHumanTaskLambdaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of a Lambda function that is run before a data object is sent to a human worker. Use this function to provide input to a custom labeling job.
            For the built-in bounding box, image classification, semantic segmentation, and text classification task types, Amazon SageMaker Ground Truth provides the following Lambda functions:
            US East (Northern Virginia) (us-east-1):
            arn:aws:lambda:us-east-1:432418664414:function:PRE-BoundingBox
            arn:aws:lambda:us-east-1:432418664414:function:PRE-ImageMultiClass
            arn:aws:lambda:us-east-1:432418664414:function:PRE-SemanticSegmentation
            arn:aws:lambda:us-east-1:432418664414:function:PRE-TextMultiClass
            US East (Ohio) (us-east-2):
            arn:aws:lambda:us-east-2:266458841044:function:PRE-BoundingBox
            arn:aws:lambda:us-east-2:266458841044:function:PRE-ImageMultiClass
            arn:aws:lambda:us-east-2:266458841044:function:PRE-SemanticSegmentation
            arn:aws:lambda:us-east-2:266458841044:function:PRE-TextMultiClass
            US West (Oregon) (us-west-2):
            arn:aws:lambda:us-west-2:081040173940:function:PRE-BoundingBox
            arn:aws:lambda:us-west-2:081040173940:function:PRE-ImageMultiClass
            arn:aws:lambda:us-west-2:081040173940:function:PRE-SemanticSegmentation
            arn:aws:lambda:us-west-2:081040173940:function:PRE-TextMultiClass
            EU (Ireland) (eu-west-1):
            arn:aws:lambda:eu-west-1:568282634449:function:PRE-BoundingBox
            arn:aws:lambda:eu-west-1:568282634449:function:PRE-ImageMultiClass
            arn:aws:lambda:eu-west-1:568282634449:function:PRE-SemanticSegmentation
            arn:aws:lambda:eu-west-1:568282634449:function:PRE-TextMultiClass
            Asia Pacific (Tokyo (ap-northeast-1):
            arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-BoundingBox
            arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-ImageMultiClass
            arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-SemanticSegmentation
            arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-TextMultiClass
            TaskKeywords (list) --Keywords used to describe the task so that workers on Amazon Mechanical Turk can discover the task.
            (string) --
            TaskTitle (string) -- [REQUIRED]A title for the task for your human workers.
            TaskDescription (string) -- [REQUIRED]A description of the task for your human workers.
            NumberOfHumanWorkersPerDataObject (integer) -- [REQUIRED]The number of human workers that will label an object.
            TaskTimeLimitInSeconds (integer) -- [REQUIRED]The amount of time that a worker has to complete a task.
            TaskAvailabilityLifetimeInSeconds (integer) --The length of time that a task remains available for labelling by human workers.
            MaxConcurrentTaskCount (integer) --Defines the maximum number of data objects that can be labeled by human workers at the same time. Each object may have more than one worker at one time.
            AnnotationConsolidationConfig (dict) -- [REQUIRED]Configures how labels are consolidated across human workers.
            AnnotationConsolidationLambdaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of a Lambda function implements the logic for annotation consolidation.
            For the built-in bounding box, image classification, semantic segmentation, and text classification task types, Amazon SageMaker Ground Truth provides the following Lambda functions:
            Bounding box - Finds the most similar boxes from different workers based on the Jaccard index of the boxes. arn:aws:lambda:us-east-1:432418664414:function:ACS-BoundingBox arn:aws:lambda:us-east-2:266458841044:function:ACS-BoundingBox arn:aws:lambda:us-west-2:081040173940:function:ACS-BoundingBox arn:aws:lambda:eu-west-1:568282634449:function:ACS-BoundingBox arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-BoundingBox
            Image classification - Uses a variant of the Expectation Maximization approach to estimate the true class of an image based on annotations from individual workers. arn:aws:lambda:us-east-1:432418664414:function:ACS-ImageMultiClass arn:aws:lambda:us-east-2:266458841044:function:ACS-ImageMultiClass arn:aws:lambda:us-west-2:081040173940:function:ACS-ImageMultiClass arn:aws:lambda:eu-west-1:568282634449:function:ACS-ImageMultiClass arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-ImageMultiClass
            Semantic segmentation - Treats each pixel in an image as a multi-class classification and treats pixel annotations from workers as 'votes' for the correct label. arn:aws:lambda:us-east-1:432418664414:function:ACS-SemanticSegmentation arn:aws:lambda:us-east-2:266458841044:function:ACS-SemanticSegmentation arn:aws:lambda:us-west-2:081040173940:function:ACS-SemanticSegmentation arn:aws:lambda:eu-west-1:568282634449:function:ACS-SemanticSegmentation arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-SemanticSegmentation
            Text classification - Uses a variant of the Expectation Maximization approach to estimate the true class of text based on annotations from individual workers. arn:aws:lambda:us-east-1:432418664414:function:ACS-TextMultiClass arn:aws:lambda:us-east-2:266458841044:function:ACS-TextMultiClass arn:aws:lambda:us-west-2:081040173940:function:ACS-TextMultiClass arn:aws:lambda:eu-west-1:568282634449:function:ACS-TextMultiClass arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-TextMultiClass
            For more information, see Annotation Consolidation .
            PublicWorkforceTaskPrice (dict) --The price that you pay for each task performed by a public worker.
            AmountInUsd (dict) --Defines the amount of money paid to a worker in United States dollars.
            Dollars (integer) --The whole number of dollars in the amount.
            Cents (integer) --The fractional portion, in cents, of the amount.
            TenthFractionsOfACent (integer) --Fractions of a cent, in tenths.
            
            

    :type Tags: list
    :param Tags: An array of key/value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :rtype: dict
    :return: {
        'LabelingJobArn': 'string'
    }
    
    
    :returns: 
    LabelingJobName (string) -- [REQUIRED]
    The name of the labeling job. This name is used to identify the job in a list of labeling jobs.
    
    LabelAttributeName (string) -- [REQUIRED]
    The attribute name to use for the label in the output manifest file. This is the key for the key/value pair formed with the label that a worker assigns to the object. The name can't end with "-metadata". If you are running a semantic segmentation labeling job, the attribute name must end with "-ref". If you are running any other kind of labeling job, the attribute name must not end with "-ref".
    
    InputConfig (dict) -- [REQUIRED]
    Input data for the labeling job, such as the Amazon S3 location of the data objects and the location of the manifest file that describes the data objects.
    
    DataSource (dict) -- [REQUIRED]The location of the input data.
    
    S3DataSource (dict) -- [REQUIRED]The Amazon S3 location of the input data objects.
    
    ManifestS3Uri (string) -- [REQUIRED]The Amazon S3 location of the manifest file that describes the input data objects.
    
    
    
    
    
    DataAttributes (dict) --Attributes of the data specified by the customer.
    
    ContentClassifiers (list) --Declares that your content is free of personally identifiable information or adult content. Amazon SageMaker may restrict the Amazon Mechanical Turk workers that can view your task based on this information.
    
    (string) --
    
    
    
    
    
    
    OutputConfig (dict) -- [REQUIRED]
    The location of the output data and the AWS Key Management Service key ID for the key used to encrypt the output data, if any.
    
    S3OutputPath (string) -- [REQUIRED]The Amazon S3 location to write output data.
    
    KmsKeyId (string) --The AWS Key Management Service ID of the key used to encrypt the output data, if any.
    
    
    
    RoleArn (string) -- [REQUIRED]
    The Amazon Resource Number (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during data labeling. You must grant this role the necessary permissions so that Amazon SageMaker can successfully complete data labeling.
    
    LabelCategoryConfigS3Uri (string) -- The S3 URL of the file that defines the categories used to label the data objects.
    The file is a JSON structure in the following format:
    
    {"document-version": "2018-11-28"
    "labels": [
    {
    "label": "*label 1* "
    },
    {
    "label": "*label 2* "
    },
    ...
    {
    "label": "*label n* "
    }
    ]
    }
    
    
    StoppingConditions (dict) -- A set of conditions for stopping the labeling job. If any of the conditions are met, the job is automatically stopped. You can use these conditions to control the cost of data labeling.
    
    MaxHumanLabeledObjectCount (integer) --The maximum number of objects that can be labeled by human workers.
    
    MaxPercentageOfInputDatasetLabeled (integer) --The maximum number of input data objects that should be labeled.
    
    
    
    LabelingJobAlgorithmsConfig (dict) -- Configures the information required to perform automated data labeling.
    
    LabelingJobAlgorithmSpecificationArn (string) -- [REQUIRED]Specifies the Amazon Resource Name (ARN) of the algorithm used for auto-labeling. You must select one of the following ARNs:
    
    Image classification arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/image-classification
    Text classification arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/text-classification
    Object detection arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/object-detection
    
    
    InitialActiveLearningModelArn (string) --At the end of an auto-label job Amazon SageMaker Ground Truth sends the Amazon Resource Nam (ARN) of the final model used for auto-labeling. You can use this model as the starting point for subsequent similar jobs by providing the ARN of the model here.
    
    LabelingJobResourceConfig (dict) --Provides configuration information for a labeling job.
    
    VolumeKmsKeyId (string) --The AWS Key Management Service key ID for the key used to encrypt the output data, if any.
    
    
    
    
    
    HumanTaskConfig (dict) -- [REQUIRED]
    Configures the information required for human workers to complete a labeling task.
    
    WorkteamArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the work team assigned to complete the tasks.
    
    UiConfig (dict) -- [REQUIRED]Information about the user interface that workers use to complete the labeling task.
    
    UiTemplateS3Uri (string) -- [REQUIRED]The Amazon S3 bucket location of the UI template. For more information about the contents of a UI template, see Creating Your Custom Labeling Task Template .
    
    
    
    PreHumanTaskLambdaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of a Lambda function that is run before a data object is sent to a human worker. Use this function to provide input to a custom labeling job.
    For the built-in bounding box, image classification, semantic segmentation, and text classification task types, Amazon SageMaker Ground Truth provides the following Lambda functions:
    
    US East (Northern Virginia) (us-east-1):
    
    arn:aws:lambda:us-east-1:432418664414:function:PRE-BoundingBox
    arn:aws:lambda:us-east-1:432418664414:function:PRE-ImageMultiClass
    arn:aws:lambda:us-east-1:432418664414:function:PRE-SemanticSegmentation
    arn:aws:lambda:us-east-1:432418664414:function:PRE-TextMultiClass
    
    
    US East (Ohio) (us-east-2):
    
    arn:aws:lambda:us-east-2:266458841044:function:PRE-BoundingBox
    arn:aws:lambda:us-east-2:266458841044:function:PRE-ImageMultiClass
    arn:aws:lambda:us-east-2:266458841044:function:PRE-SemanticSegmentation
    arn:aws:lambda:us-east-2:266458841044:function:PRE-TextMultiClass
    
    
    US West (Oregon) (us-west-2):
    
    arn:aws:lambda:us-west-2:081040173940:function:PRE-BoundingBox
    arn:aws:lambda:us-west-2:081040173940:function:PRE-ImageMultiClass
    arn:aws:lambda:us-west-2:081040173940:function:PRE-SemanticSegmentation
    arn:aws:lambda:us-west-2:081040173940:function:PRE-TextMultiClass
    
    
    EU (Ireland) (eu-west-1):
    
    arn:aws:lambda:eu-west-1:568282634449:function:PRE-BoundingBox
    arn:aws:lambda:eu-west-1:568282634449:function:PRE-ImageMultiClass
    arn:aws:lambda:eu-west-1:568282634449:function:PRE-SemanticSegmentation
    arn:aws:lambda:eu-west-1:568282634449:function:PRE-TextMultiClass
    
    
    Asia Pacific (Tokyo (ap-northeast-1):
    
    arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-BoundingBox
    arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-ImageMultiClass
    arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-SemanticSegmentation
    arn:aws:lambda:ap-northeast-1:477331159723:function:PRE-TextMultiClass
    
    
    TaskKeywords (list) --Keywords used to describe the task so that workers on Amazon Mechanical Turk can discover the task.
    
    (string) --
    
    
    TaskTitle (string) -- [REQUIRED]A title for the task for your human workers.
    
    TaskDescription (string) -- [REQUIRED]A description of the task for your human workers.
    
    NumberOfHumanWorkersPerDataObject (integer) -- [REQUIRED]The number of human workers that will label an object.
    
    TaskTimeLimitInSeconds (integer) -- [REQUIRED]The amount of time that a worker has to complete a task.
    
    TaskAvailabilityLifetimeInSeconds (integer) --The length of time that a task remains available for labelling by human workers.
    
    MaxConcurrentTaskCount (integer) --Defines the maximum number of data objects that can be labeled by human workers at the same time. Each object may have more than one worker at one time.
    
    AnnotationConsolidationConfig (dict) -- [REQUIRED]Configures how labels are consolidated across human workers.
    
    AnnotationConsolidationLambdaArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of a Lambda function implements the logic for annotation consolidation.
    For the built-in bounding box, image classification, semantic segmentation, and text classification task types, Amazon SageMaker Ground Truth provides the following Lambda functions:
    
    Bounding box - Finds the most similar boxes from different workers based on the Jaccard index of the boxes.  arn:aws:lambda:us-east-1:432418664414:function:ACS-BoundingBox arn:aws:lambda:us-east-2:266458841044:function:ACS-BoundingBox arn:aws:lambda:us-west-2:081040173940:function:ACS-BoundingBox arn:aws:lambda:eu-west-1:568282634449:function:ACS-BoundingBox arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-BoundingBox
    Image classification - Uses a variant of the Expectation Maximization approach to estimate the true class of an image based on annotations from individual workers.  arn:aws:lambda:us-east-1:432418664414:function:ACS-ImageMultiClass arn:aws:lambda:us-east-2:266458841044:function:ACS-ImageMultiClass arn:aws:lambda:us-west-2:081040173940:function:ACS-ImageMultiClass arn:aws:lambda:eu-west-1:568282634449:function:ACS-ImageMultiClass arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-ImageMultiClass
    Semantic segmentation - Treats each pixel in an image as a multi-class classification and treats pixel annotations from workers as "votes" for the correct label.  arn:aws:lambda:us-east-1:432418664414:function:ACS-SemanticSegmentation arn:aws:lambda:us-east-2:266458841044:function:ACS-SemanticSegmentation arn:aws:lambda:us-west-2:081040173940:function:ACS-SemanticSegmentation arn:aws:lambda:eu-west-1:568282634449:function:ACS-SemanticSegmentation arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-SemanticSegmentation
    Text classification - Uses a variant of the Expectation Maximization approach to estimate the true class of text based on annotations from individual workers.  arn:aws:lambda:us-east-1:432418664414:function:ACS-TextMultiClass arn:aws:lambda:us-east-2:266458841044:function:ACS-TextMultiClass arn:aws:lambda:us-west-2:081040173940:function:ACS-TextMultiClass arn:aws:lambda:eu-west-1:568282634449:function:ACS-TextMultiClass arn:aws:lambda:ap-northeast-1:477331159723:function:ACS-TextMultiClass
    
    For more information, see Annotation Consolidation .
    
    
    
    PublicWorkforceTaskPrice (dict) --The price that you pay for each task performed by a public worker.
    
    AmountInUsd (dict) --Defines the amount of money paid to a worker in United States dollars.
    
    Dollars (integer) --The whole number of dollars in the amount.
    
    Cents (integer) --The fractional portion, in cents, of the amount.
    
    TenthFractionsOfACent (integer) --Fractions of a cent, in tenths.
    
    
    
    
    
    
    
    Tags (list) -- An array of key/value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    
    (dict) --Describes a tag.
    
    Key (string) -- [REQUIRED]The tag key.
    
    Value (string) -- [REQUIRED]The tag value.
    
    
    
    
    
    
    """
    pass

def create_model(ModelName=None, PrimaryContainer=None, Containers=None, ExecutionRoleArn=None, Tags=None, VpcConfig=None, EnableNetworkIsolation=None):
    """
    Creates a model in Amazon SageMaker. In the request, you name the model and describe a primary container. For the primary container, you specify the docker image containing inference code, artifacts (from prior training), and custom environment map that the inference code uses when you deploy the model for predictions.
    Use this API to create a model if you want to use Amazon SageMaker hosting services or run a batch transform job.
    To host your model, you create an endpoint configuration with the CreateEndpointConfig API, and then create an endpoint with the CreateEndpoint API. Amazon SageMaker then deploys all of the containers that you defined for the model in the hosting environment.
    To run a batch transform using your model, you start a job with the CreateTransformJob API. Amazon SageMaker uses your model and your dataset to get inferences which are then saved to a specified S3 location.
    In the CreateModel request, you must define a container with the PrimaryContainer parameter.
    In the request, you also provide an IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute hosting instances or for batch transform jobs. In addition, you also use the IAM role to manage permissions the inference code needs. For example, if the inference code access any other AWS resources, you grant necessary permissions via this role.
    See also: AWS API Documentation
    
    
    :example: response = client.create_model(
        ModelName='string',
        PrimaryContainer={
            'ContainerHostname': 'string',
            'Image': 'string',
            'ModelDataUrl': 'string',
            'Environment': {
                'string': 'string'
            },
            'ModelPackageName': 'string'
        },
        Containers=[
            {
                'ContainerHostname': 'string',
                'Image': 'string',
                'ModelDataUrl': 'string',
                'Environment': {
                    'string': 'string'
                },
                'ModelPackageName': 'string'
            },
        ],
        ExecutionRoleArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        VpcConfig={
            'SecurityGroupIds': [
                'string',
            ],
            'Subnets': [
                'string',
            ]
        },
        EnableNetworkIsolation=True|False
    )
    
    
    :type ModelName: string
    :param ModelName: [REQUIRED]
            The name of the new model.
            

    :type PrimaryContainer: dict
    :param PrimaryContainer: The location of the primary docker image containing inference code, associated artifacts, and custom environment map that the inference code uses when the model is deployed for predictions.
            ContainerHostname (string) --The DNS host name for the container after Amazon SageMaker deploys it.
            Image (string) --The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both registry/repository[:tag] and registry/repository[@digest] image path formats. For more information, see Using Your Own Algorithms with Amazon SageMaker
            ModelDataUrl (string) --The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
            If you provide a value for this parameter, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provide. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see Activating and Deactivating AWS STS in an AWS Region in the AWS Identity and Access Management User Guide .
            Environment (dict) --The environment variables to set in the Docker container. Each key and value in the Environment string to string map can have length of up to 1024. We support up to 16 entries in the map.
            (string) --
            (string) --
            
            ModelPackageName (string) --The name of the model package to use to create the model.
            

    :type Containers: list
    :param Containers: Specifies the containers in the inference pipeline.
            (dict) --Describes the container, as part of model definition.
            ContainerHostname (string) --The DNS host name for the container after Amazon SageMaker deploys it.
            Image (string) --The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both registry/repository[:tag] and registry/repository[@digest] image path formats. For more information, see Using Your Own Algorithms with Amazon SageMaker
            ModelDataUrl (string) --The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
            If you provide a value for this parameter, Amazon SageMaker uses AWS Security Token Service to download model artifacts from the S3 path you provide. AWS STS is activated in your IAM user account by default. If you previously deactivated AWS STS for a region, you need to reactivate AWS STS for that region. For more information, see Activating and Deactivating AWS STS in an AWS Region in the AWS Identity and Access Management User Guide .
            Environment (dict) --The environment variables to set in the Docker container. Each key and value in the Environment string to string map can have length of up to 1024. We support up to 16 entries in the map.
            (string) --
            (string) --
            
            ModelPackageName (string) --The name of the model package to use to create the model.
            
            

    :type ExecutionRoleArn: string
    :param ExecutionRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute instances or for batch transform jobs. Deploying on ML compute instances is part of model hosting. For more information, see Amazon SageMaker Roles .
            Note
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the iam:PassRole permission.
            

    :type Tags: list
    :param Tags: An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :type VpcConfig: dict
    :param VpcConfig: A VpcConfig object that specifies the VPC that you want your model to connect to. Control access to and from your model container by configuring the VPC. VpcConfig is used in hosting services and in batch transform. For more information, see Protect Endpoints by Using an Amazon Virtual Private Cloud and Protect Data in Batch Transform Jobs by Using an Amazon Virtual Private Cloud .
            SecurityGroupIds (list) -- [REQUIRED]The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the Subnets field.
            (string) --
            Subnets (list) -- [REQUIRED]The ID of the subnets in the VPC to which you want to connect your training job or model.
            (string) --
            

    :type EnableNetworkIsolation: boolean
    :param EnableNetworkIsolation: Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
            Note
            The Semantic Segmentation built-in algorithm does not support network isolation.
            

    :rtype: dict
    :return: {
        'ModelArn': 'string'
    }
    
    
    """
    pass

def create_model_package(ModelPackageName=None, ModelPackageDescription=None, InferenceSpecification=None, ValidationSpecification=None, SourceAlgorithmSpecification=None, CertifyForMarketplace=None):
    """
    Creates a model package that you can use to create Amazon SageMaker models or list on AWS Marketplace. Buyers can subscribe to model packages listed on AWS Marketplace to create models in Amazon SageMaker.
    To create a model package by specifying a Docker container that contains your inference code and the Amazon S3 location of your model artifacts, provide values for InferenceSpecification . To create a model from an algorithm resource that you created or subscribed to in AWS Marketplace, provide a value for SourceAlgorithmSpecification .
    See also: AWS API Documentation
    
    
    :example: response = client.create_model_package(
        ModelPackageName='string',
        ModelPackageDescription='string',
        InferenceSpecification={
            'Containers': [
                {
                    'ContainerHostname': 'string',
                    'Image': 'string',
                    'ImageDigest': 'string',
                    'ModelDataUrl': 'string',
                    'ProductId': 'string'
                },
            ],
            'SupportedTransformInstanceTypes': [
                'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
            ],
            'SupportedRealtimeInferenceInstanceTypes': [
                'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
            ],
            'SupportedContentTypes': [
                'string',
            ],
            'SupportedResponseMIMETypes': [
                'string',
            ]
        },
        ValidationSpecification={
            'ValidationRole': 'string',
            'ValidationProfiles': [
                {
                    'ProfileName': 'string',
                    'TransformJobDefinition': {
                        'MaxConcurrentTransforms': 123,
                        'MaxPayloadInMB': 123,
                        'BatchStrategy': 'MultiRecord'|'SingleRecord',
                        'Environment': {
                            'string': 'string'
                        },
                        'TransformInput': {
                            'DataSource': {
                                'S3DataSource': {
                                    'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                    'S3Uri': 'string'
                                }
                            },
                            'ContentType': 'string',
                            'CompressionType': 'None'|'Gzip',
                            'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
                        },
                        'TransformOutput': {
                            'S3OutputPath': 'string',
                            'Accept': 'string',
                            'AssembleWith': 'None'|'Line',
                            'KmsKeyId': 'string'
                        },
                        'TransformResources': {
                            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                            'InstanceCount': 123,
                            'VolumeKmsKeyId': 'string'
                        }
                    }
                },
            ]
        },
        SourceAlgorithmSpecification={
            'SourceAlgorithms': [
                {
                    'ModelDataUrl': 'string',
                    'AlgorithmName': 'string'
                },
            ]
        },
        CertifyForMarketplace=True|False
    )
    
    
    :type ModelPackageName: string
    :param ModelPackageName: [REQUIRED]
            The name of the model package. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
            

    :type ModelPackageDescription: string
    :param ModelPackageDescription: A description of the model package.

    :type InferenceSpecification: dict
    :param InferenceSpecification: Specifies details about inference jobs that can be run with models based on this model package, including the following:
            The Amazon ECR paths of containers that contain the inference code and model artifacts.
            The instance types that the model package supports for transform jobs and real-time endpoints used for inference.
            The input and output content formats that the model package supports for inference.
            Containers (list) -- [REQUIRED]The Amazon ECR registry path of the Docker image that contains the inference code.
            (dict) --Describes the Docker container for the model package.
            ContainerHostname (string) --The DNS host name for the Docker container.
            Image (string) -- [REQUIRED]The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored.
            If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. Amazon SageMaker supports both registry/repository[:tag] and registry/repository[@digest] image path formats. For more information, see Using Your Own Algorithms with Amazon SageMaker .
            ImageDigest (string) --An MD5 hash of the training algorithm that identifies the Docker image used for training.
            ModelDataUrl (string) --The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
            ProductId (string) --The AWS Marketplace product ID of the model package.
            
            SupportedTransformInstanceTypes (list) -- [REQUIRED]A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.
            (string) --
            SupportedRealtimeInferenceInstanceTypes (list) -- [REQUIRED]A list of the instance types that are used to generate inferences in real-time.
            (string) --
            SupportedContentTypes (list) -- [REQUIRED]The supported MIME types for the input data.
            (string) --
            SupportedResponseMIMETypes (list) -- [REQUIRED]The supported MIME types for the output data.
            (string) --
            

    :type ValidationSpecification: dict
    :param ValidationSpecification: Specifies configurations for one or more transform jobs that Amazon SageMaker runs to test the model package.
            ValidationRole (string) -- [REQUIRED]The IAM roles to be used for the validation of the model package.
            ValidationProfiles (list) -- [REQUIRED]An array of ModelPackageValidationProfile objects, each of which specifies a batch transform job that Amazon SageMaker runs to validate your model package.
            (dict) --Contains data, such as the inputs and targeted instance types that are used in the process of validating the model package.
            The data provided in the validation profile is made available to your buyers on AWS Marketplace.
            ProfileName (string) -- [REQUIRED]The name of the profile for the model package.
            TransformJobDefinition (dict) -- [REQUIRED]The TransformJobDefinition object that describes the transform job used for the validation of the model package.
            MaxConcurrentTransforms (integer) --The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.
            MaxPayloadInMB (integer) --The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).
            BatchStrategy (string) --A string that determines the number of records included in a single mini-batch.
            SingleRecord means only one record is used per mini-batch. MultiRecord means a mini-batch is set to contain as many records that can fit within the MaxPayloadInMB limit.
            Environment (dict) --The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
            (string) --
            (string) --
            
            TransformInput (dict) -- [REQUIRED]A description of the input source and the way the transform job consumes it.
            DataSource (dict) -- [REQUIRED]Describes the location of the channel data, meaning the S3 location of the input data that the model can consume.
            S3DataSource (dict) -- [REQUIRED]The S3 location of the data source that is associated with a channel.
            S3DataType (string) -- [REQUIRED]If you choose S3Prefix , S3Uri identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform.
            If you choose ManifestFile , S3Uri identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform.
            S3Uri (string) -- [REQUIRED]Depending on the value specified for the S3DataType , identifies either a key name prefix or a manifest. For example:
            A key name prefix might look like this: s3://bucketname/exampleprefix .
            A manifest might look like this: s3://bucketname/example.manifest  The manifest is an S3 object which is a JSON file with the following format:  [ {'prefix': 's3://customer_bucket/some/prefix/'}, 'relative/path/to/custdata-1', 'relative/path/custdata-2', ... ]  The preceding JSON matches the following S3Uris :  s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-1 ...  The complete set of S3Uris in this manifest constitutes the input data for the channel for this datasource. The object that each S3Uris points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
            
            ContentType (string) --The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.
            CompressionType (string) --Compressing data helps save on storage space. If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is None .
            SplitType (string) --The method to use to split the transform job's data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for SplitType is None , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to Line to split records on a newline character boundary. SplitType also supports a number of record-oriented binary data formats.
            When splitting is enabled, the size of a mini-batch depends on the values of the BatchStrategy and MaxPayloadInMB parameters. When the value of BatchStrategy is MultiRecord , Amazon SageMaker sends the maximum number of records in each request, up to the MaxPayloadInMB limit. If the value of BatchStrategy is SingleRecord , Amazon SageMaker sends individual records in each request.
            Note
            Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of BatchStrategy is set to SingleRecord . Padding is not removed if the value of BatchStrategy is set to MultiRecord .
            For more information about the RecordIO data format, see Data Format in the MXNet documentation. For more information about the TFRecord fofmat, see Consuming TFRecord data in the TensorFlow documentation.
            TransformOutput (dict) -- [REQUIRED]Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
            S3OutputPath (string) -- [REQUIRED]The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, s3://bucket-name/key-name-prefix .
            For every S3 object used as input for the transform job, the transformed data is stored in a corresponding subfolder in the location under the output prefix. For example, the input data s3://bucket-name/input-name-prefix/dataset01/data.csv will have the transformed data stored at s3://bucket-name/key-name-prefix/dataset01/ , based on the original name, as a series of .part files (.part0001, part0002, etc).
            Accept (string) --The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
            AssembleWith (string) --Defines how to assemble the results of the transform job as a single S3 object. You should select a format that is most convenient to you. To concatenate the results in binary format, specify None . To add a newline character at the end of every transformed record, specify Line .
            KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The KmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            // KMS Key Alias 'alias/ExampleAlias'
            // Amazon Resource Name (ARN) of a KMS Key Alias 'arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias'
            If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see KMS-Managed Encryption Keys in the Amazon Simple Storage Service Developer Guide.
            The KMS key policy must grant permission to the IAM role that you specify in your CreateTramsformJob request. For more information, see Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide .
            TransformResources (dict) -- [REQUIRED]Identifies the ML compute instances for the transform job.
            InstanceType (string) -- [REQUIRED]The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ml.m5.large should suffice. There is no default value for InstanceType .
            InstanceCount (integer) -- [REQUIRED]The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is 1 .
            VolumeKmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The VolumeKmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            
            
            

    :type SourceAlgorithmSpecification: dict
    :param SourceAlgorithmSpecification: Details about the algorithm that was used to create the model package.
            SourceAlgorithms (list) -- [REQUIRED]A list of the algorithms that were used to create a model package.
            (dict) --Specifies an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your Amazon SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.
            ModelDataUrl (string) --The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
            AlgorithmName (string) -- [REQUIRED]The name of an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your Amazon SageMaker account or an algorithm in AWS Marketplace that you are subscribed to.
            
            

    :type CertifyForMarketplace: boolean
    :param CertifyForMarketplace: Whether to certify the model package for listing on AWS Marketplace.

    :rtype: dict
    :return: {
        'ModelPackageArn': 'string'
    }
    
    
    """
    pass

def create_notebook_instance(NotebookInstanceName=None, InstanceType=None, SubnetId=None, SecurityGroupIds=None, RoleArn=None, KmsKeyId=None, Tags=None, LifecycleConfigName=None, DirectInternetAccess=None, VolumeSizeInGB=None, AcceleratorTypes=None, DefaultCodeRepository=None, AdditionalCodeRepositories=None):
    """
    Creates an Amazon SageMaker notebook instance. A notebook instance is a machine learning (ML) compute instance running on a Jupyter notebook.
    In a CreateNotebookInstance request, specify the type of ML compute instance that you want to run. Amazon SageMaker launches the instance, installs common libraries that you can use to explore datasets for model training, and attaches an ML storage volume to the notebook instance.
    Amazon SageMaker also provides a set of example notebooks. Each notebook demonstrates how to use Amazon SageMaker with a specific algorithm or with a machine learning framework.
    After receiving the request, Amazon SageMaker does the following:
    After creating the notebook instance, Amazon SageMaker returns its Amazon Resource Name (ARN).
    After Amazon SageMaker creates the notebook instance, you can connect to the Jupyter server and work in Jupyter notebooks. For example, you can write code to explore a dataset that you can use for model training, train a model, host models by creating Amazon SageMaker endpoints, and validate hosted models.
    For more information, see How It Works .
    See also: AWS API Documentation
    
    
    :example: response = client.create_notebook_instance(
        NotebookInstanceName='string',
        InstanceType='ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.t3.medium'|'ml.t3.large'|'ml.t3.xlarge'|'ml.t3.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.c5d.xlarge'|'ml.c5d.2xlarge'|'ml.c5d.4xlarge'|'ml.c5d.9xlarge'|'ml.c5d.18xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
        SubnetId='string',
        SecurityGroupIds=[
            'string',
        ],
        RoleArn='string',
        KmsKeyId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        LifecycleConfigName='string',
        DirectInternetAccess='Enabled'|'Disabled',
        VolumeSizeInGB=123,
        AcceleratorTypes=[
            'ml.eia1.medium'|'ml.eia1.large'|'ml.eia1.xlarge',
        ],
        DefaultCodeRepository='string',
        AdditionalCodeRepositories=[
            'string',
        ]
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the new notebook instance.
            

    :type InstanceType: string
    :param InstanceType: [REQUIRED]
            The type of ML compute instance to launch for the notebook instance.
            

    :type SubnetId: string
    :param SubnetId: The ID of the subnet in a VPC to which you would like to have a connectivity from your ML compute instance.

    :type SecurityGroupIds: list
    :param SecurityGroupIds: The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet.
            (string) --
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            When you send any requests to AWS resources from the notebook instance, Amazon SageMaker assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so Amazon SageMaker can perform these tasks. The policy must allow the Amazon SageMaker service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see Amazon SageMaker Roles .
            Note
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the iam:PassRole permission.
            

    :type KmsKeyId: string
    :param KmsKeyId: If you provide a AWS KMS key ID, Amazon SageMaker uses it to encrypt data at rest on the ML storage volume that is attached to your notebook instance. The KMS key you provide must be enabled. For information, see Enabling and Disabling Keys in the AWS Key Management Service Developer Guide .

    :type Tags: list
    :param Tags: A list of tags to associate with the notebook instance. You can add tags later by using the CreateTags API.
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :type LifecycleConfigName: string
    :param LifecycleConfigName: The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see Step 2.1: (Optional) Customize a Notebook Instance .

    :type DirectInternetAccess: string
    :param DirectInternetAccess: Sets whether Amazon SageMaker provides internet access to the notebook instance. If you set this to Disabled this notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.
            For more information, see Notebook Instances Are Internet-Enabled by Default . You can set the value of this parameter to Disabled only if you set a value for the SubnetId parameter.
            

    :type VolumeSizeInGB: integer
    :param VolumeSizeInGB: The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB.

    :type AcceleratorTypes: list
    :param AcceleratorTypes: A list of Elastic Inference (EI) instance types to associate with this notebook instance. Currently, only one instance type can be associated with a notebook intance. For more information, see Using Elastic Inference in Amazon SageMaker .
            (string) --
            

    :type DefaultCodeRepository: string
    :param DefaultCodeRepository: A git repository to associate with the notebook instance as its default code repository. This can be either the name of a git repository stored as a resource in your account, or the URL of a git repository in AWS CodeCommit or in any other git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see Associating Git Repositories with Amazon SageMaker Notebook Instances .

    :type AdditionalCodeRepositories: list
    :param AdditionalCodeRepositories: An array of up to 3 git repositories to associate with the notebook instance. These can be either the names of git repositories stored as resources in your account, or the URL of git repositories in AWS CodeCommit or in any other git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see Associating Git Repositories with Amazon SageMaker Notebook Instances .
            (string) --
            

    :rtype: dict
    :return: {
        'NotebookInstanceArn': 'string'
    }
    
    
    :returns: 
    NotebookInstanceName (string) -- [REQUIRED]
    The name of the new notebook instance.
    
    InstanceType (string) -- [REQUIRED]
    The type of ML compute instance to launch for the notebook instance.
    
    SubnetId (string) -- The ID of the subnet in a VPC to which you would like to have a connectivity from your ML compute instance.
    SecurityGroupIds (list) -- The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet.
    
    (string) --
    
    
    RoleArn (string) -- [REQUIRED]
    When you send any requests to AWS resources from the notebook instance, Amazon SageMaker assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so Amazon SageMaker can perform these tasks. The policy must allow the Amazon SageMaker service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see Amazon SageMaker Roles .
    
    Note
    To be able to pass this role to Amazon SageMaker, the caller of this API must have the iam:PassRole permission.
    
    
    KmsKeyId (string) -- If you provide a AWS KMS key ID, Amazon SageMaker uses it to encrypt data at rest on the ML storage volume that is attached to your notebook instance. The KMS key you provide must be enabled. For information, see Enabling and Disabling Keys in the AWS Key Management Service Developer Guide .
    Tags (list) -- A list of tags to associate with the notebook instance. You can add tags later by using the CreateTags API.
    
    (dict) --Describes a tag.
    
    Key (string) -- [REQUIRED]The tag key.
    
    Value (string) -- [REQUIRED]The tag value.
    
    
    
    
    
    LifecycleConfigName (string) -- The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see Step 2.1: (Optional) Customize a Notebook Instance .
    DirectInternetAccess (string) -- Sets whether Amazon SageMaker provides internet access to the notebook instance. If you set this to Disabled this notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.
    For more information, see Notebook Instances Are Internet-Enabled by Default . You can set the value of this parameter to Disabled only if you set a value for the SubnetId parameter.
    
    VolumeSizeInGB (integer) -- The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB.
    AcceleratorTypes (list) -- A list of Elastic Inference (EI) instance types to associate with this notebook instance. Currently, only one instance type can be associated with a notebook intance. For more information, see Using Elastic Inference in Amazon SageMaker .
    
    (string) --
    
    
    DefaultCodeRepository (string) -- A git repository to associate with the notebook instance as its default code repository. This can be either the name of a git repository stored as a resource in your account, or the URL of a git repository in AWS CodeCommit or in any other git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see Associating Git Repositories with Amazon SageMaker Notebook Instances .
    AdditionalCodeRepositories (list) -- An array of up to 3 git repositories to associate with the notebook instance. These can be either the names of git repositories stored as resources in your account, or the URL of git repositories in AWS CodeCommit or in any other git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see Associating Git Repositories with Amazon SageMaker Notebook Instances .
    
    (string) --
    
    
    
    """
    pass

def create_notebook_instance_lifecycle_config(NotebookInstanceLifecycleConfigName=None, OnCreate=None, OnStart=None):
    """
    Creates a lifecycle configuration that you can associate with a notebook instance. A lifecycle configuration is a collection of shell scripts that run when you create or start a notebook instance.
    Each lifecycle configuration script has a limit of 16384 characters.
    The value of the $PATH environment variable that is available to both scripts is /sbin:bin:/usr/sbin:/usr/bin .
    View CloudWatch Logs for notebook instance lifecycle configurations in log group /aws/sagemaker/NotebookInstances in log stream [notebook-instance-name]/[LifecycleConfigHook] .
    Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
    For information about notebook instance lifestyle configurations, see Step 2.1: (Optional) Customize a Notebook Instance .
    See also: AWS API Documentation
    
    
    :example: response = client.create_notebook_instance_lifecycle_config(
        NotebookInstanceLifecycleConfigName='string',
        OnCreate=[
            {
                'Content': 'string'
            },
        ],
        OnStart=[
            {
                'Content': 'string'
            },
        ]
    )
    
    
    :type NotebookInstanceLifecycleConfigName: string
    :param NotebookInstanceLifecycleConfigName: [REQUIRED]
            The name of the lifecycle configuration.
            

    :type OnCreate: list
    :param OnCreate: A shell script that runs only once, when you create a notebook instance. The shell script must be a base64-encoded string.
            (dict) --Contains the notebook instance lifecycle configuration script.
            Each lifecycle configuration script has a limit of 16384 characters.
            The value of the $PATH environment variable that is available to both scripts is /sbin:bin:/usr/sbin:/usr/bin .
            View CloudWatch Logs for notebook instance lifecycle configurations in log group /aws/sagemaker/NotebookInstances in log stream [notebook-instance-name]/[LifecycleConfigHook] .
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
            For information about notebook instance lifestyle configurations, see Step 2.1: (Optional) Customize a Notebook Instance .
            Content (string) --A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
            
            

    :type OnStart: list
    :param OnStart: A shell script that runs every time you start a notebook instance, including when you create the notebook instance. The shell script must be a base64-encoded string.
            (dict) --Contains the notebook instance lifecycle configuration script.
            Each lifecycle configuration script has a limit of 16384 characters.
            The value of the $PATH environment variable that is available to both scripts is /sbin:bin:/usr/sbin:/usr/bin .
            View CloudWatch Logs for notebook instance lifecycle configurations in log group /aws/sagemaker/NotebookInstances in log stream [notebook-instance-name]/[LifecycleConfigHook] .
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
            For information about notebook instance lifestyle configurations, see Step 2.1: (Optional) Customize a Notebook Instance .
            Content (string) --A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
            
            

    :rtype: dict
    :return: {
        'NotebookInstanceLifecycleConfigArn': 'string'
    }
    
    
    """
    pass

def create_presigned_notebook_instance_url(NotebookInstanceName=None, SessionExpirationDurationInSeconds=None):
    """
    Returns a URL that you can use to connect to the Jupyter server from a notebook instance. In the Amazon SageMaker console, when you choose Open next to a notebook instance, Amazon SageMaker opens a new tab showing the Jupyter server home page from the notebook instance. The console uses this API to get the URL and show the page.
    You can restrict access to this API and to the URL that it returns to a list of IP addresses that you specify. To restrict access, attach an IAM policy that denies access to this API unless the call comes from an IP address in the specified list to every AWS Identity and Access Management user, group, or role used to access the notebook instance. Use the NotIpAddress condition operator and the aws:SourceIP condition context key to specify the list of IP addresses that you want to have access to the notebook instance. For more information, see Limit Access to a Notebook Instance by IP Address .
    See also: AWS API Documentation
    
    
    :example: response = client.create_presigned_notebook_instance_url(
        NotebookInstanceName='string',
        SessionExpirationDurationInSeconds=123
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the notebook instance.
            

    :type SessionExpirationDurationInSeconds: integer
    :param SessionExpirationDurationInSeconds: The duration of the session, in seconds. The default is 12 hours.

    :rtype: dict
    :return: {
        'AuthorizedUrl': 'string'
    }
    
    
    """
    pass

def create_training_job(TrainingJobName=None, HyperParameters=None, AlgorithmSpecification=None, RoleArn=None, InputDataConfig=None, OutputDataConfig=None, ResourceConfig=None, VpcConfig=None, StoppingCondition=None, Tags=None, EnableNetworkIsolation=None):
    """
    Starts a model training job. After training completes, Amazon SageMaker saves the resulting model artifacts to an Amazon S3 location that you specify.
    If you choose to host your model using Amazon SageMaker hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts in a deep learning service other than Amazon SageMaker, provided that you know how to use them for inferences.
    In the request body, you provide the following:
    For more information about Amazon SageMaker, see How It Works .
    See also: AWS API Documentation
    
    
    :example: response = client.create_training_job(
        TrainingJobName='string',
        HyperParameters={
            'string': 'string'
        },
        AlgorithmSpecification={
            'TrainingImage': 'string',
            'AlgorithmName': 'string',
            'TrainingInputMode': 'Pipe'|'File',
            'MetricDefinitions': [
                {
                    'Name': 'string',
                    'Regex': 'string'
                },
            ]
        },
        RoleArn='string',
        InputDataConfig=[
            {
                'ChannelName': 'string',
                'DataSource': {
                    'S3DataSource': {
                        'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                        'S3Uri': 'string',
                        'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key',
                        'AttributeNames': [
                            'string',
                        ]
                    }
                },
                'ContentType': 'string',
                'CompressionType': 'None'|'Gzip',
                'RecordWrapperType': 'None'|'RecordIO',
                'InputMode': 'Pipe'|'File',
                'ShuffleConfig': {
                    'Seed': 123
                }
            },
        ],
        OutputDataConfig={
            'KmsKeyId': 'string',
            'S3OutputPath': 'string'
        },
        ResourceConfig={
            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
            'InstanceCount': 123,
            'VolumeSizeInGB': 123,
            'VolumeKmsKeyId': 'string'
        },
        VpcConfig={
            'SecurityGroupIds': [
                'string',
            ],
            'Subnets': [
                'string',
            ]
        },
        StoppingCondition={
            'MaxRuntimeInSeconds': 123
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        EnableNetworkIsolation=True|False
    )
    
    
    :type TrainingJobName: string
    :param TrainingJobName: [REQUIRED]
            The name of the training job. The name must be unique within an AWS Region in an AWS account.
            

    :type HyperParameters: dict
    :param HyperParameters: Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see Algorithms .
            You can specify a maximum of 100 hyperparameters. Each hyperparameter is a key-value pair. Each key and value is limited to 256 characters, as specified by the Length Constraint .
            (string) --
            (string) --
            

    :type AlgorithmSpecification: dict
    :param AlgorithmSpecification: [REQUIRED]
            The registry path of the Docker image that contains the training algorithm and algorithm-specific metadata, including the input mode. For more information about algorithms provided by Amazon SageMaker, see Algorithms . For information about providing your own algorithms, see Using Your Own Algorithms with Amazon SageMaker .
            TrainingImage (string) --The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for built-in algorithms, see Algorithms Provided by Amazon SageMaker: Common Parameters .
            AlgorithmName (string) --The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on AWS Marketplace. If you specify a value for this parameter, you can't specify a value for TrainingImage .
            TrainingInputMode (string) -- [REQUIRED]The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see Algorithms . If an algorithm supports the File input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the Pipe input mode, Amazon SageMaker streams data directly from S3 to the container.
            In File mode, make sure you provision ML storage volume with sufficient capacity to accommodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any.
            For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training.
            MetricDefinitions (list) --A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. Amazon SageMaker publishes each metric to Amazon CloudWatch.
            (dict) --Specifies a metric that the training algorithm writes to stderr or stdout . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
            Name (string) -- [REQUIRED]The name of the metric.
            Regex (string) -- [REQUIRED]A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see Defining Objective Metrics .
            
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
            During model training, Amazon SageMaker needs your permission to read input data from an S3 bucket, download a Docker image that contains training code, write model artifacts to an S3 bucket, write logs to Amazon CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant permissions for all of these tasks to an IAM role. For more information, see Amazon SageMaker Roles .
            Note
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the iam:PassRole permission.
            

    :type InputDataConfig: list
    :param InputDataConfig: An array of Channel objects. Each channel is a named input source. InputDataConfig describes the input data and its location.
            Algorithms can accept input data from one or more channels. For example, an algorithm might have two channels of input data, training_data and validation_data . The configuration for each channel provides the S3 location where the input data is stored. It also provides information about the stored data: the MIME type, compression method, and whether the data is wrapped in RecordIO format.
            Depending on the input mode that the algorithm supports, Amazon SageMaker either copies input data files from an S3 bucket to a local directory in the Docker container, or makes it available as input streams.
            (dict) --A channel is a named input source that training algorithms can consume.
            ChannelName (string) -- [REQUIRED]The name of the channel.
            DataSource (dict) -- [REQUIRED]The location of the channel data.
            S3DataSource (dict) -- [REQUIRED]The S3 location of the data source that is associated with a channel.
            S3DataType (string) -- [REQUIRED]If you choose S3Prefix , S3Uri identifies a key name prefix. Amazon SageMaker uses all objects that match the specified key name prefix for model training.
            If you choose ManifestFile , S3Uri identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training.
            If you choose AugmentedManifestFile , S3Uri identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. AugmentedManifestFile can only be used if the Channel's input mode is Pipe .
            S3Uri (string) -- [REQUIRED]Depending on the value specified for the S3DataType , identifies either a key name prefix or a manifest. For example:
            A key name prefix might look like this: s3://bucketname/exampleprefix .
            A manifest might look like this: s3://bucketname/example.manifest  The manifest is an S3 object which is a JSON file with the following format:  [ {'prefix': 's3://customer_bucket/some/prefix/'}, 'relative/path/to/custdata-1', 'relative/path/custdata-2', ... ]  The preceding JSON matches the following s3Uris :  s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-2 ...  The complete set of s3uris in this manifest is the input data for the channel for this datasource. The object that each s3uris points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
            S3DataDistributionType (string) --If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify FullyReplicated .
            If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ShardedByS3Key . If there are n ML compute instances launched for a training job, each instance gets approximately 1/n of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.
            Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.
            In distributed training, where you use multiple ML compute EC2 instances, you might choose ShardedByS3Key . If the algorithm requires copying training data to the ML storage volume (when TrainingInputMode is set to File ), this copies 1/n of the number of objects.
            AttributeNames (list) --A list of one or more attribute names to use that are found in a specified augmented manifest file.
            (string) --
            
            ContentType (string) --The MIME type of the data.
            CompressionType (string) --If training data is compressed, the compression type. The default value is None . CompressionType is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
            RecordWrapperType (string) --Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see Create a Dataset Using RecordIO .
            In File mode, leave this field unset or set it to None.
            InputMode (string) --(Optional) The input mode to use for the data channel in a training job. If you don't set a value for InputMode , Amazon SageMaker uses the value set for TrainingInputMode . Use this parameter to override the TrainingInputMode setting in a AlgorithmSpecification request when you have a channel that needs a different input mode from the training job's general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use File input mode. To stream data directly from Amazon S3 to the container, choose Pipe input mode.
            To use a model for incremental training, choose File input model.
            ShuffleConfig (dict) --A configuration for a shuffle option for input data in a channel. If you use S3Prefix for S3DataType , this shuffles the results of the S3 key prefix matches. If you use ManifestFile , the order of the S3 object references in the ManifestFile is shuffled. If you use AugmentedManifestFile , the order of the JSON lines in the AugmentedManifestFile is shuffled. The shuffling order is determined using the Seed value.
            For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with S3DataDistributionType of ShardedByS3Key , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.
            Seed (integer) -- [REQUIRED]Determines the shuffling order in ShuffleConfig value.
            
            

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]
            Specifies the path to the S3 bucket where you want to store model artifacts. Amazon SageMaker creates subfolders for the artifacts.
            KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The KmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            // KMS Key Alias 'alias/ExampleAlias'
            // Amazon Resource Name (ARN) of a KMS Key Alias 'arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias'
            If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see KMS-Managed Encryption Keys in the Amazon Simple Storage Service Developer Guide.
            The KMS key policy must grant permission to the IAM role that you specify in your CreateTramsformJob request. For more information, see Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide .
            S3OutputPath (string) -- [REQUIRED]Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, s3://bucket-name/key-name-prefix .
            

    :type ResourceConfig: dict
    :param ResourceConfig: [REQUIRED]
            The resources, including the ML compute instances and ML storage volumes, to use for model training.
            ML storage volumes store model artifacts and incremental states. Training algorithms might also use ML storage volumes for scratch space. If you want Amazon SageMaker to use the ML storage volume to store the training data, choose File as the TrainingInputMode in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.
            InstanceType (string) -- [REQUIRED]The ML compute instance type.
            InstanceCount (integer) -- [REQUIRED]The number of ML compute instances to use. For distributed training, provide a value greater than 1.
            VolumeSizeInGB (integer) -- [REQUIRED]The size of the ML storage volume that you want to provision.
            ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose File as the TrainingInputMode in the algorithm specification.
            You must specify sufficient ML storage for your scenario.
            Note
            Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type.
            VolumeKmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job. The VolumeKmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            

    :type VpcConfig: dict
    :param VpcConfig: A VpcConfig object that specifies the VPC that you want your training job to connect to. Control access to and from your training container by configuring the VPC. For more information, see Protect Training Jobs by Using an Amazon Virtual Private Cloud .
            SecurityGroupIds (list) -- [REQUIRED]The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the Subnets field.
            (string) --
            Subnets (list) -- [REQUIRED]The ID of the subnets in the VPC to which you want to connect your training job or model.
            (string) --
            

    :type StoppingCondition: dict
    :param StoppingCondition: [REQUIRED]
            Sets a duration for training. Use this parameter to cap model training costs. To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
            When Amazon SageMaker terminates a job because the stopping condition has been met, training algorithms provided by Amazon SageMaker save the intermediate results of the job. This intermediate data is a valid model artifact. You can use it to create a model using the CreateModel API.
            MaxRuntimeInSeconds (integer) --The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
            

    :type Tags: list
    :param Tags: An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :type EnableNetworkIsolation: boolean
    :param EnableNetworkIsolation: Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, Amazon SageMaker downloads and uploads customer data and model artifacts through the specifed VPC, but the training container does not have network access.
            Note
            The Semantic Segmentation built-in algorithm does not support network isolation.
            

    :rtype: dict
    :return: {
        'TrainingJobArn': 'string'
    }
    
    
    :returns: 
    TrainingJobName (string) -- [REQUIRED]
    The name of the training job. The name must be unique within an AWS Region in an AWS account.
    
    HyperParameters (dict) -- Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see Algorithms .
    You can specify a maximum of 100 hyperparameters. Each hyperparameter is a key-value pair. Each key and value is limited to 256 characters, as specified by the Length Constraint .
    
    (string) --
    (string) --
    
    
    
    
    AlgorithmSpecification (dict) -- [REQUIRED]
    The registry path of the Docker image that contains the training algorithm and algorithm-specific metadata, including the input mode. For more information about algorithms provided by Amazon SageMaker, see Algorithms . For information about providing your own algorithms, see Using Your Own Algorithms with Amazon SageMaker .
    
    TrainingImage (string) --The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for built-in algorithms, see Algorithms Provided by Amazon SageMaker: Common Parameters .
    
    AlgorithmName (string) --The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on AWS Marketplace. If you specify a value for this parameter, you can't specify a value for TrainingImage .
    
    TrainingInputMode (string) -- [REQUIRED]The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see Algorithms . If an algorithm supports the File input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the Pipe input mode, Amazon SageMaker streams data directly from S3 to the container.
    In File mode, make sure you provision ML storage volume with sufficient capacity to accommodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any.
    For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training.
    
    MetricDefinitions (list) --A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. Amazon SageMaker publishes each metric to Amazon CloudWatch.
    
    (dict) --Specifies a metric that the training algorithm writes to stderr or stdout . Amazon SageMakerhyperparameter tuning captures all defined metrics. You specify one metric that a hyperparameter tuning job uses as its objective metric to choose the best training job.
    
    Name (string) -- [REQUIRED]The name of the metric.
    
    Regex (string) -- [REQUIRED]A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see Defining Objective Metrics .
    
    
    
    
    
    
    
    RoleArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
    During model training, Amazon SageMaker needs your permission to read input data from an S3 bucket, download a Docker image that contains training code, write model artifacts to an S3 bucket, write logs to Amazon CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant permissions for all of these tasks to an IAM role. For more information, see Amazon SageMaker Roles .
    
    Note
    To be able to pass this role to Amazon SageMaker, the caller of this API must have the iam:PassRole permission.
    
    
    InputDataConfig (list) -- An array of Channel objects. Each channel is a named input source. InputDataConfig describes the input data and its location.
    Algorithms can accept input data from one or more channels. For example, an algorithm might have two channels of input data, training_data and validation_data . The configuration for each channel provides the S3 location where the input data is stored. It also provides information about the stored data: the MIME type, compression method, and whether the data is wrapped in RecordIO format.
    Depending on the input mode that the algorithm supports, Amazon SageMaker either copies input data files from an S3 bucket to a local directory in the Docker container, or makes it available as input streams.
    
    (dict) --A channel is a named input source that training algorithms can consume.
    
    ChannelName (string) -- [REQUIRED]The name of the channel.
    
    DataSource (dict) -- [REQUIRED]The location of the channel data.
    
    S3DataSource (dict) -- [REQUIRED]The S3 location of the data source that is associated with a channel.
    
    S3DataType (string) -- [REQUIRED]If you choose S3Prefix , S3Uri identifies a key name prefix. Amazon SageMaker uses all objects that match the specified key name prefix for model training.
    If you choose ManifestFile , S3Uri identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training.
    If you choose AugmentedManifestFile , S3Uri identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. AugmentedManifestFile can only be used if the Channel's input mode is Pipe .
    
    S3Uri (string) -- [REQUIRED]Depending on the value specified for the S3DataType , identifies either a key name prefix or a manifest. For example:
    
    A key name prefix might look like this: s3://bucketname/exampleprefix .
    A manifest might look like this: s3://bucketname/example.manifest   The manifest is an S3 object which is a JSON file with the following format:   [ {"prefix": "s3://customer_bucket/some/prefix/"}, "relative/path/to/custdata-1", "relative/path/custdata-2", ... ]   The preceding JSON matches the following s3Uris :   s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-2 ...   The complete set of s3uris in this manifest is the input data for the channel for this datasource. The object that each s3uris points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
    
    
    S3DataDistributionType (string) --If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify FullyReplicated .
    If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ShardedByS3Key . If there are n ML compute instances launched for a training job, each instance gets approximately 1/n of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.
    Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.
    In distributed training, where you use multiple ML compute EC2 instances, you might choose ShardedByS3Key . If the algorithm requires copying training data to the ML storage volume (when TrainingInputMode is set to File ), this copies 1/n of the number of objects.
    
    AttributeNames (list) --A list of one or more attribute names to use that are found in a specified augmented manifest file.
    
    (string) --
    
    
    
    
    
    
    ContentType (string) --The MIME type of the data.
    
    CompressionType (string) --If training data is compressed, the compression type. The default value is None . CompressionType is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
    
    RecordWrapperType (string) --Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, Amazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see Create a Dataset Using RecordIO .
    In File mode, leave this field unset or set it to None.
    
    InputMode (string) --(Optional) The input mode to use for the data channel in a training job. If you don't set a value for InputMode , Amazon SageMaker uses the value set for TrainingInputMode . Use this parameter to override the TrainingInputMode setting in a  AlgorithmSpecification request when you have a channel that needs a different input mode from the training job's general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use File input mode. To stream data directly from Amazon S3 to the container, choose Pipe input mode.
    To use a model for incremental training, choose File input model.
    
    ShuffleConfig (dict) --A configuration for a shuffle option for input data in a channel. If you use S3Prefix for S3DataType , this shuffles the results of the S3 key prefix matches. If you use ManifestFile , the order of the S3 object references in the ManifestFile is shuffled. If you use AugmentedManifestFile , the order of the JSON lines in the AugmentedManifestFile is shuffled. The shuffling order is determined using the Seed value.
    For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with S3DataDistributionType of ShardedByS3Key , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.
    
    Seed (integer) -- [REQUIRED]Determines the shuffling order in ShuffleConfig value.
    
    
    
    
    
    
    
    OutputDataConfig (dict) -- [REQUIRED]
    Specifies the path to the S3 bucket where you want to store model artifacts. Amazon SageMaker creates subfolders for the artifacts.
    
    KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The KmsKeyId can be any of the following formats:
    
    // KMS Key ID  "1234abcd-12ab-34cd-56ef-1234567890ab"
    // Amazon Resource Name (ARN) of a KMS Key  "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    // KMS Key Alias  "alias/ExampleAlias"
    // Amazon Resource Name (ARN) of a KMS Key Alias  "arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"
    
    If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see KMS-Managed Encryption Keys in the Amazon Simple Storage Service Developer Guide.
    The KMS key policy must grant permission to the IAM role that you specify in your CreateTramsformJob request. For more information, see Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide .
    
    S3OutputPath (string) -- [REQUIRED]Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, s3://bucket-name/key-name-prefix .
    
    
    
    ResourceConfig (dict) -- [REQUIRED]
    The resources, including the ML compute instances and ML storage volumes, to use for model training.
    ML storage volumes store model artifacts and incremental states. Training algorithms might also use ML storage volumes for scratch space. If you want Amazon SageMaker to use the ML storage volume to store the training data, choose File as the TrainingInputMode in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.
    
    InstanceType (string) -- [REQUIRED]The ML compute instance type.
    
    InstanceCount (integer) -- [REQUIRED]The number of ML compute instances to use. For distributed training, provide a value greater than 1.
    
    VolumeSizeInGB (integer) -- [REQUIRED]The size of the ML storage volume that you want to provision.
    ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose File as the TrainingInputMode in the algorithm specification.
    You must specify sufficient ML storage for your scenario.
    
    Note
    Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type.
    
    
    VolumeKmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job. The VolumeKmsKeyId can be any of the following formats:
    
    // KMS Key ID  "1234abcd-12ab-34cd-56ef-1234567890ab"
    // Amazon Resource Name (ARN) of a KMS Key  "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    
    
    
    
    VpcConfig (dict) -- A  VpcConfig object that specifies the VPC that you want your training job to connect to. Control access to and from your training container by configuring the VPC. For more information, see Protect Training Jobs by Using an Amazon Virtual Private Cloud .
    
    SecurityGroupIds (list) -- [REQUIRED]The VPC security group IDs, in the form sg-xxxxxxxx. Specify the security groups for the VPC that is specified in the Subnets field.
    
    (string) --
    
    
    Subnets (list) -- [REQUIRED]The ID of the subnets in the VPC to which you want to connect your training job or model.
    
    (string) --
    
    
    
    
    StoppingCondition (dict) -- [REQUIRED]
    Sets a duration for training. Use this parameter to cap model training costs. To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
    When Amazon SageMaker terminates a job because the stopping condition has been met, training algorithms provided by Amazon SageMaker save the intermediate results of the job. This intermediate data is a valid model artifact. You can use it to create a model using the CreateModel API.
    
    MaxRuntimeInSeconds (integer) --The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
    
    
    
    Tags (list) -- An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    
    (dict) --Describes a tag.
    
    Key (string) -- [REQUIRED]The tag key.
    
    Value (string) -- [REQUIRED]The tag value.
    
    
    
    
    
    EnableNetworkIsolation (boolean) -- Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, Amazon SageMaker downloads and uploads customer data and model artifacts through the specifed VPC, but the training container does not have network access.
    
    Note
    The Semantic Segmentation built-in algorithm does not support network isolation.
    
    
    
    """
    pass

def create_transform_job(TransformJobName=None, ModelName=None, MaxConcurrentTransforms=None, MaxPayloadInMB=None, BatchStrategy=None, Environment=None, TransformInput=None, TransformOutput=None, TransformResources=None, Tags=None):
    """
    Starts a transform job. A transform job uses a trained model to get inferences on a dataset and saves these results to an Amazon S3 location that you specify.
    To perform batch transformations, you create a transform job and use the data that you have readily available.
    In the request body, you provide the following:
    For more information about how batch transformation works Amazon SageMaker, see How It Works .
    See also: AWS API Documentation
    
    
    :example: response = client.create_transform_job(
        TransformJobName='string',
        ModelName='string',
        MaxConcurrentTransforms=123,
        MaxPayloadInMB=123,
        BatchStrategy='MultiRecord'|'SingleRecord',
        Environment={
            'string': 'string'
        },
        TransformInput={
            'DataSource': {
                'S3DataSource': {
                    'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                    'S3Uri': 'string'
                }
            },
            'ContentType': 'string',
            'CompressionType': 'None'|'Gzip',
            'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
        },
        TransformOutput={
            'S3OutputPath': 'string',
            'Accept': 'string',
            'AssembleWith': 'None'|'Line',
            'KmsKeyId': 'string'
        },
        TransformResources={
            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
            'InstanceCount': 123,
            'VolumeKmsKeyId': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type TransformJobName: string
    :param TransformJobName: [REQUIRED]
            The name of the transform job. The name must be unique within an AWS Region in an AWS account.
            

    :type ModelName: string
    :param ModelName: [REQUIRED]
            The name of the model that you want to use for the transform job. ModelName must be the name of an existing Amazon SageMaker model within an AWS Region in an AWS account.
            

    :type MaxConcurrentTransforms: integer
    :param MaxConcurrentTransforms: The maximum number of parallel requests that can be sent to each instance in a transform job. This is good for algorithms that implement multiple workers on larger instances . The default value is 1 . To allow Amazon SageMaker to determine the appropriate number for MaxConcurrentTransforms , set the value to 0 .

    :type MaxPayloadInMB: integer
    :param MaxPayloadInMB: The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata). The value in MaxPayloadInMB must be greater or equal to the size of a single record. You can approximate the size of a record by dividing the size of your dataset by the number of records. Then multiply this value by the number of records you want in a mini-batch. We recommend to enter a slightly larger value than this to ensure the records fit within the maximum payload size. The default value is 6 MB.
            For cases where the payload might be arbitrarily large and is transmitted using HTTP chunked encoding, set the value to 0 . This feature only works in supported algorithms. Currently, Amazon SageMaker built-in algorithms do not support this feature.
            

    :type BatchStrategy: string
    :param BatchStrategy: Determines the number of records included in a single mini-batch. SingleRecord means only one record is used per mini-batch. MultiRecord means a mini-batch is set to contain as many records that can fit within the MaxPayloadInMB limit.
            Batch transform will automatically split your input data into whatever payload size is specified if you set SplitType to Line and BatchStrategy to MultiRecord . There's no need to split the dataset into smaller files or to use larger payload sizes unless the records in your dataset are very large.
            

    :type Environment: dict
    :param Environment: The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
            (string) --
            (string) --
            

    :type TransformInput: dict
    :param TransformInput: [REQUIRED]
            Describes the input source and the way the transform job consumes it.
            DataSource (dict) -- [REQUIRED]Describes the location of the channel data, meaning the S3 location of the input data that the model can consume.
            S3DataSource (dict) -- [REQUIRED]The S3 location of the data source that is associated with a channel.
            S3DataType (string) -- [REQUIRED]If you choose S3Prefix , S3Uri identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform.
            If you choose ManifestFile , S3Uri identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform.
            S3Uri (string) -- [REQUIRED]Depending on the value specified for the S3DataType , identifies either a key name prefix or a manifest. For example:
            A key name prefix might look like this: s3://bucketname/exampleprefix .
            A manifest might look like this: s3://bucketname/example.manifest  The manifest is an S3 object which is a JSON file with the following format:  [ {'prefix': 's3://customer_bucket/some/prefix/'}, 'relative/path/to/custdata-1', 'relative/path/custdata-2', ... ]  The preceding JSON matches the following S3Uris :  s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-1 ...  The complete set of S3Uris in this manifest constitutes the input data for the channel for this datasource. The object that each S3Uris points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
            
            ContentType (string) --The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.
            CompressionType (string) --Compressing data helps save on storage space. If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is None .
            SplitType (string) --The method to use to split the transform job's data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for SplitType is None , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to Line to split records on a newline character boundary. SplitType also supports a number of record-oriented binary data formats.
            When splitting is enabled, the size of a mini-batch depends on the values of the BatchStrategy and MaxPayloadInMB parameters. When the value of BatchStrategy is MultiRecord , Amazon SageMaker sends the maximum number of records in each request, up to the MaxPayloadInMB limit. If the value of BatchStrategy is SingleRecord , Amazon SageMaker sends individual records in each request.
            Note
            Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of BatchStrategy is set to SingleRecord . Padding is not removed if the value of BatchStrategy is set to MultiRecord .
            For more information about the RecordIO data format, see Data Format in the MXNet documentation. For more information about the TFRecord fofmat, see Consuming TFRecord data in the TensorFlow documentation.
            

    :type TransformOutput: dict
    :param TransformOutput: [REQUIRED]
            Describes the results of the transform job.
            S3OutputPath (string) -- [REQUIRED]The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, s3://bucket-name/key-name-prefix .
            For every S3 object used as input for the transform job, the transformed data is stored in a corresponding subfolder in the location under the output prefix. For example, the input data s3://bucket-name/input-name-prefix/dataset01/data.csv will have the transformed data stored at s3://bucket-name/key-name-prefix/dataset01/ , based on the original name, as a series of .part files (.part0001, part0002, etc).
            Accept (string) --The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
            AssembleWith (string) --Defines how to assemble the results of the transform job as a single S3 object. You should select a format that is most convenient to you. To concatenate the results in binary format, specify None . To add a newline character at the end of every transformed record, specify Line .
            KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The KmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            // KMS Key Alias 'alias/ExampleAlias'
            // Amazon Resource Name (ARN) of a KMS Key Alias 'arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias'
            If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see KMS-Managed Encryption Keys in the Amazon Simple Storage Service Developer Guide.
            The KMS key policy must grant permission to the IAM role that you specify in your CreateTramsformJob request. For more information, see Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide .
            

    :type TransformResources: dict
    :param TransformResources: [REQUIRED]
            Describes the resources, including ML instance types and ML instance count, to use for the transform job.
            InstanceType (string) -- [REQUIRED]The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ml.m5.large should suffice. There is no default value for InstanceType .
            InstanceCount (integer) -- [REQUIRED]The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is 1 .
            VolumeKmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The VolumeKmsKeyId can be any of the following formats:
            // KMS Key ID '1234abcd-12ab-34cd-56ef-1234567890ab'
            // Amazon Resource Name (ARN) of a KMS Key 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'
            

    :type Tags: list
    :param Tags: An array of key-value pairs. Adding tags is optional. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :rtype: dict
    :return: {
        'TransformJobArn': 'string'
    }
    
    
    :returns: 
    TransformJobName (string) -- [REQUIRED]
    The name of the transform job. The name must be unique within an AWS Region in an AWS account.
    
    ModelName (string) -- [REQUIRED]
    The name of the model that you want to use for the transform job. ModelName must be the name of an existing Amazon SageMaker model within an AWS Region in an AWS account.
    
    MaxConcurrentTransforms (integer) -- The maximum number of parallel requests that can be sent to each instance in a transform job. This is good for algorithms that implement multiple workers on larger instances . The default value is 1 . To allow Amazon SageMaker to determine the appropriate number for MaxConcurrentTransforms , set the value to 0 .
    MaxPayloadInMB (integer) -- The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata). The value in MaxPayloadInMB must be greater or equal to the size of a single record. You can approximate the size of a record by dividing the size of your dataset by the number of records. Then multiply this value by the number of records you want in a mini-batch. We recommend to enter a slightly larger value than this to ensure the records fit within the maximum payload size. The default value is 6 MB.
    For cases where the payload might be arbitrarily large and is transmitted using HTTP chunked encoding, set the value to 0 . This feature only works in supported algorithms. Currently, Amazon SageMaker built-in algorithms do not support this feature.
    
    BatchStrategy (string) -- Determines the number of records included in a single mini-batch. SingleRecord means only one record is used per mini-batch. MultiRecord means a mini-batch is set to contain as many records that can fit within the MaxPayloadInMB limit.
    Batch transform will automatically split your input data into whatever payload size is specified if you set SplitType to Line and BatchStrategy to MultiRecord . There's no need to split the dataset into smaller files or to use larger payload sizes unless the records in your dataset are very large.
    
    Environment (dict) -- The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
    
    (string) --
    (string) --
    
    
    
    
    TransformInput (dict) -- [REQUIRED]
    Describes the input source and the way the transform job consumes it.
    
    DataSource (dict) -- [REQUIRED]Describes the location of the channel data, meaning the S3 location of the input data that the model can consume.
    
    S3DataSource (dict) -- [REQUIRED]The S3 location of the data source that is associated with a channel.
    
    S3DataType (string) -- [REQUIRED]If you choose S3Prefix , S3Uri identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform.
    If you choose ManifestFile , S3Uri identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform.
    
    S3Uri (string) -- [REQUIRED]Depending on the value specified for the S3DataType , identifies either a key name prefix or a manifest. For example:
    
    A key name prefix might look like this: s3://bucketname/exampleprefix .
    A manifest might look like this: s3://bucketname/example.manifest   The manifest is an S3 object which is a JSON file with the following format:   [ {"prefix": "s3://customer_bucket/some/prefix/"}, "relative/path/to/custdata-1", "relative/path/custdata-2", ... ]   The preceding JSON matches the following S3Uris :   s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-1 ...   The complete set of S3Uris in this manifest constitutes the input data for the channel for this datasource. The object that each S3Uris points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
    
    
    
    
    
    
    ContentType (string) --The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.
    
    CompressionType (string) --Compressing data helps save on storage space. If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is None .
    
    SplitType (string) --The method to use to split the transform job's data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for SplitType is None , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to Line to split records on a newline character boundary. SplitType also supports a number of record-oriented binary data formats.
    When splitting is enabled, the size of a mini-batch depends on the values of the BatchStrategy and MaxPayloadInMB parameters. When the value of BatchStrategy is MultiRecord , Amazon SageMaker sends the maximum number of records in each request, up to the MaxPayloadInMB limit. If the value of BatchStrategy is SingleRecord , Amazon SageMaker sends individual records in each request.
    
    Note
    Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of BatchStrategy is set to SingleRecord . Padding is not removed if the value of BatchStrategy is set to MultiRecord .
    
    For more information about the RecordIO data format, see Data Format in the MXNet documentation. For more information about the TFRecord fofmat, see Consuming TFRecord data in the TensorFlow documentation.
    
    
    
    TransformOutput (dict) -- [REQUIRED]
    Describes the results of the transform job.
    
    S3OutputPath (string) -- [REQUIRED]The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, s3://bucket-name/key-name-prefix .
    For every S3 object used as input for the transform job, the transformed data is stored in a corresponding subfolder in the location under the output prefix. For example, the input data s3://bucket-name/input-name-prefix/dataset01/data.csv will have the transformed data stored at s3://bucket-name/key-name-prefix/dataset01/ , based on the original name, as a series of .part files (.part0001, part0002, etc).
    
    Accept (string) --The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.
    
    AssembleWith (string) --Defines how to assemble the results of the transform job as a single S3 object. You should select a format that is most convenient to you. To concatenate the results in binary format, specify None . To add a newline character at the end of every transformed record, specify Line .
    
    KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The KmsKeyId can be any of the following formats:
    
    // KMS Key ID  "1234abcd-12ab-34cd-56ef-1234567890ab"
    // Amazon Resource Name (ARN) of a KMS Key  "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    // KMS Key Alias  "alias/ExampleAlias"
    // Amazon Resource Name (ARN) of a KMS Key Alias  "arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"
    
    If you don't provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see KMS-Managed Encryption Keys in the Amazon Simple Storage Service Developer Guide.
    The KMS key policy must grant permission to the IAM role that you specify in your CreateTramsformJob request. For more information, see Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide .
    
    
    
    TransformResources (dict) -- [REQUIRED]
    Describes the resources, including ML instance types and ML instance count, to use for the transform job.
    
    InstanceType (string) -- [REQUIRED]The ML compute instance type for the transform job. For using built-in algorithms to transform moderately sized datasets, ml.m4.xlarge or ml.m5.large should suffice. There is no default value for InstanceType .
    
    InstanceCount (integer) -- [REQUIRED]The number of ML compute instances to use in the transform job. For distributed transform, provide a value greater than 1. The default value is 1 .
    
    VolumeKmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the batch transform job. The VolumeKmsKeyId can be any of the following formats:
    
    // KMS Key ID  "1234abcd-12ab-34cd-56ef-1234567890ab"
    // Amazon Resource Name (ARN) of a KMS Key  "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    
    
    
    
    Tags (list) -- An array of key-value pairs. Adding tags is optional. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    
    (dict) --Describes a tag.
    
    Key (string) -- [REQUIRED]The tag key.
    
    Value (string) -- [REQUIRED]The tag value.
    
    
    
    
    
    
    """
    pass

def create_workteam(WorkteamName=None, MemberDefinitions=None, Description=None, Tags=None):
    """
    Creates a new work team for labeling your data. A work team is defined by one or more Amazon Cognito user pools. You must first create the user pools before you can create a work team.
    You cannot create more than 25 work teams in an account and region.
    See also: AWS API Documentation
    
    
    :example: response = client.create_workteam(
        WorkteamName='string',
        MemberDefinitions=[
            {
                'CognitoMemberDefinition': {
                    'UserPool': 'string',
                    'UserGroup': 'string',
                    'ClientId': 'string'
                }
            },
        ],
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type WorkteamName: string
    :param WorkteamName: [REQUIRED]
            The name of the work team. Use this name to identify the work team.
            

    :type MemberDefinitions: list
    :param MemberDefinitions: [REQUIRED]
            A list of MemberDefinition objects that contains objects that identify the Amazon Cognito user pool that makes up the work team. For more information, see Amazon Cognito User Pools .
            All of the CognitoMemberDefinition objects that make up the member definition must have the same ClientId and UserPool values.
            (dict) --Defines the Amazon Cognito user group that is part of a work team.
            CognitoMemberDefinition (dict) --The Amazon Cognito user group that is part of the work team.
            UserPool (string) -- [REQUIRED]An identifier for a user pool. The user pool must be in the same region as the service that you are calling.
            UserGroup (string) -- [REQUIRED]An identifier for a user group.
            ClientId (string) -- [REQUIRED]An identifier for an application client. You must create the app client ID using Amazon Cognito.
            
            

    :type Description: string
    :param Description: [REQUIRED]
            A description of the work team.
            

    :type Tags: list
    :param Tags: 
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :rtype: dict
    :return: {
        'WorkteamArn': 'string'
    }
    
    
    """
    pass

def delete_algorithm(AlgorithmName=None):
    """
    Removes the specified algorithm from your account.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_algorithm(
        AlgorithmName='string'
    )
    
    
    :type AlgorithmName: string
    :param AlgorithmName: [REQUIRED]
            The name of the algorithm to delete.
            

    """
    pass

def delete_code_repository(CodeRepositoryName=None):
    """
    Deletes the specified git repository from your account.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_code_repository(
        CodeRepositoryName='string'
    )
    
    
    :type CodeRepositoryName: string
    :param CodeRepositoryName: [REQUIRED]
            The name of the git repository to delete.
            

    """
    pass

def delete_endpoint(EndpointName=None):
    """
    Deletes an endpoint. Amazon SageMaker frees up all of the resources that were deployed when the endpoint was created.
    Amazon SageMaker retires any custom KMS key grants associated with the endpoint, meaning you don't need to use the RevokeGrant API call.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_endpoint(
        EndpointName='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of the endpoint that you want to delete.
            

    """
    pass

def delete_endpoint_config(EndpointConfigName=None):
    """
    Deletes an endpoint configuration. The DeleteEndpointConfig API deletes only the specified configuration. It does not delete endpoints created using the configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_endpoint_config(
        EndpointConfigName='string'
    )
    
    
    :type EndpointConfigName: string
    :param EndpointConfigName: [REQUIRED]
            The name of the endpoint configuration that you want to delete.
            

    """
    pass

def delete_model(ModelName=None):
    """
    Deletes a model. The DeleteModel API deletes only the model entry that was created in Amazon SageMaker when you called the CreateModel API. It does not delete model artifacts, inference code, or the IAM role that you specified when creating the model.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_model(
        ModelName='string'
    )
    
    
    :type ModelName: string
    :param ModelName: [REQUIRED]
            The name of the model to delete.
            

    """
    pass

def delete_model_package(ModelPackageName=None):
    """
    Deletes a model package.
    A model package is used to create Amazon SageMaker models or list on AWS Marketplace. Buyers can subscribe to model packages listed on AWS Marketplace to create models in Amazon SageMaker.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_model_package(
        ModelPackageName='string'
    )
    
    
    :type ModelPackageName: string
    :param ModelPackageName: [REQUIRED]
            The name of the model package. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
            

    """
    pass

def delete_notebook_instance(NotebookInstanceName=None):
    """
    Deletes an Amazon SageMaker notebook instance. Before you can delete a notebook instance, you must call the StopNotebookInstance API.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_notebook_instance(
        NotebookInstanceName='string'
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the Amazon SageMaker notebook instance to delete.
            

    """
    pass

def delete_notebook_instance_lifecycle_config(NotebookInstanceLifecycleConfigName=None):
    """
    Deletes a notebook instance lifecycle configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_notebook_instance_lifecycle_config(
        NotebookInstanceLifecycleConfigName='string'
    )
    
    
    :type NotebookInstanceLifecycleConfigName: string
    :param NotebookInstanceLifecycleConfigName: [REQUIRED]
            The name of the lifecycle configuration to delete.
            

    """
    pass

def delete_tags(ResourceArn=None, TagKeys=None):
    """
    Deletes the specified tags from an Amazon SageMaker resource.
    To list a resource's tags, use the ListTags API.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tags(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource whose tags you want to delete.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            An array or one or more tag keys to delete.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_workteam(WorkteamName=None):
    """
    Deletes an existing work team. This operation can't be undone.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_workteam(
        WorkteamName='string'
    )
    
    
    :type WorkteamName: string
    :param WorkteamName: [REQUIRED]
            The name of the work team to delete.
            

    :rtype: dict
    :return: {
        'Success': True|False
    }
    
    
    """
    pass

def describe_algorithm(AlgorithmName=None):
    """
    Returns a description of the specified algorithm that is in your account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_algorithm(
        AlgorithmName='string'
    )
    
    
    :type AlgorithmName: string
    :param AlgorithmName: [REQUIRED]
            The name of the algorithm to describe.
            

    :rtype: dict
    :return: {
        'AlgorithmName': 'string',
        'AlgorithmArn': 'string',
        'AlgorithmDescription': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'TrainingSpecification': {
            'TrainingImage': 'string',
            'TrainingImageDigest': 'string',
            'SupportedHyperParameters': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'Integer'|'Continuous'|'Categorical'|'FreeText',
                    'Range': {
                        'IntegerParameterRangeSpecification': {
                            'MinValue': 'string',
                            'MaxValue': 'string'
                        },
                        'ContinuousParameterRangeSpecification': {
                            'MinValue': 'string',
                            'MaxValue': 'string'
                        },
                        'CategoricalParameterRangeSpecification': {
                            'Values': [
                                'string',
                            ]
                        }
                    },
                    'IsTunable': True|False,
                    'IsRequired': True|False,
                    'DefaultValue': 'string'
                },
            ],
            'SupportedTrainingInstanceTypes': [
                'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
            ],
            'SupportsDistributedTraining': True|False,
            'MetricDefinitions': [
                {
                    'Name': 'string',
                    'Regex': 'string'
                },
            ],
            'TrainingChannels': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'IsRequired': True|False,
                    'SupportedContentTypes': [
                        'string',
                    ],
                    'SupportedCompressionTypes': [
                        'None'|'Gzip',
                    ],
                    'SupportedInputModes': [
                        'Pipe'|'File',
                    ]
                },
            ],
            'SupportedTuningJobObjectiveMetrics': [
                {
                    'Type': 'Maximize'|'Minimize',
                    'MetricName': 'string'
                },
            ]
        },
        'InferenceSpecification': {
            'Containers': [
                {
                    'ContainerHostname': 'string',
                    'Image': 'string',
                    'ImageDigest': 'string',
                    'ModelDataUrl': 'string',
                    'ProductId': 'string'
                },
            ],
            'SupportedTransformInstanceTypes': [
                'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
            ],
            'SupportedRealtimeInferenceInstanceTypes': [
                'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
            ],
            'SupportedContentTypes': [
                'string',
            ],
            'SupportedResponseMIMETypes': [
                'string',
            ]
        },
        'ValidationSpecification': {
            'ValidationRole': 'string',
            'ValidationProfiles': [
                {
                    'ProfileName': 'string',
                    'TrainingJobDefinition': {
                        'TrainingInputMode': 'Pipe'|'File',
                        'HyperParameters': {
                            'string': 'string'
                        },
                        'InputDataConfig': [
                            {
                                'ChannelName': 'string',
                                'DataSource': {
                                    'S3DataSource': {
                                        'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                        'S3Uri': 'string',
                                        'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key',
                                        'AttributeNames': [
                                            'string',
                                        ]
                                    }
                                },
                                'ContentType': 'string',
                                'CompressionType': 'None'|'Gzip',
                                'RecordWrapperType': 'None'|'RecordIO',
                                'InputMode': 'Pipe'|'File',
                                'ShuffleConfig': {
                                    'Seed': 123
                                }
                            },
                        ],
                        'OutputDataConfig': {
                            'KmsKeyId': 'string',
                            'S3OutputPath': 'string'
                        },
                        'ResourceConfig': {
                            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                            'InstanceCount': 123,
                            'VolumeSizeInGB': 123,
                            'VolumeKmsKeyId': 'string'
                        },
                        'StoppingCondition': {
                            'MaxRuntimeInSeconds': 123
                        }
                    },
                    'TransformJobDefinition': {
                        'MaxConcurrentTransforms': 123,
                        'MaxPayloadInMB': 123,
                        'BatchStrategy': 'MultiRecord'|'SingleRecord',
                        'Environment': {
                            'string': 'string'
                        },
                        'TransformInput': {
                            'DataSource': {
                                'S3DataSource': {
                                    'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                    'S3Uri': 'string'
                                }
                            },
                            'ContentType': 'string',
                            'CompressionType': 'None'|'Gzip',
                            'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
                        },
                        'TransformOutput': {
                            'S3OutputPath': 'string',
                            'Accept': 'string',
                            'AssembleWith': 'None'|'Line',
                            'KmsKeyId': 'string'
                        },
                        'TransformResources': {
                            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                            'InstanceCount': 123,
                            'VolumeKmsKeyId': 'string'
                        }
                    }
                },
            ]
        },
        'AlgorithmStatus': 'Pending'|'InProgress'|'Completed'|'Failed'|'Deleting',
        'AlgorithmStatusDetails': {
            'ValidationStatuses': [
                {
                    'Name': 'string',
                    'Status': 'NotStarted'|'InProgress'|'Completed'|'Failed',
                    'FailureReason': 'string'
                },
            ],
            'ImageScanStatuses': [
                {
                    'Name': 'string',
                    'Status': 'NotStarted'|'InProgress'|'Completed'|'Failed',
                    'FailureReason': 'string'
                },
            ]
        },
        'ProductId': 'string',
        'CertifyForMarketplace': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_code_repository(CodeRepositoryName=None):
    """
    Gets details about the specified git repository.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_code_repository(
        CodeRepositoryName='string'
    )
    
    
    :type CodeRepositoryName: string
    :param CodeRepositoryName: [REQUIRED]
            The name of the git repository to describe.
            

    :rtype: dict
    :return: {
        'CodeRepositoryName': 'string',
        'CodeRepositoryArn': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1),
        'GitConfig': {
            'RepositoryUrl': 'string',
            'Branch': 'string',
            'SecretArn': 'string'
        }
    }
    
    
    """
    pass

def describe_compilation_job(CompilationJobName=None):
    """
    Returns information about a model compilation job.
    To create a model compilation job, use  CreateCompilationJob . To get information about multiple model compilation jobs, use  ListCompilationJobs .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_compilation_job(
        CompilationJobName='string'
    )
    
    
    :type CompilationJobName: string
    :param CompilationJobName: [REQUIRED]
            The name of the model compilation job that you want information about.
            

    :rtype: dict
    :return: {
        'CompilationJobName': 'string',
        'CompilationJobArn': 'string',
        'CompilationJobStatus': 'INPROGRESS'|'COMPLETED'|'FAILED'|'STARTING'|'STOPPING'|'STOPPED',
        'CompilationStartTime': datetime(2015, 1, 1),
        'CompilationEndTime': datetime(2015, 1, 1),
        'StoppingCondition': {
            'MaxRuntimeInSeconds': 123
        },
        'CreationTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1),
        'FailureReason': 'string',
        'ModelArtifacts': {
            'S3ModelArtifacts': 'string'
        },
        'RoleArn': 'string',
        'InputConfig': {
            'S3Uri': 'string',
            'DataInputConfig': 'string',
            'Framework': 'TENSORFLOW'|'MXNET'|'ONNX'|'PYTORCH'|'XGBOOST'
        },
        'OutputConfig': {
            'S3OutputLocation': 'string',
            'TargetDevice': 'ml_m4'|'ml_m5'|'ml_c4'|'ml_c5'|'ml_p2'|'ml_p3'|'jetson_tx1'|'jetson_tx2'|'rasp3b'|'deeplens'
        }
    }
    
    
    """
    pass

def describe_endpoint(EndpointName=None):
    """
    Returns the description of an endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_endpoint(
        EndpointName='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of the endpoint.
            

    :rtype: dict
    :return: {
        'EndpointName': 'string',
        'EndpointArn': 'string',
        'EndpointConfigName': 'string',
        'ProductionVariants': [
            {
                'VariantName': 'string',
                'DeployedImages': [
                    {
                        'SpecifiedImage': 'string',
                        'ResolvedImage': 'string',
                        'ResolutionTime': datetime(2015, 1, 1)
                    },
                ],
                'CurrentWeight': ...,
                'DesiredWeight': ...,
                'CurrentInstanceCount': 123,
                'DesiredInstanceCount': 123
            },
        ],
        'EndpointStatus': 'OutOfService'|'Creating'|'Updating'|'SystemUpdating'|'RollingBack'|'InService'|'Deleting'|'Failed',
        'FailureReason': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_endpoint_config(EndpointConfigName=None):
    """
    Returns the description of an endpoint configuration created using the CreateEndpointConfig API.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_endpoint_config(
        EndpointConfigName='string'
    )
    
    
    :type EndpointConfigName: string
    :param EndpointConfigName: [REQUIRED]
            The name of the endpoint configuration.
            

    :rtype: dict
    :return: {
        'EndpointConfigName': 'string',
        'EndpointConfigArn': 'string',
        'ProductionVariants': [
            {
                'VariantName': 'string',
                'ModelName': 'string',
                'InitialInstanceCount': 123,
                'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                'InitialVariantWeight': ...,
                'AcceleratorType': 'ml.eia1.medium'|'ml.eia1.large'|'ml.eia1.xlarge'
            },
        ],
        'KmsKeyId': 'string',
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_hyper_parameter_tuning_job(HyperParameterTuningJobName=None):
    """
    Gets a description of a hyperparameter tuning job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_hyper_parameter_tuning_job(
        HyperParameterTuningJobName='string'
    )
    
    
    :type HyperParameterTuningJobName: string
    :param HyperParameterTuningJobName: [REQUIRED]
            The name of the tuning job to describe.
            

    :rtype: dict
    :return: {
        'HyperParameterTuningJobName': 'string',
        'HyperParameterTuningJobArn': 'string',
        'HyperParameterTuningJobConfig': {
            'Strategy': 'Bayesian',
            'HyperParameterTuningJobObjective': {
                'Type': 'Maximize'|'Minimize',
                'MetricName': 'string'
            },
            'ResourceLimits': {
                'MaxNumberOfTrainingJobs': 123,
                'MaxParallelTrainingJobs': 123
            },
            'ParameterRanges': {
                'IntegerParameterRanges': [
                    {
                        'Name': 'string',
                        'MinValue': 'string',
                        'MaxValue': 'string'
                    },
                ],
                'ContinuousParameterRanges': [
                    {
                        'Name': 'string',
                        'MinValue': 'string',
                        'MaxValue': 'string'
                    },
                ],
                'CategoricalParameterRanges': [
                    {
                        'Name': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ]
            },
            'TrainingJobEarlyStoppingType': 'Off'|'Auto'
        },
        'TrainingJobDefinition': {
            'StaticHyperParameters': {
                'string': 'string'
            },
            'AlgorithmSpecification': {
                'TrainingImage': 'string',
                'TrainingInputMode': 'Pipe'|'File',
                'AlgorithmName': 'string',
                'MetricDefinitions': [
                    {
                        'Name': 'string',
                        'Regex': 'string'
                    },
                ]
            },
            'RoleArn': 'string',
            'InputDataConfig': [
                {
                    'ChannelName': 'string',
                    'DataSource': {
                        'S3DataSource': {
                            'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                            'S3Uri': 'string',
                            'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key',
                            'AttributeNames': [
                                'string',
                            ]
                        }
                    },
                    'ContentType': 'string',
                    'CompressionType': 'None'|'Gzip',
                    'RecordWrapperType': 'None'|'RecordIO',
                    'InputMode': 'Pipe'|'File',
                    'ShuffleConfig': {
                        'Seed': 123
                    }
                },
            ],
            'VpcConfig': {
                'SecurityGroupIds': [
                    'string',
                ],
                'Subnets': [
                    'string',
                ]
            },
            'OutputDataConfig': {
                'KmsKeyId': 'string',
                'S3OutputPath': 'string'
            },
            'ResourceConfig': {
                'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                'InstanceCount': 123,
                'VolumeSizeInGB': 123,
                'VolumeKmsKeyId': 'string'
            },
            'StoppingCondition': {
                'MaxRuntimeInSeconds': 123
            },
            'EnableNetworkIsolation': True|False
        },
        'HyperParameterTuningJobStatus': 'Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
        'CreationTime': datetime(2015, 1, 1),
        'HyperParameterTuningEndTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1),
        'TrainingJobStatusCounters': {
            'Completed': 123,
            'InProgress': 123,
            'RetryableError': 123,
            'NonRetryableError': 123,
            'Stopped': 123
        },
        'ObjectiveStatusCounters': {
            'Succeeded': 123,
            'Pending': 123,
            'Failed': 123
        },
        'BestTrainingJob': {
            'TrainingJobName': 'string',
            'TrainingJobArn': 'string',
            'TuningJobName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TrainingStartTime': datetime(2015, 1, 1),
            'TrainingEndTime': datetime(2015, 1, 1),
            'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
            'TunedHyperParameters': {
                'string': 'string'
            },
            'FailureReason': 'string',
            'FinalHyperParameterTuningJobObjectiveMetric': {
                'Type': 'Maximize'|'Minimize',
                'MetricName': 'string',
                'Value': ...
            },
            'ObjectiveStatus': 'Succeeded'|'Pending'|'Failed'
        },
        'OverallBestTrainingJob': {
            'TrainingJobName': 'string',
            'TrainingJobArn': 'string',
            'TuningJobName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TrainingStartTime': datetime(2015, 1, 1),
            'TrainingEndTime': datetime(2015, 1, 1),
            'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
            'TunedHyperParameters': {
                'string': 'string'
            },
            'FailureReason': 'string',
            'FinalHyperParameterTuningJobObjectiveMetric': {
                'Type': 'Maximize'|'Minimize',
                'MetricName': 'string',
                'Value': ...
            },
            'ObjectiveStatus': 'Succeeded'|'Pending'|'Failed'
        },
        'WarmStartConfig': {
            'ParentHyperParameterTuningJobs': [
                {
                    'HyperParameterTuningJobName': 'string'
                },
            ],
            'WarmStartType': 'IdenticalDataAndAlgorithm'|'TransferLearning'
        },
        'FailureReason': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_labeling_job(LabelingJobName=None):
    """
    Gets information about a labeling job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_labeling_job(
        LabelingJobName='string'
    )
    
    
    :type LabelingJobName: string
    :param LabelingJobName: [REQUIRED]
            The name of the labeling job to return information for.
            

    :rtype: dict
    :return: {
        'LabelingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
        'LabelCounters': {
            'TotalLabeled': 123,
            'HumanLabeled': 123,
            'MachineLabeled': 123,
            'FailedNonRetryableError': 123,
            'Unlabeled': 123
        },
        'FailureReason': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1),
        'JobReferenceCode': 'string',
        'LabelingJobName': 'string',
        'LabelingJobArn': 'string',
        'LabelAttributeName': 'string',
        'InputConfig': {
            'DataSource': {
                'S3DataSource': {
                    'ManifestS3Uri': 'string'
                }
            },
            'DataAttributes': {
                'ContentClassifiers': [
                    'FreeOfPersonallyIdentifiableInformation'|'FreeOfAdultContent',
                ]
            }
        },
        'OutputConfig': {
            'S3OutputPath': 'string',
            'KmsKeyId': 'string'
        },
        'RoleArn': 'string',
        'LabelCategoryConfigS3Uri': 'string',
        'StoppingConditions': {
            'MaxHumanLabeledObjectCount': 123,
            'MaxPercentageOfInputDatasetLabeled': 123
        },
        'LabelingJobAlgorithmsConfig': {
            'LabelingJobAlgorithmSpecificationArn': 'string',
            'InitialActiveLearningModelArn': 'string',
            'LabelingJobResourceConfig': {
                'VolumeKmsKeyId': 'string'
            }
        },
        'HumanTaskConfig': {
            'WorkteamArn': 'string',
            'UiConfig': {
                'UiTemplateS3Uri': 'string'
            },
            'PreHumanTaskLambdaArn': 'string',
            'TaskKeywords': [
                'string',
            ],
            'TaskTitle': 'string',
            'TaskDescription': 'string',
            'NumberOfHumanWorkersPerDataObject': 123,
            'TaskTimeLimitInSeconds': 123,
            'TaskAvailabilityLifetimeInSeconds': 123,
            'MaxConcurrentTaskCount': 123,
            'AnnotationConsolidationConfig': {
                'AnnotationConsolidationLambdaArn': 'string'
            },
            'PublicWorkforceTaskPrice': {
                'AmountInUsd': {
                    'Dollars': 123,
                    'Cents': 123,
                    'TenthFractionsOfACent': 123
                }
            }
        },
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'LabelingJobOutput': {
            'OutputDatasetS3Uri': 'string',
            'FinalActiveLearningModelArn': 'string'
        }
    }
    
    
    :returns: 
    Image classification arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/image-classification
    Text classification arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/text-classification
    Object detection arn:aws:sagemaker:*region* :027400017018:labeling-job-algorithm-specification/object-detection
    
    """
    pass

def describe_model(ModelName=None):
    """
    Describes a model that you created using the CreateModel API.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_model(
        ModelName='string'
    )
    
    
    :type ModelName: string
    :param ModelName: [REQUIRED]
            The name of the model.
            

    :rtype: dict
    :return: {
        'ModelName': 'string',
        'PrimaryContainer': {
            'ContainerHostname': 'string',
            'Image': 'string',
            'ModelDataUrl': 'string',
            'Environment': {
                'string': 'string'
            },
            'ModelPackageName': 'string'
        },
        'Containers': [
            {
                'ContainerHostname': 'string',
                'Image': 'string',
                'ModelDataUrl': 'string',
                'Environment': {
                    'string': 'string'
                },
                'ModelPackageName': 'string'
            },
        ],
        'ExecutionRoleArn': 'string',
        'VpcConfig': {
            'SecurityGroupIds': [
                'string',
            ],
            'Subnets': [
                'string',
            ]
        },
        'CreationTime': datetime(2015, 1, 1),
        'ModelArn': 'string',
        'EnableNetworkIsolation': True|False
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_model_package(ModelPackageName=None):
    """
    Returns a description of the specified model package, which is used to create Amazon SageMaker models or list them on AWS Marketplace.
    To create models in Amazon SageMaker, buyers can subscribe to model packages listed on AWS Marketplace.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_model_package(
        ModelPackageName='string'
    )
    
    
    :type ModelPackageName: string
    :param ModelPackageName: [REQUIRED]
            The name of the model package to describe.
            

    :rtype: dict
    :return: {
        'ModelPackageName': 'string',
        'ModelPackageArn': 'string',
        'ModelPackageDescription': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'InferenceSpecification': {
            'Containers': [
                {
                    'ContainerHostname': 'string',
                    'Image': 'string',
                    'ImageDigest': 'string',
                    'ModelDataUrl': 'string',
                    'ProductId': 'string'
                },
            ],
            'SupportedTransformInstanceTypes': [
                'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
            ],
            'SupportedRealtimeInferenceInstanceTypes': [
                'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
            ],
            'SupportedContentTypes': [
                'string',
            ],
            'SupportedResponseMIMETypes': [
                'string',
            ]
        },
        'SourceAlgorithmSpecification': {
            'SourceAlgorithms': [
                {
                    'ModelDataUrl': 'string',
                    'AlgorithmName': 'string'
                },
            ]
        },
        'ValidationSpecification': {
            'ValidationRole': 'string',
            'ValidationProfiles': [
                {
                    'ProfileName': 'string',
                    'TransformJobDefinition': {
                        'MaxConcurrentTransforms': 123,
                        'MaxPayloadInMB': 123,
                        'BatchStrategy': 'MultiRecord'|'SingleRecord',
                        'Environment': {
                            'string': 'string'
                        },
                        'TransformInput': {
                            'DataSource': {
                                'S3DataSource': {
                                    'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                    'S3Uri': 'string'
                                }
                            },
                            'ContentType': 'string',
                            'CompressionType': 'None'|'Gzip',
                            'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
                        },
                        'TransformOutput': {
                            'S3OutputPath': 'string',
                            'Accept': 'string',
                            'AssembleWith': 'None'|'Line',
                            'KmsKeyId': 'string'
                        },
                        'TransformResources': {
                            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
                            'InstanceCount': 123,
                            'VolumeKmsKeyId': 'string'
                        }
                    }
                },
            ]
        },
        'ModelPackageStatus': 'Pending'|'InProgress'|'Completed'|'Failed'|'Deleting',
        'ModelPackageStatusDetails': {
            'ValidationStatuses': [
                {
                    'Name': 'string',
                    'Status': 'NotStarted'|'InProgress'|'Completed'|'Failed',
                    'FailureReason': 'string'
                },
            ],
            'ImageScanStatuses': [
                {
                    'Name': 'string',
                    'Status': 'NotStarted'|'InProgress'|'Completed'|'Failed',
                    'FailureReason': 'string'
                },
            ]
        },
        'CertifyForMarketplace': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_notebook_instance(NotebookInstanceName=None):
    """
    Returns information about a notebook instance.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_notebook_instance(
        NotebookInstanceName='string'
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the notebook instance that you want information about.
            

    :rtype: dict
    :return: {
        'NotebookInstanceArn': 'string',
        'NotebookInstanceName': 'string',
        'NotebookInstanceStatus': 'Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting'|'Updating',
        'FailureReason': 'string',
        'Url': 'string',
        'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.t3.medium'|'ml.t3.large'|'ml.t3.xlarge'|'ml.t3.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.c5d.xlarge'|'ml.c5d.2xlarge'|'ml.c5d.4xlarge'|'ml.c5d.9xlarge'|'ml.c5d.18xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
        'SubnetId': 'string',
        'SecurityGroups': [
            'string',
        ],
        'RoleArn': 'string',
        'KmsKeyId': 'string',
        'NetworkInterfaceId': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'CreationTime': datetime(2015, 1, 1),
        'NotebookInstanceLifecycleConfigName': 'string',
        'DirectInternetAccess': 'Enabled'|'Disabled',
        'VolumeSizeInGB': 123,
        'AcceleratorTypes': [
            'ml.eia1.medium'|'ml.eia1.large'|'ml.eia1.xlarge',
        ],
        'DefaultCodeRepository': 'string',
        'AdditionalCodeRepositories': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_notebook_instance_lifecycle_config(NotebookInstanceLifecycleConfigName=None):
    """
    Returns a description of a notebook instance lifecycle configuration.
    For information about notebook instance lifestyle configurations, see Step 2.1: (Optional) Customize a Notebook Instance .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_notebook_instance_lifecycle_config(
        NotebookInstanceLifecycleConfigName='string'
    )
    
    
    :type NotebookInstanceLifecycleConfigName: string
    :param NotebookInstanceLifecycleConfigName: [REQUIRED]
            The name of the lifecycle configuration to describe.
            

    :rtype: dict
    :return: {
        'NotebookInstanceLifecycleConfigArn': 'string',
        'NotebookInstanceLifecycleConfigName': 'string',
        'OnCreate': [
            {
                'Content': 'string'
            },
        ],
        'OnStart': [
            {
                'Content': 'string'
            },
        ],
        'LastModifiedTime': datetime(2015, 1, 1),
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_subscribed_workteam(WorkteamArn=None):
    """
    Gets information about a work team provided by a vendor. It returns details about the subscription with a vendor in the AWS Marketplace.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_subscribed_workteam(
        WorkteamArn='string'
    )
    
    
    :type WorkteamArn: string
    :param WorkteamArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the subscribed work team to describe.
            

    :rtype: dict
    :return: {
        'SubscribedWorkteam': {
            'WorkteamArn': 'string',
            'MarketplaceTitle': 'string',
            'SellerName': 'string',
            'MarketplaceDescription': 'string',
            'ListingId': 'string'
        }
    }
    
    
    """
    pass

def describe_training_job(TrainingJobName=None):
    """
    Returns information about a training job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_training_job(
        TrainingJobName='string'
    )
    
    
    :type TrainingJobName: string
    :param TrainingJobName: [REQUIRED]
            The name of the training job.
            

    :rtype: dict
    :return: {
        'TrainingJobName': 'string',
        'TrainingJobArn': 'string',
        'TuningJobArn': 'string',
        'LabelingJobArn': 'string',
        'ModelArtifacts': {
            'S3ModelArtifacts': 'string'
        },
        'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
        'SecondaryStatus': 'Starting'|'LaunchingMLInstances'|'PreparingTrainingStack'|'Downloading'|'DownloadingTrainingImage'|'Training'|'Uploading'|'Stopping'|'Stopped'|'MaxRuntimeExceeded'|'Completed'|'Failed',
        'FailureReason': 'string',
        'HyperParameters': {
            'string': 'string'
        },
        'AlgorithmSpecification': {
            'TrainingImage': 'string',
            'AlgorithmName': 'string',
            'TrainingInputMode': 'Pipe'|'File',
            'MetricDefinitions': [
                {
                    'Name': 'string',
                    'Regex': 'string'
                },
            ]
        },
        'RoleArn': 'string',
        'InputDataConfig': [
            {
                'ChannelName': 'string',
                'DataSource': {
                    'S3DataSource': {
                        'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                        'S3Uri': 'string',
                        'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key',
                        'AttributeNames': [
                            'string',
                        ]
                    }
                },
                'ContentType': 'string',
                'CompressionType': 'None'|'Gzip',
                'RecordWrapperType': 'None'|'RecordIO',
                'InputMode': 'Pipe'|'File',
                'ShuffleConfig': {
                    'Seed': 123
                }
            },
        ],
        'OutputDataConfig': {
            'KmsKeyId': 'string',
            'S3OutputPath': 'string'
        },
        'ResourceConfig': {
            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
            'InstanceCount': 123,
            'VolumeSizeInGB': 123,
            'VolumeKmsKeyId': 'string'
        },
        'VpcConfig': {
            'SecurityGroupIds': [
                'string',
            ],
            'Subnets': [
                'string',
            ]
        },
        'StoppingCondition': {
            'MaxRuntimeInSeconds': 123
        },
        'CreationTime': datetime(2015, 1, 1),
        'TrainingStartTime': datetime(2015, 1, 1),
        'TrainingEndTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1),
        'SecondaryStatusTransitions': [
            {
                'Status': 'Starting'|'LaunchingMLInstances'|'PreparingTrainingStack'|'Downloading'|'DownloadingTrainingImage'|'Training'|'Uploading'|'Stopping'|'Stopped'|'MaxRuntimeExceeded'|'Completed'|'Failed',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'StatusMessage': 'string'
            },
        ],
        'FinalMetricDataList': [
            {
                'MetricName': 'string',
                'Value': ...,
                'Timestamp': datetime(2015, 1, 1)
            },
        ],
        'EnableNetworkIsolation': True|False
    }
    
    
    :returns: 
    LaunchingMLInstances
    PreparingTrainingStack
    DownloadingTrainingImage
    
    """
    pass

def describe_transform_job(TransformJobName=None):
    """
    Returns information about a transform job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_transform_job(
        TransformJobName='string'
    )
    
    
    :type TransformJobName: string
    :param TransformJobName: [REQUIRED]
            The name of the transform job that you want to view details of.
            

    :rtype: dict
    :return: {
        'TransformJobName': 'string',
        'TransformJobArn': 'string',
        'TransformJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
        'FailureReason': 'string',
        'ModelName': 'string',
        'MaxConcurrentTransforms': 123,
        'MaxPayloadInMB': 123,
        'BatchStrategy': 'MultiRecord'|'SingleRecord',
        'Environment': {
            'string': 'string'
        },
        'TransformInput': {
            'DataSource': {
                'S3DataSource': {
                    'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                    'S3Uri': 'string'
                }
            },
            'ContentType': 'string',
            'CompressionType': 'None'|'Gzip',
            'SplitType': 'None'|'Line'|'RecordIO'|'TFRecord'
        },
        'TransformOutput': {
            'S3OutputPath': 'string',
            'Accept': 'string',
            'AssembleWith': 'None'|'Line',
            'KmsKeyId': 'string'
        },
        'TransformResources': {
            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge',
            'InstanceCount': 123,
            'VolumeKmsKeyId': 'string'
        },
        'CreationTime': datetime(2015, 1, 1),
        'TransformStartTime': datetime(2015, 1, 1),
        'TransformEndTime': datetime(2015, 1, 1),
        'LabelingJobArn': 'string'
    }
    
    
    :returns: 
    A key name prefix might look like this: s3://bucketname/exampleprefix .
    A manifest might look like this: s3://bucketname/example.manifest   The manifest is an S3 object which is a JSON file with the following format:   [ {"prefix": "s3://customer_bucket/some/prefix/"}, "relative/path/to/custdata-1", "relative/path/custdata-2", ... ]   The preceding JSON matches the following S3Uris :   s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-1 ...   The complete set of S3Uris in this manifest constitutes the input data for the channel for this datasource. The object that each S3Uris points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
    
    """
    pass

def describe_workteam(WorkteamName=None):
    """
    Gets information about a specific work team. You can see information such as the create date, the last updated date, membership information, and the work team's Amazon Resource Name (ARN).
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workteam(
        WorkteamName='string'
    )
    
    
    :type WorkteamName: string
    :param WorkteamName: [REQUIRED]
            The name of the work team to return a description of.
            

    :rtype: dict
    :return: {
        'Workteam': {
            'WorkteamName': 'string',
            'MemberDefinitions': [
                {
                    'CognitoMemberDefinition': {
                        'UserPool': 'string',
                        'UserGroup': 'string',
                        'ClientId': 'string'
                    }
                },
            ],
            'WorkteamArn': 'string',
            'ProductListingIds': [
                'string',
            ],
            'Description': 'string',
            'SubDomain': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'LastUpdatedDate': datetime(2015, 1, 1)
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

def get_search_suggestions(Resource=None, SuggestionQuery=None):
    """
    An auto-complete API for the search functionality in the Amazon SageMaker console. It returns suggestions of possible matches for the property name to use in Search queries. Provides suggestions for HyperParameters , Tags , and Metrics .
    See also: AWS API Documentation
    
    
    :example: response = client.get_search_suggestions(
        Resource='TrainingJob',
        SuggestionQuery={
            'PropertyNameQuery': {
                'PropertyNameHint': 'string'
            }
        }
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]
            The name of the Amazon SageMaker resource to Search for. The only valid Resource value is TrainingJob .
            

    :type SuggestionQuery: dict
    :param SuggestionQuery: Limits the property names that are included in the response.
            PropertyNameQuery (dict) --A type of SuggestionQuery . Defines a property name hint. Only property names that match the specified hint are included in the response.
            PropertyNameHint (string) -- [REQUIRED]Text that is part of a property's name. The property names of hyperparameter, metric, and tag key names that begin with the specified text in the PropertyNameHint .
            
            

    :rtype: dict
    :return: {
        'PropertyNameSuggestions': [
            {
                'PropertyName': 'string'
            },
        ]
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

def list_algorithms(CreationTimeAfter=None, CreationTimeBefore=None, MaxResults=None, NameContains=None, NextToken=None, SortBy=None, SortOrder=None):
    """
    Lists the machine learning algorithms that have been created.
    See also: AWS API Documentation
    
    
    :example: response = client.list_algorithms(
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        MaxResults=123,
        NameContains='string',
        NextToken='string',
        SortBy='Name'|'CreationTime',
        SortOrder='Ascending'|'Descending'
    )
    
    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only algorithms created after the specified time (timestamp).

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only algorithms created before the specified time (timestamp).

    :type MaxResults: integer
    :param MaxResults: The maximum number of algorithms to return in the response.

    :type NameContains: string
    :param NameContains: A string in the algorithm name. This filter returns only algorithms whose name contains the specified string.

    :type NextToken: string
    :param NextToken: If the response to a previous ListAlgorithms request was truncated, the response includes a NextToken . To retrieve the next set of algorithms, use the token in the next request.

    :type SortBy: string
    :param SortBy: The parameter by which to sort the results. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for the results. The default is Ascending .

    :rtype: dict
    :return: {
        'AlgorithmSummaryList': [
            {
                'AlgorithmName': 'string',
                'AlgorithmArn': 'string',
                'AlgorithmDescription': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'AlgorithmStatus': 'Pending'|'InProgress'|'Completed'|'Failed'|'Deleting'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_code_repositories(CreationTimeAfter=None, CreationTimeBefore=None, LastModifiedTimeAfter=None, LastModifiedTimeBefore=None, MaxResults=None, NameContains=None, NextToken=None, SortBy=None, SortOrder=None):
    """
    Gets a list of the git repositories in your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_code_repositories(
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        MaxResults=123,
        NameContains='string',
        NextToken='string',
        SortBy='Name'|'CreationTime'|'LastModifiedTime',
        SortOrder='Ascending'|'Descending'
    )
    
    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only git repositories that were created after the specified time.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only git repositories that were created before the specified time.

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only git repositories that were last modified after the specified time.

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only git repositories that were last modified before the specified time.

    :type MaxResults: integer
    :param MaxResults: The maximum number of git repositories to return in the response.

    :type NameContains: string
    :param NameContains: A string in the git repositories name. This filter returns only repositories whose name contains the specified string.

    :type NextToken: string
    :param NextToken: If the result of a ListCodeRepositoriesOutput request was truncated, the response includes a NextToken . To get the next set of git repositories, use the token in the next request.

    :type SortBy: string
    :param SortBy: The field to sort results by. The default is Name .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :rtype: dict
    :return: {
        'CodeRepositorySummaryList': [
            {
                'CodeRepositoryName': 'string',
                'CodeRepositoryArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'GitConfig': {
                    'RepositoryUrl': 'string',
                    'Branch': 'string',
                    'SecretArn': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Name
    Amazon Resource Name (ARN)
    Creation time
    Last modified time
    Configuration information, including the URL location of the repository and the ARN of the AWS Secrets Manager secret that contains the credentials used to access the repository.
    
    
    """
    pass

def list_compilation_jobs(NextToken=None, MaxResults=None, CreationTimeAfter=None, CreationTimeBefore=None, LastModifiedTimeAfter=None, LastModifiedTimeBefore=None, NameContains=None, StatusEquals=None, SortBy=None, SortOrder=None):
    """
    Lists model compilation jobs that satisfy various filters.
    To create a model compilation job, use  CreateCompilationJob . To get information about a particular model compilation job you have created, use  DescribeCompilationJob .
    See also: AWS API Documentation
    
    
    :example: response = client.list_compilation_jobs(
        NextToken='string',
        MaxResults=123,
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        NameContains='string',
        StatusEquals='INPROGRESS'|'COMPLETED'|'FAILED'|'STARTING'|'STOPPING'|'STOPPED',
        SortBy='Name'|'CreationTime'|'Status',
        SortOrder='Ascending'|'Descending'
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of the previous ListCompilationJobs request was truncated, the response includes a NextToken . To retrieve the next set of model compilation jobs, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of model compilation jobs to return in the response.

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns the model compilation jobs that were created after a specified time.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns the model compilation jobs that were created before a specified time.

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns the model compilation jobs that were modified after a specified time.

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns the model compilation jobs that were modified before a specified time.

    :type NameContains: string
    :param NameContains: A filter that returns the model compilation jobs whose name contains a specified string.

    :type StatusEquals: string
    :param StatusEquals: A filter that retrieves model compilation jobs with a specific DescribeCompilationJobResponse$CompilationJobStatus status.

    :type SortBy: string
    :param SortBy: The field by which to sort results. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :rtype: dict
    :return: {
        'CompilationJobSummaries': [
            {
                'CompilationJobName': 'string',
                'CompilationJobArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'CompilationStartTime': datetime(2015, 1, 1),
                'CompilationEndTime': datetime(2015, 1, 1),
                'CompilationTargetDevice': 'ml_m4'|'ml_m5'|'ml_c4'|'ml_c5'|'ml_p2'|'ml_p3'|'jetson_tx1'|'jetson_tx2'|'rasp3b'|'deeplens',
                'LastModifiedTime': datetime(2015, 1, 1),
                'CompilationJobStatus': 'INPROGRESS'|'COMPLETED'|'FAILED'|'STARTING'|'STOPPING'|'STOPPED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_endpoint_configs(SortBy=None, SortOrder=None, NextToken=None, MaxResults=None, NameContains=None, CreationTimeBefore=None, CreationTimeAfter=None):
    """
    Lists endpoint configurations.
    See also: AWS API Documentation
    
    
    :example: response = client.list_endpoint_configs(
        SortBy='Name'|'CreationTime',
        SortOrder='Ascending'|'Descending',
        NextToken='string',
        MaxResults=123,
        NameContains='string',
        CreationTimeBefore=datetime(2015, 1, 1),
        CreationTimeAfter=datetime(2015, 1, 1)
    )
    
    
    :type SortBy: string
    :param SortBy: The field to sort results by. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :type NextToken: string
    :param NextToken: If the result of the previous ListEndpointConfig request was truncated, the response includes a NextToken . To retrieve the next set of endpoint configurations, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of training jobs to return in the response.

    :type NameContains: string
    :param NameContains: A string in the endpoint configuration name. This filter returns only endpoint configurations whose name contains the specified string.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only endpoint configurations created before the specified time (timestamp).

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only endpoint configurations created after the specified time (timestamp).

    :rtype: dict
    :return: {
        'EndpointConfigs': [
            {
                'EndpointConfigName': 'string',
                'EndpointConfigArn': 'string',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_endpoints(SortBy=None, SortOrder=None, NextToken=None, MaxResults=None, NameContains=None, CreationTimeBefore=None, CreationTimeAfter=None, LastModifiedTimeBefore=None, LastModifiedTimeAfter=None, StatusEquals=None):
    """
    Lists endpoints.
    See also: AWS API Documentation
    
    
    :example: response = client.list_endpoints(
        SortBy='Name'|'CreationTime'|'Status',
        SortOrder='Ascending'|'Descending',
        NextToken='string',
        MaxResults=123,
        NameContains='string',
        CreationTimeBefore=datetime(2015, 1, 1),
        CreationTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        StatusEquals='OutOfService'|'Creating'|'Updating'|'SystemUpdating'|'RollingBack'|'InService'|'Deleting'|'Failed'
    )
    
    
    :type SortBy: string
    :param SortBy: Sorts the list of results. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :type NextToken: string
    :param NextToken: If the result of a ListEndpoints request was truncated, the response includes a NextToken . To retrieve the next set of endpoints, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of endpoints to return in the response.

    :type NameContains: string
    :param NameContains: A string in endpoint names. This filter returns only endpoints whose name contains the specified string.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only endpoints that were created before the specified time (timestamp).

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only endpoints that were created after the specified time (timestamp).

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only endpoints that were modified before the specified timestamp.

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only endpoints that were modified after the specified timestamp.

    :type StatusEquals: string
    :param StatusEquals: A filter that returns only endpoints with the specified status.

    :rtype: dict
    :return: {
        'Endpoints': [
            {
                'EndpointName': 'string',
                'EndpointArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'EndpointStatus': 'OutOfService'|'Creating'|'Updating'|'SystemUpdating'|'RollingBack'|'InService'|'Deleting'|'Failed'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    OutOfService : Endpoint is not available to take incoming requests.
    Creating :  CreateEndpoint is executing.
    Updating :  UpdateEndpoint or  UpdateEndpointWeightsAndCapacities is executing.
    SystemUpdating : Endpoint is undergoing maintenance and cannot be updated or deleted or re-scaled until it has completed. This mainenance operation does not change any customer-specified values such as VPC config, KMS encryption, model, instance type, or instance count.
    RollingBack : Endpoint fails to scale up or down or change its variant weight and is in the process of rolling back to its previous configuration. Once the rollback completes, endpoint returns to an InService status. This transitional status only applies to an endpoint that has autoscaling enabled and is undergoing variant weight or capacity changes as part of an  UpdateEndpointWeightsAndCapacities call or when the  UpdateEndpointWeightsAndCapacities operation is called explicitly.
    InService : Endpoint is available to process incoming requests.
    Deleting :  DeleteEndpoint is executing.
    Failed : Endpoint could not be created, updated, or re-scaled. Use  DescribeEndpointOutput$FailureReason for information about the failure.  DeleteEndpoint is the only operation that can be performed on a failed endpoint.
    
    """
    pass

def list_hyper_parameter_tuning_jobs(NextToken=None, MaxResults=None, SortBy=None, SortOrder=None, NameContains=None, CreationTimeAfter=None, CreationTimeBefore=None, LastModifiedTimeAfter=None, LastModifiedTimeBefore=None, StatusEquals=None):
    """
    Gets a list of  HyperParameterTuningJobSummary objects that describe the hyperparameter tuning jobs launched in your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_hyper_parameter_tuning_jobs(
        NextToken='string',
        MaxResults=123,
        SortBy='Name'|'Status'|'CreationTime',
        SortOrder='Ascending'|'Descending',
        NameContains='string',
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        StatusEquals='Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping'
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of the previous ListHyperParameterTuningJobs request was truncated, the response includes a NextToken . To retrieve the next set of tuning jobs, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of tuning jobs to return. The default value is 10.

    :type SortBy: string
    :param SortBy: The field to sort results by. The default is Name .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :type NameContains: string
    :param NameContains: A string in the tuning job name. This filter returns only tuning jobs whose name contains the specified string.

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only tuning jobs that were created after the specified time.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only tuning jobs that were created before the specified time.

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only tuning jobs that were modified after the specified time.

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only tuning jobs that were modified before the specified time.

    :type StatusEquals: string
    :param StatusEquals: A filter that returns only tuning jobs with the specified status.

    :rtype: dict
    :return: {
        'HyperParameterTuningJobSummaries': [
            {
                'HyperParameterTuningJobName': 'string',
                'HyperParameterTuningJobArn': 'string',
                'HyperParameterTuningJobStatus': 'Completed'|'InProgress'|'Failed'|'Stopped'|'Stopping',
                'Strategy': 'Bayesian',
                'CreationTime': datetime(2015, 1, 1),
                'HyperParameterTuningEndTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'TrainingJobStatusCounters': {
                    'Completed': 123,
                    'InProgress': 123,
                    'RetryableError': 123,
                    'NonRetryableError': 123,
                    'Stopped': 123
                },
                'ObjectiveStatusCounters': {
                    'Succeeded': 123,
                    'Pending': 123,
                    'Failed': 123
                },
                'ResourceLimits': {
                    'MaxNumberOfTrainingJobs': 123,
                    'MaxParallelTrainingJobs': 123
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_labeling_jobs(CreationTimeAfter=None, CreationTimeBefore=None, LastModifiedTimeAfter=None, LastModifiedTimeBefore=None, MaxResults=None, NextToken=None, NameContains=None, SortBy=None, SortOrder=None, StatusEquals=None):
    """
    Gets a list of labeling jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.list_labeling_jobs(
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        MaxResults=123,
        NextToken='string',
        NameContains='string',
        SortBy='Name'|'CreationTime'|'Status',
        SortOrder='Ascending'|'Descending',
        StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped'
    )
    
    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only labeling jobs created after the specified time (timestamp).

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only labeling jobs created before the specified time (timestamp).

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only labeling jobs modified after the specified time (timestamp).

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only labeling jobs modified before the specified time (timestamp).

    :type MaxResults: integer
    :param MaxResults: The maximum number of labeling jobs to return in each page of the response.

    :type NextToken: string
    :param NextToken: If the result of the previous ListLabelingJobs request was truncated, the response includes a NextToken . To retrieve the next set of labeling jobs, use the token in the next request.

    :type NameContains: string
    :param NameContains: A string in the labeling job name. This filter returns only labeling jobs whose name contains the specified string.

    :type SortBy: string
    :param SortBy: The field to sort results by. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :type StatusEquals: string
    :param StatusEquals: A filter that retrieves only labeling jobs with a specific status.

    :rtype: dict
    :return: {
        'LabelingJobSummaryList': [
            {
                'LabelingJobName': 'string',
                'LabelingJobArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'LabelingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                'LabelCounters': {
                    'TotalLabeled': 123,
                    'HumanLabeled': 123,
                    'MachineLabeled': 123,
                    'FailedNonRetryableError': 123,
                    'Unlabeled': 123
                },
                'WorkteamArn': 'string',
                'PreHumanTaskLambdaArn': 'string',
                'AnnotationConsolidationLambdaArn': 'string',
                'FailureReason': 'string',
                'LabelingJobOutput': {
                    'OutputDatasetS3Uri': 'string',
                    'FinalActiveLearningModelArn': 'string'
                },
                'InputConfig': {
                    'DataSource': {
                        'S3DataSource': {
                            'ManifestS3Uri': 'string'
                        }
                    },
                    'DataAttributes': {
                        'ContentClassifiers': [
                            'FreeOfPersonallyIdentifiableInformation'|'FreeOfAdultContent',
                        ]
                    }
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_labeling_jobs_for_workteam(WorkteamArn=None, MaxResults=None, NextToken=None, CreationTimeAfter=None, CreationTimeBefore=None, JobReferenceCodeContains=None, SortBy=None, SortOrder=None):
    """
    Gets a list of labeling jobs assigned to a specified work team.
    See also: AWS API Documentation
    
    
    :example: response = client.list_labeling_jobs_for_workteam(
        WorkteamArn='string',
        MaxResults=123,
        NextToken='string',
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        JobReferenceCodeContains='string',
        SortBy='CreationTime',
        SortOrder='Ascending'|'Descending'
    )
    
    
    :type WorkteamArn: string
    :param WorkteamArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the work team for which you want to see labeling jobs for.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of labeling jobs to return in each page of the response.

    :type NextToken: string
    :param NextToken: If the result of the previous ListLabelingJobsForWorkteam request was truncated, the response includes a NextToken . To retrieve the next set of labeling jobs, use the token in the next request.

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only labeling jobs created after the specified time (timestamp).

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only labeling jobs created before the specified time (timestamp).

    :type JobReferenceCodeContains: string
    :param JobReferenceCodeContains: A filter the limits jobs to only the ones whose job reference code contains the specified string.

    :type SortBy: string
    :param SortBy: The field to sort results by. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :rtype: dict
    :return: {
        'LabelingJobSummaryList': [
            {
                'LabelingJobName': 'string',
                'JobReferenceCode': 'string',
                'WorkRequesterAccountId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LabelCounters': {
                    'HumanLabeled': 123,
                    'PendingHuman': 123,
                    'Total': 123
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_model_packages(CreationTimeAfter=None, CreationTimeBefore=None, MaxResults=None, NameContains=None, NextToken=None, SortBy=None, SortOrder=None):
    """
    Lists the model packages that have been created.
    See also: AWS API Documentation
    
    
    :example: response = client.list_model_packages(
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        MaxResults=123,
        NameContains='string',
        NextToken='string',
        SortBy='Name'|'CreationTime',
        SortOrder='Ascending'|'Descending'
    )
    
    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only model packages created after the specified time (timestamp).

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only model packages created before the specified time (timestamp).

    :type MaxResults: integer
    :param MaxResults: The maximum number of model packages to return in the response.

    :type NameContains: string
    :param NameContains: A string in the model package name. This filter returns only model packages whose name contains the specified string.

    :type NextToken: string
    :param NextToken: If the response to a previous ListModelPackages request was truncated, the response includes a NextToken . To retrieve the next set of model packages, use the token in the next request.

    :type SortBy: string
    :param SortBy: The parameter by which to sort the results. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for the results. The default is Ascending .

    :rtype: dict
    :return: {
        'ModelPackageSummaryList': [
            {
                'ModelPackageName': 'string',
                'ModelPackageArn': 'string',
                'ModelPackageDescription': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'ModelPackageStatus': 'Pending'|'InProgress'|'Completed'|'Failed'|'Deleting'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_models(SortBy=None, SortOrder=None, NextToken=None, MaxResults=None, NameContains=None, CreationTimeBefore=None, CreationTimeAfter=None):
    """
    Lists models created with the CreateModel API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_models(
        SortBy='Name'|'CreationTime',
        SortOrder='Ascending'|'Descending',
        NextToken='string',
        MaxResults=123,
        NameContains='string',
        CreationTimeBefore=datetime(2015, 1, 1),
        CreationTimeAfter=datetime(2015, 1, 1)
    )
    
    
    :type SortBy: string
    :param SortBy: Sorts the list of results. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :type NextToken: string
    :param NextToken: If the response to a previous ListModels request was truncated, the response includes a NextToken . To retrieve the next set of models, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of models to return in the response.

    :type NameContains: string
    :param NameContains: A string in the training job name. This filter returns only models in the training job whose name contains the specified string.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only models created before the specified time (timestamp).

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only models created after the specified time (timestamp).

    :rtype: dict
    :return: {
        'Models': [
            {
                'ModelName': 'string',
                'ModelArn': 'string',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_notebook_instance_lifecycle_configs(NextToken=None, MaxResults=None, SortBy=None, SortOrder=None, NameContains=None, CreationTimeBefore=None, CreationTimeAfter=None, LastModifiedTimeBefore=None, LastModifiedTimeAfter=None):
    """
    Lists notebook instance lifestyle configurations created with the  CreateNotebookInstanceLifecycleConfig API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_notebook_instance_lifecycle_configs(
        NextToken='string',
        MaxResults=123,
        SortBy='Name'|'CreationTime'|'LastModifiedTime',
        SortOrder='Ascending'|'Descending',
        NameContains='string',
        CreationTimeBefore=datetime(2015, 1, 1),
        CreationTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1)
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of a ListNotebookInstanceLifecycleConfigs request was truncated, the response includes a NextToken . To get the next set of lifecycle configurations, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of lifecycle configurations to return in the response.

    :type SortBy: string
    :param SortBy: Sorts the list of results. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results.

    :type NameContains: string
    :param NameContains: A string in the lifecycle configuration name. This filter returns only lifecycle configurations whose name contains the specified string.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only lifecycle configurations that were created before the specified time (timestamp).

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only lifecycle configurations that were created after the specified time (timestamp).

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only lifecycle configurations that were modified before the specified time (timestamp).

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only lifecycle configurations that were modified after the specified time (timestamp).

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'NotebookInstanceLifecycleConfigs': [
            {
                'NotebookInstanceLifecycleConfigName': 'string',
                'NotebookInstanceLifecycleConfigArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def list_notebook_instances(NextToken=None, MaxResults=None, SortBy=None, SortOrder=None, NameContains=None, CreationTimeBefore=None, CreationTimeAfter=None, LastModifiedTimeBefore=None, LastModifiedTimeAfter=None, StatusEquals=None, NotebookInstanceLifecycleConfigNameContains=None, DefaultCodeRepositoryContains=None, AdditionalCodeRepositoryEquals=None):
    """
    Returns a list of the Amazon SageMaker notebook instances in the requester's account in an AWS Region.
    See also: AWS API Documentation
    
    
    :example: response = client.list_notebook_instances(
        NextToken='string',
        MaxResults=123,
        SortBy='Name'|'CreationTime'|'Status',
        SortOrder='Ascending'|'Descending',
        NameContains='string',
        CreationTimeBefore=datetime(2015, 1, 1),
        CreationTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        StatusEquals='Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting'|'Updating',
        NotebookInstanceLifecycleConfigNameContains='string',
        DefaultCodeRepositoryContains='string',
        AdditionalCodeRepositoryEquals='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If the previous call to the ListNotebookInstances is truncated, the response includes a NextToken . You can use this token in your subsequent ListNotebookInstances request to fetch the next set of notebook instances.
            Note
            You might specify a filter or a sort order in your request. When response is truncated, you must use the same values for the filer and sort order in the next request.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of notebook instances to return.

    :type SortBy: string
    :param SortBy: The field to sort results by. The default is Name .

    :type SortOrder: string
    :param SortOrder: The sort order for results.

    :type NameContains: string
    :param NameContains: A string in the notebook instances' name. This filter returns only notebook instances whose name contains the specified string.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only notebook instances that were created before the specified time (timestamp).

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only notebook instances that were created after the specified time (timestamp).

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only notebook instances that were modified before the specified time (timestamp).

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only notebook instances that were modified after the specified time (timestamp).

    :type StatusEquals: string
    :param StatusEquals: A filter that returns only notebook instances with the specified status.

    :type NotebookInstanceLifecycleConfigNameContains: string
    :param NotebookInstanceLifecycleConfigNameContains: A string in the name of a notebook instances lifecycle configuration associated with this notebook instance. This filter returns only notebook instances associated with a lifecycle configuration with a name that contains the specified string.

    :type DefaultCodeRepositoryContains: string
    :param DefaultCodeRepositoryContains: A string in the name or URL of a git repository associated with this notebook instance. This filter returns only notebook instances associated with a git repository with a name that contains the specified string.

    :type AdditionalCodeRepositoryEquals: string
    :param AdditionalCodeRepositoryEquals: A filter that returns only notebook instances with associated with the specified git respository.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'NotebookInstances': [
            {
                'NotebookInstanceName': 'string',
                'NotebookInstanceArn': 'string',
                'NotebookInstanceStatus': 'Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting'|'Updating',
                'Url': 'string',
                'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.t3.medium'|'ml.t3.large'|'ml.t3.xlarge'|'ml.t3.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.c5d.xlarge'|'ml.c5d.2xlarge'|'ml.c5d.4xlarge'|'ml.c5d.9xlarge'|'ml.c5d.18xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'NotebookInstanceLifecycleConfigName': 'string',
                'DefaultCodeRepository': 'string',
                'AdditionalCodeRepositories': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_subscribed_workteams(NameContains=None, NextToken=None, MaxResults=None):
    """
    Gets a list of the work teams that you are subscribed to in the AWS Marketplace. The list may be empty if no work team satisfies the filter specified in the NameContains parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.list_subscribed_workteams(
        NameContains='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NameContains: string
    :param NameContains: A string in the work team name. This filter returns only work teams whose name contains the specified string.

    :type NextToken: string
    :param NextToken: If the result of the previous ListSubscribedWorkteams request was truncated, the response includes a NextToken . To retrieve the next set of labeling jobs, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of work teams to return in each page of the response.

    :rtype: dict
    :return: {
        'SubscribedWorkteams': [
            {
                'WorkteamArn': 'string',
                'MarketplaceTitle': 'string',
                'SellerName': 'string',
                'MarketplaceDescription': 'string',
                'ListingId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_tags(ResourceArn=None, NextToken=None, MaxResults=None):
    """
    Returns the tags for the specified Amazon SageMaker resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags(
        ResourceArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.
            

    :type NextToken: string
    :param NextToken: If the response to the previous ListTags request is truncated, Amazon SageMaker returns this token. To retrieve the next set of tags, use it in the subsequent request.

    :type MaxResults: integer
    :param MaxResults: Maximum number of tags to return.

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

def list_training_jobs(NextToken=None, MaxResults=None, CreationTimeAfter=None, CreationTimeBefore=None, LastModifiedTimeAfter=None, LastModifiedTimeBefore=None, NameContains=None, StatusEquals=None, SortBy=None, SortOrder=None):
    """
    Lists training jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.list_training_jobs(
        NextToken='string',
        MaxResults=123,
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        NameContains='string',
        StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
        SortBy='Name'|'CreationTime'|'Status',
        SortOrder='Ascending'|'Descending'
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of the previous ListTrainingJobs request was truncated, the response includes a NextToken . To retrieve the next set of training jobs, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of training jobs to return in the response.

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only training jobs created after the specified time (timestamp).

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only training jobs created before the specified time (timestamp).

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only training jobs modified after the specified time (timestamp).

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only training jobs modified before the specified time (timestamp).

    :type NameContains: string
    :param NameContains: A string in the training job name. This filter returns only training jobs whose name contains the specified string.

    :type StatusEquals: string
    :param StatusEquals: A filter that retrieves only training jobs with a specific status.

    :type SortBy: string
    :param SortBy: The field to sort results by. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :rtype: dict
    :return: {
        'TrainingJobSummaries': [
            {
                'TrainingJobName': 'string',
                'TrainingJobArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TrainingEndTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_training_jobs_for_hyper_parameter_tuning_job(HyperParameterTuningJobName=None, NextToken=None, MaxResults=None, StatusEquals=None, SortBy=None, SortOrder=None):
    """
    Gets a list of  TrainingJobSummary objects that describe the training jobs that a hyperparameter tuning job launched.
    See also: AWS API Documentation
    
    
    :example: response = client.list_training_jobs_for_hyper_parameter_tuning_job(
        HyperParameterTuningJobName='string',
        NextToken='string',
        MaxResults=123,
        StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
        SortBy='Name'|'CreationTime'|'Status'|'FinalObjectiveMetricValue',
        SortOrder='Ascending'|'Descending'
    )
    
    
    :type HyperParameterTuningJobName: string
    :param HyperParameterTuningJobName: [REQUIRED]
            The name of the tuning job whose training jobs you want to list.
            

    :type NextToken: string
    :param NextToken: If the result of the previous ListTrainingJobsForHyperParameterTuningJob request was truncated, the response includes a NextToken . To retrieve the next set of training jobs, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of training jobs to return. The default value is 10.

    :type StatusEquals: string
    :param StatusEquals: A filter that returns only training jobs with the specified status.

    :type SortBy: string
    :param SortBy: The field to sort results by. The default is Name .
            If the value of this field is FinalObjectiveMetricValue , any training jobs that did not return an objective metric are not listed.
            

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :rtype: dict
    :return: {
        'TrainingJobSummaries': [
            {
                'TrainingJobName': 'string',
                'TrainingJobArn': 'string',
                'TuningJobName': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TrainingStartTime': datetime(2015, 1, 1),
                'TrainingEndTime': datetime(2015, 1, 1),
                'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                'TunedHyperParameters': {
                    'string': 'string'
                },
                'FailureReason': 'string',
                'FinalHyperParameterTuningJobObjectiveMetric': {
                    'Type': 'Maximize'|'Minimize',
                    'MetricName': 'string',
                    'Value': ...
                },
                'ObjectiveStatus': 'Succeeded'|'Pending'|'Failed'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_transform_jobs(CreationTimeAfter=None, CreationTimeBefore=None, LastModifiedTimeAfter=None, LastModifiedTimeBefore=None, NameContains=None, StatusEquals=None, SortBy=None, SortOrder=None, NextToken=None, MaxResults=None):
    """
    Lists transform jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.list_transform_jobs(
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        NameContains='string',
        StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
        SortBy='Name'|'CreationTime'|'Status',
        SortOrder='Ascending'|'Descending',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only transform jobs created after the specified time.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only transform jobs created before the specified time.

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only transform jobs modified after the specified time.

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only transform jobs modified before the specified time.

    :type NameContains: string
    :param NameContains: A string in the transform job name. This filter returns only transform jobs whose name contains the specified string.

    :type StatusEquals: string
    :param StatusEquals: A filter that retrieves only transform jobs with a specific status.

    :type SortBy: string
    :param SortBy: The field to sort results by. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Descending .

    :type NextToken: string
    :param NextToken: If the result of the previous ListTransformJobs request was truncated, the response includes a NextToken . To retrieve the next set of transform jobs, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of transform jobs to return in the response. The default value is 10 .

    :rtype: dict
    :return: {
        'TransformJobSummaries': [
            {
                'TransformJobName': 'string',
                'TransformJobArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TransformEndTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'TransformJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                'FailureReason': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_workteams(SortBy=None, SortOrder=None, NameContains=None, NextToken=None, MaxResults=None):
    """
    Gets a list of work teams that you have defined in a region. The list may be empty if no work team satisfies the filter specified in the NameContains parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.list_workteams(
        SortBy='Name'|'CreateDate',
        SortOrder='Ascending'|'Descending',
        NameContains='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SortBy: string
    :param SortBy: The field to sort results by. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :type NameContains: string
    :param NameContains: A string in the work team's name. This filter returns only work teams whose name contains the specified string.

    :type NextToken: string
    :param NextToken: If the result of the previous ListWorkteams request was truncated, the response includes a NextToken . To retrieve the next set of labeling jobs, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of work teams to return in each page of the response.

    :rtype: dict
    :return: {
        'Workteams': [
            {
                'WorkteamName': 'string',
                'MemberDefinitions': [
                    {
                        'CognitoMemberDefinition': {
                            'UserPool': 'string',
                            'UserGroup': 'string',
                            'ClientId': 'string'
                        }
                    },
                ],
                'WorkteamArn': 'string',
                'ProductListingIds': [
                    'string',
                ],
                'Description': 'string',
                'SubDomain': 'string',
                'CreateDate': datetime(2015, 1, 1),
                'LastUpdatedDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def render_ui_template(UiTemplate=None, Task=None, RoleArn=None):
    """
    Renders the UI template so that you can preview the worker's experience.
    See also: AWS API Documentation
    
    
    :example: response = client.render_ui_template(
        UiTemplate={
            'Content': 'string'
        },
        Task={
            'Input': 'string'
        },
        RoleArn='string'
    )
    
    
    :type UiTemplate: dict
    :param UiTemplate: [REQUIRED]
            A Template object containing the worker UI template to render.
            Content (string) -- [REQUIRED]The content of the Liquid template for the worker user interface.
            

    :type Task: dict
    :param Task: [REQUIRED]
            A RenderableTask object containing a representative task to render.
            Input (string) -- [REQUIRED]A JSON object that contains values for the variables defined in the template. It is made available to the template under the substitution variable task.input . For example, if you define a variable task.input.text in your template, you can supply the variable in the JSON object as 'text': 'sample text' .
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) that has access to the S3 objects that are used by the template.
            

    :rtype: dict
    :return: {
        'RenderedContent': 'string',
        'Errors': [
            {
                'Code': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    """
    pass

def search(Resource=None, SearchExpression=None, SortBy=None, SortOrder=None, NextToken=None, MaxResults=None):
    """
    Finds Amazon SageMaker resources that match a search query. Matching resource objects are returned as a list of SearchResult objects in the response. You can sort the search results by any resource property in a ascending or descending order.
    You can query against the following value types: numerical, text, Booleans, and timestamps.
    See also: AWS API Documentation
    
    
    :example: response = client.search(
        Resource='TrainingJob',
        SearchExpression={
            'Filters': [
                {
                    'Name': 'string',
                    'Operator': 'Equals'|'NotEquals'|'GreaterThan'|'GreaterThanOrEqualTo'|'LessThan'|'LessThanOrEqualTo'|'Contains',
                    'Value': 'string'
                },
            ],
            'NestedFilters': [
                {
                    'NestedPropertyName': 'string',
                    'Filters': [
                        {
                            'Name': 'string',
                            'Operator': 'Equals'|'NotEquals'|'GreaterThan'|'GreaterThanOrEqualTo'|'LessThan'|'LessThanOrEqualTo'|'Contains',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'SubExpressions': [
                {'... recursive ...'},
            ],
            'Operator': 'And'|'Or'
        },
        SortBy='string',
        SortOrder='Ascending'|'Descending',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]
            The name of the Amazon SageMaker resource to search for. Currently, the only valid Resource value is TrainingJob .
            

    :type SearchExpression: dict
    :param SearchExpression: A Boolean conditional statement. Resource objects must satisfy this condition to be included in search results. You must provide at least one subexpression, filter, or nested filter. The maximum number of recursive SubExpressions , NestedFilters , and Filters that can be included in a SearchExpression object is 50.
            Filters (list) --A list of filter objects.
            (dict) --A conditional statement for a search expression that includes a Boolean operator, a resource property, and a value.
            If you don't specify an Operator and a Value , the filter searches for only the specified property. For example, defining a Filter for the FailureReason for the TrainingJob Resource searches for training job objects that have a value in the FailureReason field.
            If you specify a Value , but not an Operator , Amazon SageMaker uses the equals operator as the default.
            In search, there are several property types:
            Metrics
            To define a metric filter, enter a value using the form 'Metrics.<name>' , where <name> is a metric name. For example, the following filter searches for training jobs with an 'accuracy' metric greater than '0.9' :
            {'Name': 'Metrics.accuracy',
            'Operator': 'GREATER_THAN',
            'Value': '0.9'
            }
            HyperParameters
            To define a hyperparameter filter, enter a value with the form 'HyperParameters.<name>' . Decimal hyperparameter values are treated as a decimal in a comparison if the specified Value is also a decimal value. If the specified Value is an integer, the decimal hyperparameter values are treated as integers. For example, the following filter is satisfied by training jobs with a 'learning_rate' hyperparameter that is less than '0.5' :
            {'Name': 'HyperParameters.learning_rate',
            'Operator': 'LESS_THAN',
            'Value': '0.5'
            }
            Tags
            To define a tag filter, enter a value with the form 'Tags.<key>' .
            Name (string) -- [REQUIRED]A property name. For example, TrainingJobName . For the list of valid property names returned in a search result for each supported resource, see TrainingJob properties. You must specify a valid property name for the resource.
            Operator (string) --A Boolean binary operator that is used to evaluate the filter. The operator field contains one of the following values:
            Equals
            The specified resource in Name equals the specified Value .
            NotEquals
            The specified resource in Name does not equal the specified Value .
            GreaterThan
            The specified resource in Name is greater than the specified Value . Not supported for text-based properties.
            GreaterThanOrEqualTo
            The specified resource in Name is greater than or equal to the specified Value . Not supported for text-based properties.
            LessThan
            The specified resource in Name is less than the specified Value . Not supported for text-based properties.
            LessThanOrEqualTo
            The specified resource in Name is less than or equal to the specified Value . Not supported for text-based properties.
            Contains
            Only supported for text-based properties. The word-list of the property contains the specified Value .
            If you have specified a filter Value , the default is Equals .
            Value (string) --A value used with Resource and Operator to determine if objects satisfy the filter's condition. For numerical properties, Value must be an integer or floating-point decimal. For timestamp properties, Value must be an ISO 8601 date-time string of the following format: YYYY-mm-dd'T'HH:MM:SS .
            
            NestedFilters (list) --A list of nested filter objects.
            (dict) --Defines a list of NestedFilter objects. To satisfy the conditions specified in the NestedFilters call, a resource must satisfy the conditions of all of the filters.
            For example, a NestedFilters could be defined using the training job's InputDataConfig property, this would be defined as a list of Channel objects.
            A NestedFilters object contains multiple filters. For example, to find all training jobs whose name contains train and that have cat/data in their S3Uri (specified in InputDataConfig ), you need to create a NestedFilters object that specifies the InputDataConfig property with the following Filter objects:
            '{Name:'InputDataConfig.ChannelName', 'Operator':'EQUALS', 'Value':'train'}',
            '{Name:'InputDataConfig.DataSource.S3DataSource.S3Uri', 'Operator':'CONTAINS', 'Value':'cat/data'}'
            NestedPropertyName (string) -- [REQUIRED]The name of the property to use in the nested filters. The value must match a listed property name, such as InputDataConfig .
            Filters (list) -- [REQUIRED]A list of filters. Each filter acts on a property. Filters must contain at least one Filters value. For example, a NestedFilters call might include a filter on the PropertyName parameter of the InputDataConfig property: InputDataConfig.DataSource.S3DataSource.S3Uri .
            (dict) --A conditional statement for a search expression that includes a Boolean operator, a resource property, and a value.
            If you don't specify an Operator and a Value , the filter searches for only the specified property. For example, defining a Filter for the FailureReason for the TrainingJob Resource searches for training job objects that have a value in the FailureReason field.
            If you specify a Value , but not an Operator , Amazon SageMaker uses the equals operator as the default.
            In search, there are several property types:
            Metrics
            To define a metric filter, enter a value using the form 'Metrics.<name>' , where <name> is a metric name. For example, the following filter searches for training jobs with an 'accuracy' metric greater than '0.9' :
            {'Name': 'Metrics.accuracy',
            'Operator': 'GREATER_THAN',
            'Value': '0.9'
            }
            HyperParameters
            To define a hyperparameter filter, enter a value with the form 'HyperParameters.<name>' . Decimal hyperparameter values are treated as a decimal in a comparison if the specified Value is also a decimal value. If the specified Value is an integer, the decimal hyperparameter values are treated as integers. For example, the following filter is satisfied by training jobs with a 'learning_rate' hyperparameter that is less than '0.5' :
            {'Name': 'HyperParameters.learning_rate',
            'Operator': 'LESS_THAN',
            'Value': '0.5'
            }
            Tags
            To define a tag filter, enter a value with the form 'Tags.<key>' .
            Name (string) -- [REQUIRED]A property name. For example, TrainingJobName . For the list of valid property names returned in a search result for each supported resource, see TrainingJob properties. You must specify a valid property name for the resource.
            Operator (string) --A Boolean binary operator that is used to evaluate the filter. The operator field contains one of the following values:
            Equals
            The specified resource in Name equals the specified Value .
            NotEquals
            The specified resource in Name does not equal the specified Value .
            GreaterThan
            The specified resource in Name is greater than the specified Value . Not supported for text-based properties.
            GreaterThanOrEqualTo
            The specified resource in Name is greater than or equal to the specified Value . Not supported for text-based properties.
            LessThan
            The specified resource in Name is less than the specified Value . Not supported for text-based properties.
            LessThanOrEqualTo
            The specified resource in Name is less than or equal to the specified Value . Not supported for text-based properties.
            Contains
            Only supported for text-based properties. The word-list of the property contains the specified Value .
            If you have specified a filter Value , the default is Equals .
            Value (string) --A value used with Resource and Operator to determine if objects satisfy the filter's condition. For numerical properties, Value must be an integer or floating-point decimal. For timestamp properties, Value must be an ISO 8601 date-time string of the following format: YYYY-mm-dd'T'HH:MM:SS .
            
            
            SubExpressions (list) --A list of search expression objects.
            (dict) --A multi-expression that searches for the specified resource or resources in a search. All resource objects that satisfy the expression's condition are included in the search results. You must specify at least one subexpression, filter, or nested filter. A SearchExpression can contain up to twenty elements.
            A SearchExpression contains the following components:
            A list of Filter objects. Each filter defines a simple Boolean expression comprised of a resource property name, Boolean operator, and value.
            A list of NestedFilter objects. Each nested filter defines a list of Boolean expressions using a list of resource properties. A nested filter is satisfied if a single object in the list satisfies all Boolean expressions.
            A list of SearchExpression objects. A search expression object can be nested in a list of search expression objects.
            A Boolean operator: And or Or .
            
            Operator (string) --A Boolean operator used to evaluate the search expression. If you want every conditional statement in all lists to be satisfied for the entire search expression to be true, specify And . If only a single conditional statement needs to be true for the entire search expression to be true, specify Or . The default value is And .
            

    :type SortBy: string
    :param SortBy: The name of the resource property used to sort the SearchResults . The default is LastModifiedTime .

    :type SortOrder: string
    :param SortOrder: How SearchResults are ordered. Valid values are Ascending or Descending . The default is Descending .

    :type NextToken: string
    :param NextToken: If more than MaxResults resource objects match the specified SearchExpression , the SearchResponse includes a NextToken . The NextToken can be passed to the next SearchRequest to continue retrieving results for the specified SearchExpression and Sort parameters.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a SearchResponse .

    :rtype: dict
    :return: {
        'Results': [
            {
                'TrainingJob': {
                    'TrainingJobName': 'string',
                    'TrainingJobArn': 'string',
                    'TuningJobArn': 'string',
                    'LabelingJobArn': 'string',
                    'ModelArtifacts': {
                        'S3ModelArtifacts': 'string'
                    },
                    'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
                    'SecondaryStatus': 'Starting'|'LaunchingMLInstances'|'PreparingTrainingStack'|'Downloading'|'DownloadingTrainingImage'|'Training'|'Uploading'|'Stopping'|'Stopped'|'MaxRuntimeExceeded'|'Completed'|'Failed',
                    'FailureReason': 'string',
                    'HyperParameters': {
                        'string': 'string'
                    },
                    'AlgorithmSpecification': {
                        'TrainingImage': 'string',
                        'AlgorithmName': 'string',
                        'TrainingInputMode': 'Pipe'|'File',
                        'MetricDefinitions': [
                            {
                                'Name': 'string',
                                'Regex': 'string'
                            },
                        ]
                    },
                    'RoleArn': 'string',
                    'InputDataConfig': [
                        {
                            'ChannelName': 'string',
                            'DataSource': {
                                'S3DataSource': {
                                    'S3DataType': 'ManifestFile'|'S3Prefix'|'AugmentedManifestFile',
                                    'S3Uri': 'string',
                                    'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key',
                                    'AttributeNames': [
                                        'string',
                                    ]
                                }
                            },
                            'ContentType': 'string',
                            'CompressionType': 'None'|'Gzip',
                            'RecordWrapperType': 'None'|'RecordIO',
                            'InputMode': 'Pipe'|'File',
                            'ShuffleConfig': {
                                'Seed': 123
                            }
                        },
                    ],
                    'OutputDataConfig': {
                        'KmsKeyId': 'string',
                        'S3OutputPath': 'string'
                    },
                    'ResourceConfig': {
                        'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                        'InstanceCount': 123,
                        'VolumeSizeInGB': 123,
                        'VolumeKmsKeyId': 'string'
                    },
                    'VpcConfig': {
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'Subnets': [
                            'string',
                        ]
                    },
                    'StoppingCondition': {
                        'MaxRuntimeInSeconds': 123
                    },
                    'CreationTime': datetime(2015, 1, 1),
                    'TrainingStartTime': datetime(2015, 1, 1),
                    'TrainingEndTime': datetime(2015, 1, 1),
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'SecondaryStatusTransitions': [
                        {
                            'Status': 'Starting'|'LaunchingMLInstances'|'PreparingTrainingStack'|'Downloading'|'DownloadingTrainingImage'|'Training'|'Uploading'|'Stopping'|'Stopped'|'MaxRuntimeExceeded'|'Completed'|'Failed',
                            'StartTime': datetime(2015, 1, 1),
                            'EndTime': datetime(2015, 1, 1),
                            'StatusMessage': 'string'
                        },
                    ],
                    'FinalMetricDataList': [
                        {
                            'MetricName': 'string',
                            'Value': ...,
                            'Timestamp': datetime(2015, 1, 1)
                        },
                    ],
                    'EnableNetworkIsolation': True|False,
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    InProgress - The training is in progress.
    Completed - The training job has completed.
    Failed - The training job has failed. To see the reason for the failure, see the FailureReason field in the response to a DescribeTrainingJobResponse call.
    Stopping - The training job is stopping.
    Stopped - The training job has stopped.
    
    """
    pass

def start_notebook_instance(NotebookInstanceName=None):
    """
    Launches an ML compute instance with the latest version of the libraries and attaches your ML storage volume. After configuring the notebook instance, Amazon SageMaker sets the notebook instance status to InService . A notebook instance's status must be InService before you can connect to your Jupyter notebook.
    See also: AWS API Documentation
    
    
    :example: response = client.start_notebook_instance(
        NotebookInstanceName='string'
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the notebook instance to start.
            

    """
    pass

def stop_compilation_job(CompilationJobName=None):
    """
    Stops a model compilation job.
    To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal. This gracefully shuts the job down. If the job hasn't stopped, it sends the SIGKILL signal.
    When it receives a StopCompilationJob request, Amazon SageMaker changes the  CompilationJobSummary$CompilationJobStatus of the job to Stopping . After Amazon SageMaker stops the job, it sets the  CompilationJobSummary$CompilationJobStatus to Stopped .
    See also: AWS API Documentation
    
    
    :example: response = client.stop_compilation_job(
        CompilationJobName='string'
    )
    
    
    :type CompilationJobName: string
    :param CompilationJobName: [REQUIRED]
            The name of the model compilation job to stop.
            

    """
    pass

def stop_hyper_parameter_tuning_job(HyperParameterTuningJobName=None):
    """
    Stops a running hyperparameter tuning job and all running training jobs that the tuning job launched.
    All model artifacts output from the training jobs are stored in Amazon Simple Storage Service (Amazon S3). All data that the training jobs write to Amazon CloudWatch Logs are still available in CloudWatch. After the tuning job moves to the Stopped state, it releases all reserved resources for the tuning job.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_hyper_parameter_tuning_job(
        HyperParameterTuningJobName='string'
    )
    
    
    :type HyperParameterTuningJobName: string
    :param HyperParameterTuningJobName: [REQUIRED]
            The name of the tuning job to stop.
            

    """
    pass

def stop_labeling_job(LabelingJobName=None):
    """
    Stops a running labeling job. A job that is stopped cannot be restarted. Any results obtained before the job is stopped are placed in the Amazon S3 output bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_labeling_job(
        LabelingJobName='string'
    )
    
    
    :type LabelingJobName: string
    :param LabelingJobName: [REQUIRED]
            The name of the labeling job to stop.
            

    """
    pass

def stop_notebook_instance(NotebookInstanceName=None):
    """
    Terminates the ML compute instance. Before terminating the instance, Amazon SageMaker disconnects the ML storage volume from it. Amazon SageMaker preserves the ML storage volume.
    To access data on the ML storage volume for a notebook instance that has been terminated, call the StartNotebookInstance API. StartNotebookInstance launches another ML compute instance, configures it, and attaches the preserved ML storage volume so you can continue your work.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_notebook_instance(
        NotebookInstanceName='string'
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the notebook instance to terminate.
            

    """
    pass

def stop_training_job(TrainingJobName=None):
    """
    Stops a training job. To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts, so the results of the training is not lost.
    Training algorithms provided by Amazon SageMaker save the intermediate results of a model training job. This intermediate data is a valid model artifact. You can use the model artifacts that are saved when Amazon SageMaker stops a training job to create a model.
    When it receives a StopTrainingJob request, Amazon SageMaker changes the status of the job to Stopping . After Amazon SageMaker stops the job, it sets the status to Stopped .
    See also: AWS API Documentation
    
    
    :example: response = client.stop_training_job(
        TrainingJobName='string'
    )
    
    
    :type TrainingJobName: string
    :param TrainingJobName: [REQUIRED]
            The name of the training job to stop.
            

    """
    pass

def stop_transform_job(TransformJobName=None):
    """
    Stops a transform job.
    When Amazon SageMaker receives a StopTransformJob request, the status of the job changes to Stopping . After Amazon SageMaker stops the job, the status is set to Stopped . When you stop a transform job before it is completed, Amazon SageMaker doesn't store the job's output in Amazon S3.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_transform_job(
        TransformJobName='string'
    )
    
    
    :type TransformJobName: string
    :param TransformJobName: [REQUIRED]
            The name of the transform job to stop.
            

    """
    pass

def update_code_repository(CodeRepositoryName=None, GitConfig=None):
    """
    Updates the specified git repository with the specified values.
    See also: AWS API Documentation
    
    
    :example: response = client.update_code_repository(
        CodeRepositoryName='string',
        GitConfig={
            'SecretArn': 'string'
        }
    )
    
    
    :type CodeRepositoryName: string
    :param CodeRepositoryName: [REQUIRED]
            The name of the git repository to update.
            

    :type GitConfig: dict
    :param GitConfig: The configuration of the git repository, including the URL and the Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the repository. The secret must have a staging label of AWSCURRENT and must be in the following format:
            {'username': *UserName* , 'password': *Password* }
            SecretArn (string) --The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of AWSCURRENT and must be in the following format:
            {'username': *UserName* , 'password': *Password* }
            

    :rtype: dict
    :return: {
        'CodeRepositoryArn': 'string'
    }
    
    
    """
    pass

def update_endpoint(EndpointName=None, EndpointConfigName=None):
    """
    Deploys the new EndpointConfig specified in the request, switches to using newly created endpoint, and then deletes resources provisioned for the endpoint using the previous EndpointConfig (there is no availability loss).
    When Amazon SageMaker receives the request, it sets the endpoint status to Updating . After updating the endpoint, it sets the status to InService . To check the status of an endpoint, use the DescribeEndpoint API.
    See also: AWS API Documentation
    
    
    :example: response = client.update_endpoint(
        EndpointName='string',
        EndpointConfigName='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of the endpoint whose configuration you want to update.
            

    :type EndpointConfigName: string
    :param EndpointConfigName: [REQUIRED]
            The name of the new endpoint configuration.
            

    :rtype: dict
    :return: {
        'EndpointArn': 'string'
    }
    
    
    """
    pass

def update_endpoint_weights_and_capacities(EndpointName=None, DesiredWeightsAndCapacities=None):
    """
    Updates variant weight of one or more variants associated with an existing endpoint, or capacity of one variant associated with an existing endpoint. When it receives the request, Amazon SageMaker sets the endpoint status to Updating . After updating the endpoint, it sets the status to InService . To check the status of an endpoint, use the DescribeEndpoint API.
    See also: AWS API Documentation
    
    
    :example: response = client.update_endpoint_weights_and_capacities(
        EndpointName='string',
        DesiredWeightsAndCapacities=[
            {
                'VariantName': 'string',
                'DesiredWeight': ...,
                'DesiredInstanceCount': 123
            },
        ]
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of an existing Amazon SageMaker endpoint.
            

    :type DesiredWeightsAndCapacities: list
    :param DesiredWeightsAndCapacities: [REQUIRED]
            An object that provides new capacity and weight values for a variant.
            (dict) --Specifies weight and capacity values for a production variant.
            VariantName (string) -- [REQUIRED]The name of the variant to update.
            DesiredWeight (float) --The variant's weight.
            DesiredInstanceCount (integer) --The variant's capacity.
            
            

    :rtype: dict
    :return: {
        'EndpointArn': 'string'
    }
    
    
    """
    pass

def update_notebook_instance(NotebookInstanceName=None, InstanceType=None, RoleArn=None, LifecycleConfigName=None, DisassociateLifecycleConfig=None, VolumeSizeInGB=None, DefaultCodeRepository=None, AdditionalCodeRepositories=None, AcceleratorTypes=None, DisassociateAcceleratorTypes=None, DisassociateDefaultCodeRepository=None, DisassociateAdditionalCodeRepositories=None):
    """
    Updates a notebook instance. NotebookInstance updates include upgrading or downgrading the ML compute instance used for your notebook instance to accommodate changes in your workload requirements. You can also update the VPC security groups.
    See also: AWS API Documentation
    
    
    :example: response = client.update_notebook_instance(
        NotebookInstanceName='string',
        InstanceType='ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.t3.medium'|'ml.t3.large'|'ml.t3.xlarge'|'ml.t3.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.c5d.xlarge'|'ml.c5d.2xlarge'|'ml.c5d.4xlarge'|'ml.c5d.9xlarge'|'ml.c5d.18xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
        RoleArn='string',
        LifecycleConfigName='string',
        DisassociateLifecycleConfig=True|False,
        VolumeSizeInGB=123,
        DefaultCodeRepository='string',
        AdditionalCodeRepositories=[
            'string',
        ],
        AcceleratorTypes=[
            'ml.eia1.medium'|'ml.eia1.large'|'ml.eia1.xlarge',
        ],
        DisassociateAcceleratorTypes=True|False,
        DisassociateDefaultCodeRepository=True|False,
        DisassociateAdditionalCodeRepositories=True|False
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the notebook instance to update.
            

    :type InstanceType: string
    :param InstanceType: The Amazon ML compute instance type.

    :type RoleArn: string
    :param RoleArn: The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can assume to access the notebook instance. For more information, see Amazon SageMaker Roles .
            Note
            To be able to pass this role to Amazon SageMaker, the caller of this API must have the iam:PassRole permission.
            

    :type LifecycleConfigName: string
    :param LifecycleConfigName: The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see Step 2.1: (Optional) Customize a Notebook Instance .

    :type DisassociateLifecycleConfig: boolean
    :param DisassociateLifecycleConfig: Set to true to remove the notebook instance lifecycle configuration currently associated with the notebook instance.

    :type VolumeSizeInGB: integer
    :param VolumeSizeInGB: The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB.

    :type DefaultCodeRepository: string
    :param DefaultCodeRepository: The git repository to associate with the notebook instance as its default code repository. This can be either the name of a git repository stored as a resource in your account, or the URL of a git repository in AWS CodeCommit or in any other git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see Associating Git Repositories with Amazon SageMaker Notebook Instances .

    :type AdditionalCodeRepositories: list
    :param AdditionalCodeRepositories: An array of up to 3 git repositories to associate with the notebook instance. These can be either the names of git repositories stored as resources in your account, or the URL of git repositories in AWS CodeCommit or in any other git repository.. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see Associating Git Repositories with Amazon SageMaker Notebook Instances .
            (string) --
            

    :type AcceleratorTypes: list
    :param AcceleratorTypes: A list of the Elastic Inference (EI) instance types to associate with this notebook instance. Currently only one EI instance type can be associated with a notebook instance. For more information, see Using Elastic Inference in Amazon SageMaker .
            (string) --
            

    :type DisassociateAcceleratorTypes: boolean
    :param DisassociateAcceleratorTypes: A list of the Elastic Inference (EI) instance types to remove from this notebook instance.

    :type DisassociateDefaultCodeRepository: boolean
    :param DisassociateDefaultCodeRepository: The name or URL of the default git repository to remove from this notebook instance.

    :type DisassociateAdditionalCodeRepositories: boolean
    :param DisassociateAdditionalCodeRepositories: A list of names or URLs of the default git repositories to remove from this notebook instance.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_notebook_instance_lifecycle_config(NotebookInstanceLifecycleConfigName=None, OnCreate=None, OnStart=None):
    """
    Updates a notebook instance lifecycle configuration created with the  CreateNotebookInstanceLifecycleConfig API.
    See also: AWS API Documentation
    
    
    :example: response = client.update_notebook_instance_lifecycle_config(
        NotebookInstanceLifecycleConfigName='string',
        OnCreate=[
            {
                'Content': 'string'
            },
        ],
        OnStart=[
            {
                'Content': 'string'
            },
        ]
    )
    
    
    :type NotebookInstanceLifecycleConfigName: string
    :param NotebookInstanceLifecycleConfigName: [REQUIRED]
            The name of the lifecycle configuration.
            

    :type OnCreate: list
    :param OnCreate: The shell script that runs only once, when you create a notebook instance
            (dict) --Contains the notebook instance lifecycle configuration script.
            Each lifecycle configuration script has a limit of 16384 characters.
            The value of the $PATH environment variable that is available to both scripts is /sbin:bin:/usr/sbin:/usr/bin .
            View CloudWatch Logs for notebook instance lifecycle configurations in log group /aws/sagemaker/NotebookInstances in log stream [notebook-instance-name]/[LifecycleConfigHook] .
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
            For information about notebook instance lifestyle configurations, see Step 2.1: (Optional) Customize a Notebook Instance .
            Content (string) --A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
            
            

    :type OnStart: list
    :param OnStart: The shell script that runs every time you start a notebook instance, including when you create the notebook instance.
            (dict) --Contains the notebook instance lifecycle configuration script.
            Each lifecycle configuration script has a limit of 16384 characters.
            The value of the $PATH environment variable that is available to both scripts is /sbin:bin:/usr/sbin:/usr/bin .
            View CloudWatch Logs for notebook instance lifecycle configurations in log group /aws/sagemaker/NotebookInstances in log stream [notebook-instance-name]/[LifecycleConfigHook] .
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
            For information about notebook instance lifestyle configurations, see Step 2.1: (Optional) Customize a Notebook Instance .
            Content (string) --A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_workteam(WorkteamName=None, MemberDefinitions=None, Description=None):
    """
    Updates an existing work team with new member definitions or description.
    See also: AWS API Documentation
    
    
    :example: response = client.update_workteam(
        WorkteamName='string',
        MemberDefinitions=[
            {
                'CognitoMemberDefinition': {
                    'UserPool': 'string',
                    'UserGroup': 'string',
                    'ClientId': 'string'
                }
            },
        ],
        Description='string'
    )
    
    
    :type WorkteamName: string
    :param WorkteamName: [REQUIRED]
            The name of the work team to update.
            

    :type MemberDefinitions: list
    :param MemberDefinitions: A list of MemberDefinition objects that contain the updated work team members.
            (dict) --Defines the Amazon Cognito user group that is part of a work team.
            CognitoMemberDefinition (dict) --The Amazon Cognito user group that is part of the work team.
            UserPool (string) -- [REQUIRED]An identifier for a user pool. The user pool must be in the same region as the service that you are calling.
            UserGroup (string) -- [REQUIRED]An identifier for a user group.
            ClientId (string) -- [REQUIRED]An identifier for an application client. You must create the app client ID using Amazon Cognito.
            
            

    :type Description: string
    :param Description: An updated description for the work team.

    :rtype: dict
    :return: {
        'Workteam': {
            'WorkteamName': 'string',
            'MemberDefinitions': [
                {
                    'CognitoMemberDefinition': {
                        'UserPool': 'string',
                        'UserGroup': 'string',
                        'ClientId': 'string'
                    }
                },
            ],
            'WorkteamArn': 'string',
            'ProductListingIds': [
                'string',
            ],
            'Description': 'string',
            'SubDomain': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'LastUpdatedDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

