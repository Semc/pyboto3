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

def batch_check_layer_availability(registryId=None, repositoryName=None, layerDigests=None):
    """
    Check the availability of multiple image layers in a specified registry and repository.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_check_layer_availability(
        registryId='string',
        repositoryName='string',
        layerDigests=[
            'string',
        ]
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the image layers to check. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository that is associated with the image layers to check.
            

    :type layerDigests: list
    :param layerDigests: [REQUIRED]
            The digests of the image layers to check.
            (string) --
            

    :rtype: dict
    :return: {
        'layers': [
            {
                'layerDigest': 'string',
                'layerAvailability': 'AVAILABLE'|'UNAVAILABLE',
                'layerSize': 123,
                'mediaType': 'string'
            },
        ],
        'failures': [
            {
                'layerDigest': 'string',
                'failureCode': 'InvalidLayerDigest'|'MissingLayerDigest',
                'failureReason': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_delete_image(registryId=None, repositoryName=None, imageIds=None):
    """
    Deletes a list of specified images within a specified repository. Images are specified with either imageTag or imageDigest .
    You can remove a tag from an image by specifying the image's tag in your request. When you remove the last tag from an image, the image is deleted from your repository.
    You can completely delete an image (and all of its tags) by specifying the image's digest in your request.
    See also: AWS API Documentation
    
    Examples
    This example deletes images with the tags precise and trusty in a repository called ubuntu in the default registry for an account.
    Expected Output:
    
    :example: response = client.batch_delete_image(
        registryId='string',
        repositoryName='string',
        imageIds=[
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ]
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the image to delete. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The repository that contains the image to delete.
            

    :type imageIds: list
    :param imageIds: [REQUIRED]
            A list of image ID references that correspond to images to delete. The format of the imageIds reference is imageTag=tag or imageDigest=digest .
            (dict) --An object with identifying information for an Amazon ECR image.
            imageDigest (string) --The sha256 digest of the image manifest.
            imageTag (string) --The tag used for the image.
            
            

    :rtype: dict
    :return: {
        'imageIds': [
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ],
        'failures': [
            {
                'imageId': {
                    'imageDigest': 'string',
                    'imageTag': 'string'
                },
                'failureCode': 'InvalidImageDigest'|'InvalidImageTag'|'ImageTagDoesNotMatchDigest'|'ImageNotFound'|'MissingDigestAndTag',
                'failureReason': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_get_image(registryId=None, repositoryName=None, imageIds=None, acceptedMediaTypes=None):
    """
    Gets detailed information for specified images within a specified repository. Images are specified with either imageTag or imageDigest .
    See also: AWS API Documentation
    
    Examples
    This example obtains information for an image with a specified image digest ID from the repository named ubuntu in the current account.
    Expected Output:
    
    :example: response = client.batch_get_image(
        registryId='string',
        repositoryName='string',
        imageIds=[
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ],
        acceptedMediaTypes=[
            'string',
        ]
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The repository that contains the images to describe.
            

    :type imageIds: list
    :param imageIds: [REQUIRED]
            A list of image ID references that correspond to images to describe. The format of the imageIds reference is imageTag=tag or imageDigest=digest .
            (dict) --An object with identifying information for an Amazon ECR image.
            imageDigest (string) --The sha256 digest of the image manifest.
            imageTag (string) --The tag used for the image.
            
            

    :type acceptedMediaTypes: list
    :param acceptedMediaTypes: The accepted media types for the request.
            Valid values: application/vnd.docker.distribution.manifest.v1+json | application/vnd.docker.distribution.manifest.v2+json | application/vnd.oci.image.manifest.v1+json
            (string) --
            

    :rtype: dict
    :return: {
        'images': [
            {
                'registryId': 'string',
                'repositoryName': 'string',
                'imageId': {
                    'imageDigest': 'string',
                    'imageTag': 'string'
                },
                'imageManifest': 'string'
            },
        ],
        'failures': [
            {
                'imageId': {
                    'imageDigest': 'string',
                    'imageTag': 'string'
                },
                'failureCode': 'InvalidImageDigest'|'InvalidImageTag'|'ImageTagDoesNotMatchDigest'|'ImageNotFound'|'MissingDigestAndTag',
                'failureReason': 'string'
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

def complete_layer_upload(registryId=None, repositoryName=None, uploadId=None, layerDigests=None):
    """
    Informs Amazon ECR that the image layer upload has completed for a specified registry, repository name, and upload ID. You can optionally provide a sha256 digest of the image layer for data validation purposes.
    See also: AWS API Documentation
    
    
    :example: response = client.complete_layer_upload(
        registryId='string',
        repositoryName='string',
        uploadId='string',
        layerDigests=[
            'string',
        ]
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry to which to upload layers. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to associate with the image layer.
            

    :type uploadId: string
    :param uploadId: [REQUIRED]
            The upload ID from a previous InitiateLayerUpload operation to associate with the image layer.
            

    :type layerDigests: list
    :param layerDigests: [REQUIRED]
            The sha256 digest of the image layer.
            (string) --
            

    :rtype: dict
    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'uploadId': 'string',
        'layerDigest': 'string'
    }
    
    
    """
    pass

def create_repository(repositoryName=None, tags=None):
    """
    Creates an image repository.
    See also: AWS API Documentation
    
    Examples
    This example creates a repository called nginx-web-app inside the project-a namespace in the default registry for an account.
    Expected Output:
    
    :example: response = client.create_repository(
        repositoryName='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app ) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app ).
            

    :type tags: list
    :param tags: 
            (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            Key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            Value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            
            

    :rtype: dict
    :return: {
        'repository': {
            'repositoryArn': 'string',
            'registryId': 'string',
            'repositoryName': 'string',
            'repositoryUri': 'string',
            'createdAt': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def delete_lifecycle_policy(registryId=None, repositoryName=None):
    """
    Deletes the specified lifecycle policy.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_lifecycle_policy(
        registryId='string',
        repositoryName='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository.
            

    :rtype: dict
    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'lifecyclePolicyText': 'string',
        'lastEvaluatedAt': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def delete_repository(registryId=None, repositoryName=None, force=None):
    """
    Deletes an existing image repository. If a repository contains images, you must use the force option to delete it.
    See also: AWS API Documentation
    
    Examples
    This example force deletes a repository named ubuntu in the default registry for an account. The force parameter is required if the repository contains images.
    Expected Output:
    
    :example: response = client.delete_repository(
        registryId='string',
        repositoryName='string',
        force=True|False
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository to delete. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to delete.
            

    :type force: boolean
    :param force: If a repository contains images, forces the deletion.

    :rtype: dict
    :return: {
        'repository': {
            'repositoryArn': 'string',
            'registryId': 'string',
            'repositoryName': 'string',
            'repositoryUri': 'string',
            'createdAt': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def delete_repository_policy(registryId=None, repositoryName=None):
    """
    Deletes the repository policy from a specified repository.
    See also: AWS API Documentation
    
    Examples
    This example deletes the policy associated with the repository named ubuntu in the current account.
    Expected Output:
    
    :example: response = client.delete_repository_policy(
        registryId='string',
        repositoryName='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository policy to delete. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository that is associated with the repository policy to delete.
            

    :rtype: dict
    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'policyText': 'string'
    }
    
    
    """
    pass

def describe_images(registryId=None, repositoryName=None, imageIds=None, nextToken=None, maxResults=None, filter=None):
    """
    Returns metadata about the images in a repository, including image size, image tags, and creation date.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_images(
        registryId='string',
        repositoryName='string',
        imageIds=[
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ],
        nextToken='string',
        maxResults=123,
        filter={
            'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'
        }
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to describe images. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            A list of repositories to describe.
            

    :type imageIds: list
    :param imageIds: The list of image IDs for the requested repository.
            (dict) --An object with identifying information for an Amazon ECR image.
            imageDigest (string) --The sha256 digest of the image manifest.
            imageTag (string) --The tag used for the image.
            
            

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeImages request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return. This option cannot be used when you specify images with imageIds .

    :type maxResults: integer
    :param maxResults: The maximum number of repository results returned by DescribeImages in paginated output. When this parameter is used, DescribeImages only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeImages request with the returned nextToken value. This value can be between 1 and 1000. If this parameter is not used, then DescribeImages returns up to 100 results and a nextToken value, if applicable. This option cannot be used when you specify images with imageIds .

    :type filter: dict
    :param filter: The filter key and value with which to filter your DescribeImages results.
            tagStatus (string) --The tag status with which to filter your DescribeImages results. You can filter results based on whether they are TAGGED or UNTAGGED .
            

    :rtype: dict
    :return: {
        'imageDetails': [
            {
                'registryId': 'string',
                'repositoryName': 'string',
                'imageDigest': 'string',
                'imageTags': [
                    'string',
                ],
                'imageSizeInBytes': 123,
                'imagePushedAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_repositories(registryId=None, repositoryNames=None, nextToken=None, maxResults=None):
    """
    Describes image repositories in a registry.
    See also: AWS API Documentation
    
    Examples
    The following example obtains a list and description of all repositories in the default registry to which the current user has access.
    Expected Output:
    
    :example: response = client.describe_repositories(
        registryId='string',
        repositoryNames=[
            'string',
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repositories to be described. If you do not specify a registry, the default registry is assumed.

    :type repositoryNames: list
    :param repositoryNames: A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.
            (string) --
            

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeRepositories request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return. This option cannot be used when you specify repositories with repositoryNames .
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of repository results returned by DescribeRepositories in paginated output. When this parameter is used, DescribeRepositories only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeRepositories request with the returned nextToken value. This value can be between 1 and 1000. If this parameter is not used, then DescribeRepositories returns up to 100 results and a nextToken value, if applicable. This option cannot be used when you specify repositories with repositoryNames .

    :rtype: dict
    :return: {
        'repositories': [
            {
                'repositoryArn': 'string',
                'registryId': 'string',
                'repositoryName': 'string',
                'repositoryUri': 'string',
                'createdAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
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

def get_authorization_token(registryIds=None):
    """
    Retrieves a token that is valid for a specified registry for 12 hours. This command allows you to use the docker CLI to push and pull images with Amazon ECR. If you do not specify a registry, the default registry is assumed.
    The authorizationToken returned for each registry specified is a base64 encoded string that can be decoded and used in a docker login command to authenticate to a registry. The AWS CLI offers an aws ecr get-login command that simplifies the login process.
    See also: AWS API Documentation
    
    Examples
    This example gets an authorization token for your default registry.
    Expected Output:
    
    :example: response = client.get_authorization_token(
        registryIds=[
            'string',
        ]
    )
    
    
    :type registryIds: list
    :param registryIds: A list of AWS account IDs that are associated with the registries for which to get authorization tokens. If you do not specify a registry, the default registry is assumed.
            (string) --
            

    :rtype: dict
    :return: {
        'authorizationData': [
            {
                'authorizationToken': 'string',
                'expiresAt': datetime(2015, 1, 1),
                'proxyEndpoint': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_download_url_for_layer(registryId=None, repositoryName=None, layerDigest=None):
    """
    Retrieves the pre-signed Amazon S3 download URL corresponding to an image layer. You can only get URLs for image layers that are referenced in an image.
    See also: AWS API Documentation
    
    
    :example: response = client.get_download_url_for_layer(
        registryId='string',
        repositoryName='string',
        layerDigest='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the image layer to download. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository that is associated with the image layer to download.
            

    :type layerDigest: string
    :param layerDigest: [REQUIRED]
            The digest of the image layer to download.
            

    :rtype: dict
    :return: {
        'downloadUrl': 'string',
        'layerDigest': 'string'
    }
    
    
    """
    pass

def get_lifecycle_policy(registryId=None, repositoryName=None):
    """
    Retrieves the specified lifecycle policy.
    See also: AWS API Documentation
    
    
    :example: response = client.get_lifecycle_policy(
        registryId='string',
        repositoryName='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository.
            

    :rtype: dict
    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'lifecyclePolicyText': 'string',
        'lastEvaluatedAt': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_lifecycle_policy_preview(registryId=None, repositoryName=None, imageIds=None, nextToken=None, maxResults=None, filter=None):
    """
    Retrieves the results of the specified lifecycle policy preview request.
    See also: AWS API Documentation
    
    
    :example: response = client.get_lifecycle_policy_preview(
        registryId='string',
        repositoryName='string',
        imageIds=[
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ],
        nextToken='string',
        maxResults=123,
        filter={
            'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'
        }
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository.
            

    :type imageIds: list
    :param imageIds: The list of imageIDs to be included.
            (dict) --An object with identifying information for an Amazon ECR image.
            imageDigest (string) --The sha256 digest of the image manifest.
            imageTag (string) --The tag used for the image.
            
            

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated GetLifecyclePolicyPreviewRequest request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return. This option cannot be used when you specify images with imageIds .

    :type maxResults: integer
    :param maxResults: The maximum number of repository results returned by GetLifecyclePolicyPreviewRequest in paginated output. When this parameter is used, GetLifecyclePolicyPreviewRequest only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another GetLifecyclePolicyPreviewRequest request with the returned nextToken value. This value can be between 1 and 1000. If this parameter is not used, then GetLifecyclePolicyPreviewRequest returns up to 100 results and a nextToken value, if applicable. This option cannot be used when you specify images with imageIds .

    :type filter: dict
    :param filter: An optional parameter that filters results based on image tag status and all tags, if tagged.
            tagStatus (string) --The tag status of the image.
            

    :rtype: dict
    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'lifecyclePolicyText': 'string',
        'status': 'IN_PROGRESS'|'COMPLETE'|'EXPIRED'|'FAILED',
        'nextToken': 'string',
        'previewResults': [
            {
                'imageTags': [
                    'string',
                ],
                'imageDigest': 'string',
                'imagePushedAt': datetime(2015, 1, 1),
                'action': {
                    'type': 'EXPIRE'
                },
                'appliedRulePriority': 123
            },
        ],
        'summary': {
            'expiringImageTotalCount': 123
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

def get_repository_policy(registryId=None, repositoryName=None):
    """
    Retrieves the repository policy for a specified repository.
    See also: AWS API Documentation
    
    Examples
    This example obtains the repository policy for the repository named ubuntu.
    Expected Output:
    
    :example: response = client.get_repository_policy(
        registryId='string',
        repositoryName='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository with the policy to retrieve.
            

    :rtype: dict
    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'policyText': 'string'
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

def initiate_layer_upload(registryId=None, repositoryName=None):
    """
    Notify Amazon ECR that you intend to upload an image layer.
    See also: AWS API Documentation
    
    
    :example: response = client.initiate_layer_upload(
        registryId='string',
        repositoryName='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry to which you intend to upload layers. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to which you intend to upload layers.
            

    :rtype: dict
    :return: {
        'uploadId': 'string',
        'partSize': 123
    }
    
    
    """
    pass

def list_images(registryId=None, repositoryName=None, nextToken=None, maxResults=None, filter=None):
    """
    Lists all the image IDs for a given repository.
    You can filter images based on whether or not they are tagged by setting the tagStatus parameter to TAGGED or UNTAGGED . For example, you can filter your results to return only UNTAGGED images and then pipe that result to a  BatchDeleteImage operation to delete them. Or, you can filter your results to return only TAGGED images to list all of the tags in your repository.
    See also: AWS API Documentation
    
    Examples
    This example lists all of the images in the repository named ubuntu in the default registry in the current account.
    Expected Output:
    
    :example: response = client.list_images(
        registryId='string',
        repositoryName='string',
        nextToken='string',
        maxResults=123,
        filter={
            'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'
        }
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to list images. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The repository with image IDs to be listed.
            

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListImages request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of image results returned by ListImages in paginated output. When this parameter is used, ListImages only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListImages request with the returned nextToken value. This value can be between 1 and 1000. If this parameter is not used, then ListImages returns up to 100 results and a nextToken value, if applicable.

    :type filter: dict
    :param filter: The filter key and value with which to filter your ListImages results.
            tagStatus (string) --The tag status with which to filter your ListImages results. You can filter results based on whether they are TAGGED or UNTAGGED .
            

    :rtype: dict
    :return: {
        'imageIds': [
            {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    List the tags for an Amazon ECR resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the only supported resource is an Amazon ECR repository.
            

    :rtype: dict
    :return: {
        'tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def put_image(registryId=None, repositoryName=None, imageManifest=None, imageTag=None):
    """
    Creates or updates the image manifest and tags associated with an image.
    See also: AWS API Documentation
    
    
    :example: response = client.put_image(
        registryId='string',
        repositoryName='string',
        imageManifest='string',
        imageTag='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository in which to put the image. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository in which to put the image.
            

    :type imageManifest: string
    :param imageManifest: [REQUIRED]
            The image manifest corresponding to the image to be uploaded.
            

    :type imageTag: string
    :param imageTag: The tag to associate with the image. This parameter is required for images that use the Docker Image Manifest V2 Schema 2 or OCI formats.

    :rtype: dict
    :return: {
        'image': {
            'registryId': 'string',
            'repositoryName': 'string',
            'imageId': {
                'imageDigest': 'string',
                'imageTag': 'string'
            },
            'imageManifest': 'string'
        }
    }
    
    
    """
    pass

def put_lifecycle_policy(registryId=None, repositoryName=None, lifecyclePolicyText=None):
    """
    Creates or updates a lifecycle policy. For information about lifecycle policy syntax, see Lifecycle Policy Template .
    See also: AWS API Documentation
    
    
    :example: response = client.put_lifecycle_policy(
        registryId='string',
        repositoryName='string',
        lifecyclePolicyText='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to receive the policy.
            

    :type lifecyclePolicyText: string
    :param lifecyclePolicyText: [REQUIRED]
            The JSON repository policy text to apply to the repository.
            

    :rtype: dict
    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'lifecyclePolicyText': 'string'
    }
    
    
    """
    pass

def set_repository_policy(registryId=None, repositoryName=None, policyText=None, force=None):
    """
    Applies a repository policy on a specified repository to control access permissions.
    See also: AWS API Documentation
    
    
    :example: response = client.set_repository_policy(
        registryId='string',
        repositoryName='string',
        policyText='string',
        force=True|False
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to receive the policy.
            

    :type policyText: string
    :param policyText: [REQUIRED]
            The JSON repository policy text to apply to the repository.
            

    :type force: boolean
    :param force: If the policy you are attempting to set on a repository policy would prevent you from setting another policy in the future, you must force the SetRepositoryPolicy operation. This is intended to prevent accidental repository lock outs.

    :rtype: dict
    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'policyText': 'string'
    }
    
    
    """
    pass

def start_lifecycle_policy_preview(registryId=None, repositoryName=None, lifecyclePolicyText=None):
    """
    Starts a preview of the specified lifecycle policy. This allows you to see the results before creating the lifecycle policy.
    See also: AWS API Documentation
    
    
    :example: response = client.start_lifecycle_policy_preview(
        registryId='string',
        repositoryName='string',
        lifecyclePolicyText='string'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to be evaluated.
            

    :type lifecyclePolicyText: string
    :param lifecyclePolicyText: The policy to be evaluated against. If you do not specify a policy, the current policy for the repository is used.

    :rtype: dict
    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'lifecyclePolicyText': 'string',
        'status': 'IN_PROGRESS'|'COMPLETE'|'EXPIRED'|'FAILED'
    }
    
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds specified tags to a resource with the specified ARN. Existing tags on a resource are not changed if they are not specified in the request parameters.
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
            The Amazon Resource Name (ARN) of the the resource to which to add tags. Currently, the only supported resource is an Amazon ECR repository.
            

    :type tags: list
    :param tags: [REQUIRED]
            The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            Key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            Value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Deletes specified tags from a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource from which to remove tags. Currently, the only supported resource is an Amazon ECR repository.
            

    :type tagKeys: list
    :param tagKeys: [REQUIRED]
            The keys of the tags to be removed.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def upload_layer_part(registryId=None, repositoryName=None, uploadId=None, partFirstByte=None, partLastByte=None, layerPartBlob=None):
    """
    Uploads an image layer part to Amazon ECR.
    See also: AWS API Documentation
    
    
    :example: response = client.upload_layer_part(
        registryId='string',
        repositoryName='string',
        uploadId='string',
        partFirstByte=123,
        partLastByte=123,
        layerPartBlob=b'bytes'
    )
    
    
    :type registryId: string
    :param registryId: The AWS account ID associated with the registry to which you are uploading layer parts. If you do not specify a registry, the default registry is assumed.

    :type repositoryName: string
    :param repositoryName: [REQUIRED]
            The name of the repository to which you are uploading layer parts.
            

    :type uploadId: string
    :param uploadId: [REQUIRED]
            The upload ID from a previous InitiateLayerUpload operation to associate with the layer part upload.
            

    :type partFirstByte: integer
    :param partFirstByte: [REQUIRED]
            The integer value of the first byte of the layer part.
            

    :type partLastByte: integer
    :param partLastByte: [REQUIRED]
            The integer value of the last byte of the layer part.
            

    :type layerPartBlob: bytes
    :param layerPartBlob: [REQUIRED]
            The base64-encoded layer part payload.
            

    :rtype: dict
    :return: {
        'registryId': 'string',
        'repositoryName': 'string',
        'uploadId': 'string',
        'lastByteReceived': 123
    }
    
    
    """
    pass

