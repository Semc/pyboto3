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

def add_tags_to_certificate(CertificateArn=None, Tags=None):
    """
    Adds one or more tags to an ACM certificate. Tags are labels that you can use to identify and organize your AWS resources. Each tag consists of a key and an optional value . You specify the certificate on input by its Amazon Resource Name (ARN). You specify the tag by using a key-value pair.
    You can apply a tag to just one certificate if you want to identify a specific characteristic of that certificate, or you can apply the same tag to multiple certificates if you want to filter for a common relationship among those certificates. Similarly, you can apply the same tag to multiple resources if you want to specify a relationship among those resources. For example, you can add the same tag to an ACM certificate and an Elastic Load Balancing load balancer to indicate that they are both used by the same website. For more information, see Tagging ACM certificates .
    To remove one or more tags, use the  RemoveTagsFromCertificate action. To view all of the tags that have been applied to the certificate, use the  ListTagsForCertificate action.
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags_to_certificate(\n    CertificateArn='string',\n    Tags=[\n        {\n            'Key': 'string',\n            'Value': 'string'\n        },\n    ]\n)\n\n
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nString that contains the ARN of the ACM certificate to which the tag is to be applied. This must be of the form:\n\narn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe key-value pair that defines the tag. The tag value is optional.\n\n(dict) --A key-value pair that identifies or specifies metadata about an ACM resource.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def delete_certificate(CertificateArn=None):
    """
    Deletes a certificate and its associated private key. If this action succeeds, the certificate no longer appears in the list that can be displayed by calling the  ListCertificates action or be retrieved by calling the  GetCertificate action. The certificate will not be available for use by AWS services integrated with ACM.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_certificate(\n    CertificateArn='string'\n)\n\n
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nString that contains the ARN of the ACM certificate to be deleted. This must be of the form:\n\narn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    """
    pass

def describe_certificate(CertificateArn=None):
    """
    Returns detailed metadata about the specified ACM certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_certificate(\n    CertificateArn='string'\n)\n\n
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the ACM certificate. The ARN must have the following form:\n\narn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    :rtype: dict\nReturnsResponse Syntax{\n    'Certificate': {\n        'CertificateArn': 'string',\n        'DomainName': 'string',\n        'SubjectAlternativeNames': [\n            'string',\n        ],\n        'DomainValidationOptions': [\n            {\n                'DomainName': 'string',\n                'ValidationEmails': [\n                    'string',\n                ],\n                'ValidationDomain': 'string',\n                'ValidationStatus': 'PENDING_VALIDATION'|'SUCCESS'|'FAILED',\n                'ResourceRecord': {\n                    'Name': 'string',\n                    'Type': 'CNAME',\n                    'Value': 'string'\n                },\n                'ValidationMethod': 'EMAIL'|'DNS'\n            },\n        ],\n        'Serial': 'string',\n        'Subject': 'string',\n        'Issuer': 'string',\n        'CreatedAt': datetime(2015, 1, 1),\n        'IssuedAt': datetime(2015, 1, 1),\n        'ImportedAt': datetime(2015, 1, 1),\n        'Status': 'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED',\n        'RevokedAt': datetime(2015, 1, 1),\n        'RevocationReason': 'UNSPECIFIED'|'KEY_COMPROMISE'|'CA_COMPROMISE'|'AFFILIATION_CHANGED'|'SUPERCEDED'|'CESSATION_OF_OPERATION'|'CERTIFICATE_HOLD'|'REMOVE_FROM_CRL'|'PRIVILEGE_WITHDRAWN'|'A_A_COMPROMISE',\n        'NotBefore': datetime(2015, 1, 1),\n        'NotAfter': datetime(2015, 1, 1),\n        'KeyAlgorithm': 'RSA_2048'|'RSA_1024'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1'|'EC_secp521r1',\n        'SignatureAlgorithm': 'string',\n        'InUseBy': [\n            'string',\n        ],\n        'FailureReason': 'NO_AVAILABLE_CONTACTS'|'ADDITIONAL_VERIFICATION_REQUIRED'|'DOMAIN_NOT_ALLOWED'|'INVALID_PUBLIC_DOMAIN'|'CAA_ERROR'|'PCA_LIMIT_EXCEEDED'|'PCA_INVALID_ARN'|'PCA_INVALID_STATE'|'PCA_REQUEST_FAILED'|'PCA_RESOURCE_NOT_FOUND'|'PCA_INVALID_ARGS'|'OTHER',\n        'Type': 'IMPORTED'|'AMAZON_ISSUED'|'PRIVATE',\n        'RenewalSummary': {\n            'RenewalStatus': 'PENDING_AUTO_RENEWAL'|'PENDING_VALIDATION'|'SUCCESS'|'FAILED',\n            'DomainValidationOptions': [\n                {\n                    'DomainName': 'string',\n                    'ValidationEmails': [\n                        'string',\n                    ],\n                    'ValidationDomain': 'string',\n                    'ValidationStatus': 'PENDING_VALIDATION'|'SUCCESS'|'FAILED',\n                    'ResourceRecord': {\n                        'Name': 'string',\n                        'Type': 'CNAME',\n                        'Value': 'string'\n                    },\n                    'ValidationMethod': 'EMAIL'|'DNS'\n                },\n            ]\n        },\n        'KeyUsages': [\n            {\n                'Name': 'DIGITAL_SIGNATURE'|'NON_REPUDIATION'|'KEY_ENCIPHERMENT'|'DATA_ENCIPHERMENT'|'KEY_AGREEMENT'|'CERTIFICATE_SIGNING'|'CRL_SIGNING'|'ENCIPHER_ONLY'|'DECIPHER_ONLY'|'ANY'|'CUSTOM'\n            },\n        ],\n        'ExtendedKeyUsages': [\n            {\n                'Name': 'TLS_WEB_SERVER_AUTHENTICATION'|'TLS_WEB_CLIENT_AUTHENTICATION'|'CODE_SIGNING'|'EMAIL_PROTECTION'|'TIME_STAMPING'|'OCSP_SIGNING'|'IPSEC_END_SYSTEM'|'IPSEC_TUNNEL'|'IPSEC_USER'|'ANY'|'NONE'|'CUSTOM',\n                'OID': 'string'\n            },\n        ],\n        'CertificateAuthorityArn': 'string',\n        'RenewalEligibility': 'ELIGIBLE'|'INELIGIBLE',\n        'Options': {\n            'CertificateTransparencyLoggingPreference': 'ENABLED'|'DISABLED'\n        }\n    }\n}\n\n\nResponse Structure\n\n(dict) --\nCertificate (dict) --Metadata about an ACM certificate.\n\nCertificateArn (string) --The Amazon Resource Name (ARN) of the certificate. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n\nDomainName (string) --The fully qualified domain name for the certificate, such as www.example.com or example.com.\n\nSubjectAlternativeNames (list) --One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.\n\n(string) --\n\n\nDomainValidationOptions (list) --Contains information about the initial validation of each domain name that occurs as a result of the  RequestCertificate request. This field exists only when the certificate type is AMAZON_ISSUED .\n\n(dict) --Contains information about the validation of each domain name in the certificate.\n\nDomainName (string) --A fully qualified domain name (FQDN) in the certificate. For example, www.example.com or example.com .\n\nValidationEmails (list) --A list of email addresses that ACM used to send domain validation emails.\n\n(string) --\n\n\nValidationDomain (string) --The domain name that ACM used to send domain validation emails.\n\nValidationStatus (string) --The validation status of the domain name. This can be one of the following values:\n\nPENDING_VALIDATION\nSUCCESS\nFAILED\n\n\nResourceRecord (dict) --Contains the CNAME record that you add to your DNS database for domain validation. For more information, see Use DNS to Validate Domain Ownership .\n\nName (string) --The name of the DNS record to create in your domain. This is supplied by ACM.\n\nType (string) --The type of DNS record. Currently this can be CNAME .\n\nValue (string) --The value of the CNAME record to add to your DNS database. This is supplied by ACM.\n\n\n\nValidationMethod (string) --Specifies the domain validation method.\n\n\n\n\n\nSerial (string) --The serial number of the certificate.\n\nSubject (string) --The name of the entity that is associated with the public key contained in the certificate.\n\nIssuer (string) --The name of the certificate authority that issued and signed the certificate.\n\nCreatedAt (datetime) --The time at which the certificate was requested. This value exists only when the certificate type is AMAZON_ISSUED .\n\nIssuedAt (datetime) --The time at which the certificate was issued. This value exists only when the certificate type is AMAZON_ISSUED .\n\nImportedAt (datetime) --The date and time at which the certificate was imported. This value exists only when the certificate type is IMPORTED .\n\nStatus (string) --The status of the certificate.\n\nRevokedAt (datetime) --The time at which the certificate was revoked. This value exists only when the certificate status is REVOKED .\n\nRevocationReason (string) --The reason the certificate was revoked. This value exists only when the certificate status is REVOKED .\n\nNotBefore (datetime) --The time before which the certificate is not valid.\n\nNotAfter (datetime) --The time after which the certificate is not valid.\n\nKeyAlgorithm (string) --The algorithm that was used to generate the public-private key pair.\n\nSignatureAlgorithm (string) --The algorithm that was used to sign the certificate.\n\nInUseBy (list) --A list of ARNs for the AWS resources that are using the certificate. A certificate can be used by multiple AWS resources.\n\n(string) --\n\n\nFailureReason (string) --The reason the certificate request failed. This value exists only when the certificate status is FAILED . For more information, see Certificate Request Failed in the AWS Certificate Manager User Guide .\n\nType (string) --The source of the certificate. For certificates provided by ACM, this value is AMAZON_ISSUED . For certificates that you imported with  ImportCertificate , this value is IMPORTED . ACM does not provide managed renewal for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see Importing Certificates in the AWS Certificate Manager User Guide .\n\nRenewalSummary (dict) --Contains information about the status of ACM\'s managed renewal for the certificate. This field exists only when the certificate type is AMAZON_ISSUED .\n\nRenewalStatus (string) --The status of ACM\'s managed renewal of the certificate.\n\nDomainValidationOptions (list) --Contains information about the validation of each domain name in the certificate, as it pertains to ACM\'s managed renewal . This is different from the initial validation that occurs as a result of the  RequestCertificate request. This field exists only when the certificate type is AMAZON_ISSUED .\n\n(dict) --Contains information about the validation of each domain name in the certificate.\n\nDomainName (string) --A fully qualified domain name (FQDN) in the certificate. For example, www.example.com or example.com .\n\nValidationEmails (list) --A list of email addresses that ACM used to send domain validation emails.\n\n(string) --\n\n\nValidationDomain (string) --The domain name that ACM used to send domain validation emails.\n\nValidationStatus (string) --The validation status of the domain name. This can be one of the following values:\n\nPENDING_VALIDATION\nSUCCESS\nFAILED\n\n\nResourceRecord (dict) --Contains the CNAME record that you add to your DNS database for domain validation. For more information, see Use DNS to Validate Domain Ownership .\n\nName (string) --The name of the DNS record to create in your domain. This is supplied by ACM.\n\nType (string) --The type of DNS record. Currently this can be CNAME .\n\nValue (string) --The value of the CNAME record to add to your DNS database. This is supplied by ACM.\n\n\n\nValidationMethod (string) --Specifies the domain validation method.\n\n\n\n\n\n\n\nKeyUsages (list) --A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.\n\n(dict) --The Key Usage X.509 v3 extension defines the purpose of the public key contained in the certificate.\n\nName (string) --A string value that contains a Key Usage extension name.\n\n\n\n\n\nExtendedKeyUsages (list) --Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID).\n\n(dict) --The Extended Key Usage X.509 v3 extension defines one or more purposes for which the public key can be used. This is in addition to or in place of the basic purposes specified by the Key Usage extension.\n\nName (string) --The name of an Extended Key Usage value.\n\nOID (string) --An object identifier (OID) for the extension value. OIDs are strings of numbers separated by periods. The following OIDs are defined in RFC 3280 and RFC 5280.\n\n1.3.6.1.5.5.7.3.1 (TLS_WEB_SERVER_AUTHENTICATION)\n1.3.6.1.5.5.7.3.2 (TLS_WEB_CLIENT_AUTHENTICATION)\n1.3.6.1.5.5.7.3.3 (CODE_SIGNING)\n1.3.6.1.5.5.7.3.4 (EMAIL_PROTECTION)\n1.3.6.1.5.5.7.3.8 (TIME_STAMPING)\n1.3.6.1.5.5.7.3.9 (OCSP_SIGNING)\n1.3.6.1.5.5.7.3.5 (IPSEC_END_SYSTEM)\n1.3.6.1.5.5.7.3.6 (IPSEC_TUNNEL)\n1.3.6.1.5.5.7.3.7 (IPSEC_USER)\n\n\n\n\n\n\nCertificateAuthorityArn (string) --The Amazon Resource Name (ARN) of the ACM PCA private certificate authority (CA) that issued the certificate. This has the following format:\n\narn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012\n\nRenewalEligibility (string) --Specifies whether the certificate is eligible for renewal.\n\nOptions (dict) --Value that specifies whether to add the certificate to a transparency log. Certificate transparency makes it possible to detect SSL certificates that have been mistakenly or maliciously issued. A browser might respond to certificate that has not been logged by showing an error message. The logs are cryptographically secure.\n\nCertificateTransparencyLoggingPreference (string) --You can opt out of certificate transparency logging by specifying the DISABLED option. Opt in by specifying ENABLED .\n\n\n\n\n\n\n\n\n\n\n
    :return: {\n    'Certificate': {\n        'CertificateArn': 'string',\n        'DomainName': 'string',\n        'SubjectAlternativeNames': [\n            'string',\n        ],\n        'DomainValidationOptions': [\n            {\n                'DomainName': 'string',\n                'ValidationEmails': [\n                    'string',\n                ],\n                'ValidationDomain': 'string',\n                'ValidationStatus': 'PENDING_VALIDATION'|'SUCCESS'|'FAILED',\n                'ResourceRecord': {\n                    'Name': 'string',\n                    'Type': 'CNAME',\n                    'Value': 'string'\n                },\n                'ValidationMethod': 'EMAIL'|'DNS'\n            },\n        ],\n        'Serial': 'string',\n        'Subject': 'string',\n        'Issuer': 'string',\n        'CreatedAt': datetime(2015, 1, 1),\n        'IssuedAt': datetime(2015, 1, 1),\n        'ImportedAt': datetime(2015, 1, 1),\n        'Status': 'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED',\n        'RevokedAt': datetime(2015, 1, 1),\n        'RevocationReason': 'UNSPECIFIED'|'KEY_COMPROMISE'|'CA_COMPROMISE'|'AFFILIATION_CHANGED'|'SUPERCEDED'|'CESSATION_OF_OPERATION'|'CERTIFICATE_HOLD'|'REMOVE_FROM_CRL'|'PRIVILEGE_WITHDRAWN'|'A_A_COMPROMISE',\n        'NotBefore': datetime(2015, 1, 1),\n        'NotAfter': datetime(2015, 1, 1),\n        'KeyAlgorithm': 'RSA_2048'|'RSA_1024'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1'|'EC_secp521r1',\n        'SignatureAlgorithm': 'string',\n        'InUseBy': [\n            'string',\n        ],\n        'FailureReason': 'NO_AVAILABLE_CONTACTS'|'ADDITIONAL_VERIFICATION_REQUIRED'|'DOMAIN_NOT_ALLOWED'|'INVALID_PUBLIC_DOMAIN'|'CAA_ERROR'|'PCA_LIMIT_EXCEEDED'|'PCA_INVALID_ARN'|'PCA_INVALID_STATE'|'PCA_REQUEST_FAILED'|'PCA_RESOURCE_NOT_FOUND'|'PCA_INVALID_ARGS'|'OTHER',\n        'Type': 'IMPORTED'|'AMAZON_ISSUED'|'PRIVATE',\n        'RenewalSummary': {\n            'RenewalStatus': 'PENDING_AUTO_RENEWAL'|'PENDING_VALIDATION'|'SUCCESS'|'FAILED',\n            'DomainValidationOptions': [\n                {\n                    'DomainName': 'string',\n                    'ValidationEmails': [\n                        'string',\n                    ],\n                    'ValidationDomain': 'string',\n                    'ValidationStatus': 'PENDING_VALIDATION'|'SUCCESS'|'FAILED',\n                    'ResourceRecord': {\n                        'Name': 'string',\n                        'Type': 'CNAME',\n                        'Value': 'string'\n                    },\n                    'ValidationMethod': 'EMAIL'|'DNS'\n                },\n            ]\n        },\n        'KeyUsages': [\n            {\n                'Name': 'DIGITAL_SIGNATURE'|'NON_REPUDIATION'|'KEY_ENCIPHERMENT'|'DATA_ENCIPHERMENT'|'KEY_AGREEMENT'|'CERTIFICATE_SIGNING'|'CRL_SIGNING'|'ENCIPHER_ONLY'|'DECIPHER_ONLY'|'ANY'|'CUSTOM'\n            },\n        ],\n        'ExtendedKeyUsages': [\n            {\n                'Name': 'TLS_WEB_SERVER_AUTHENTICATION'|'TLS_WEB_CLIENT_AUTHENTICATION'|'CODE_SIGNING'|'EMAIL_PROTECTION'|'TIME_STAMPING'|'OCSP_SIGNING'|'IPSEC_END_SYSTEM'|'IPSEC_TUNNEL'|'IPSEC_USER'|'ANY'|'NONE'|'CUSTOM',\n                'OID': 'string'\n            },\n        ],\n        'CertificateAuthorityArn': 'string',\n        'RenewalEligibility': 'ELIGIBLE'|'INELIGIBLE',\n        'Options': {\n            'CertificateTransparencyLoggingPreference': 'ENABLED'|'DISABLED'\n        }\n    }\n}\n\n
    :returns: \n(string) --\n
    """
    pass

def export_certificate(CertificateArn=None, Passphrase=None):
    """
    Exports a private certificate issued by a private certificate authority (CA) for use anywhere. You can export the certificate, the certificate chain, and the encrypted private key associated with the public key embedded in the certificate. You must store the private key securely. The private key is a 2048 bit RSA key. You must provide a passphrase for the private key when exporting it. You can use the following OpenSSL command to decrypt it later. Provide the passphrase when prompted.
    See also: AWS API Documentation
    
    
    :example: response = client.export_certificate(\n    CertificateArn='string',\n    Passphrase=b'bytes'\n)\n\n
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nAn Amazon Resource Name (ARN) of the issued certificate. This must be of the form:\n\narn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012\n

    :type Passphrase: bytes
    :param Passphrase: [REQUIRED]\nPassphrase to associate with the encrypted exported private key. If you want to later decrypt the private key, you must have the passphrase. You can use the following OpenSSL command to decrypt a private key:\n\nopenssl rsa -in encrypted_key.pem -out decrypted_key.pem\n

    :rtype: dict\n\nReturnsResponse Syntax\n{\n    'Certificate': 'string',\n    'CertificateChain': 'string',\n    'PrivateKey': 'string'\n}\n\n\nResponse Structure\n\n(dict) --\n\nCertificate (string) --\nThe base64 PEM-encoded certificate.\n\nCertificateChain (string) --\nThe base64 PEM-encoded certificate chain. This does not include the certificate that you are exporting.\n\nPrivateKey (string) --\nThe PEM-encoded private key associated with the public key in the certificate.\n\n\n\n\n\n\n\n
    :return: {\n    'Certificate': 'string',\n    'CertificateChain': 'string',\n    'PrivateKey': 'string'\n}\n\n
    """
    pass

def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for

    :type Params: dict
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_certificate(CertificateArn=None):
    """
    Retrieves a certificate specified by an ARN and its certificate chain . The chain is an ordered list of certificates that contains the end entity certificate, intermediate certificates of subordinate CAs, and the root certificate in that order. The certificate and certificate chain are base64 encoded. If you want to decode the certificate to see the individual fields, you can use OpenSSL.
    See also: AWS API Documentation
    
    
    :example: response = client.get_certificate(\n    CertificateArn='string'\n)\n\n
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nString that contains a certificate ARN in the following format:\n\narn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    :rtype: dict\nReturnsResponse Syntax{\n    'Certificate': 'string',\n    'CertificateChain': 'string'\n}\n\n\nResponse Structure\n\n(dict) --\nCertificate (string) --String that contains the ACM certificate represented by the ARN specified at input.\n\nCertificateChain (string) --The certificate chain that contains the root certificate issued by the certificate authority (CA).\n\n\n\n\n\n\n
    :return: {\n    'Certificate': 'string',\n    'CertificateChain': 'string'\n}\n\n
    """
    pass

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}\nReturnsA paginator object.\n\n
    """
    pass

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter\n\n
    """
    pass

def import_certificate(CertificateArn=None, Certificate=None, PrivateKey=None, CertificateChain=None):
    """
    Imports a certificate into AWS Certificate Manager (ACM) to use with services that are integrated with ACM. Note that integrated services allow only certificate types and keys they support to be associated with their resources. Further, their support differs depending on whether the certificate is imported into IAM or into ACM. For more information, see the documentation for each service. For more information about importing certificates into ACM, see Importing Certificates in the AWS Certificate Manager User Guide .
    Note the following guidelines when importing third party certificates:
    This operation returns the Amazon Resource Name (ARN) of the imported certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.import_certificate(\n    CertificateArn='string',\n    Certificate=b'bytes',\n    PrivateKey=b'bytes',\n    CertificateChain=b'bytes'\n)\n\n
    :type CertificateArn: string
    :param CertificateArn: The Amazon Resource Name (ARN) of an imported certificate to replace. To import a new certificate, omit this field.

    :type Certificate: bytes
    :param Certificate: [REQUIRED]\nThe certificate to import.\n

    :type PrivateKey: bytes
    :param PrivateKey: [REQUIRED]\nThe private key that matches the public key in the certificate.\n

    :type CertificateChain: bytes
    :param CertificateChain: The PEM encoded certificate chain.

    :rtype: dict\n\nReturnsResponse Syntax\n{\n    'CertificateArn': 'string'\n}\n\n\nResponse Structure\n\n(dict) --\n\nCertificateArn (string) --\nThe Amazon Resource Name (ARN) of the imported certificate.\n\n\n\n\n\n\n\n
    :return: {\n    'CertificateArn': 'string'\n}\n\n
    :returns: \nCertificateArn (string) -- The Amazon Resource Name (ARN) of an imported certificate to replace. To import a new certificate, omit this field.\nCertificate (bytes) -- [REQUIRED]\nThe certificate to import.\n\nPrivateKey (bytes) -- [REQUIRED]\nThe private key that matches the public key in the certificate.\n\nCertificateChain (bytes) -- The PEM encoded certificate chain.\n
    """
    pass

def list_certificates(CertificateStatuses=None, Includes=None, NextToken=None, MaxItems=None):
    """
    Retrieves a list of certificate ARNs and domain names. You can request that only certificates that match a specific status be listed. You can also filter by specific attributes of the certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.list_certificates(\n    CertificateStatuses=[\n        'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED',\n    ],\n    Includes={\n        'extendedKeyUsage': [\n            'TLS_WEB_SERVER_AUTHENTICATION'|'TLS_WEB_CLIENT_AUTHENTICATION'|'CODE_SIGNING'|'EMAIL_PROTECTION'|'TIME_STAMPING'|'OCSP_SIGNING'|'IPSEC_END_SYSTEM'|'IPSEC_TUNNEL'|'IPSEC_USER'|'ANY'|'NONE'|'CUSTOM',\n        ],\n        'keyUsage': [\n            'DIGITAL_SIGNATURE'|'NON_REPUDIATION'|'KEY_ENCIPHERMENT'|'DATA_ENCIPHERMENT'|'KEY_AGREEMENT'|'CERTIFICATE_SIGNING'|'CRL_SIGNING'|'ENCIPHER_ONLY'|'DECIPHER_ONLY'|'ANY'|'CUSTOM',\n        ],\n        'keyTypes': [\n            'RSA_2048'|'RSA_1024'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1'|'EC_secp521r1',\n        ]\n    },\n    NextToken='string',\n    MaxItems=123\n)\n\n
    :type CertificateStatuses: list
    :param CertificateStatuses: Filter the certificate list by status value.\n\n(string) --\n\n

    :type Includes: dict
    :param Includes: Filter the certificate list. For more information, see the Filters structure.\n\nextendedKeyUsage (list) --Specify one or more ExtendedKeyUsage extension values.\n\n(string) --\n\n\nkeyUsage (list) --Specify one or more KeyUsage extension values.\n\n(string) --\n\n\nkeyTypes (list) --Specify one or more algorithms that can be used to generate key pairs.\n\n(string) --\n\n\n\n

    :type NextToken: string
    :param NextToken: Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of NextToken from the response you just received.

    :type MaxItems: integer
    :param MaxItems: Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the NextToken element is sent in the response. Use this NextToken value in a subsequent request to retrieve additional items.

    :rtype: dict\n\nReturnsResponse Syntax\n{\n    'NextToken': 'string',\n    'CertificateSummaryList': [\n        {\n            'CertificateArn': 'string',\n            'DomainName': 'string'\n        },\n    ]\n}\n\n\nResponse Structure\n\n(dict) --\n\nNextToken (string) --\nWhen the list is truncated, this value is present and contains the value to use for the NextToken parameter in a subsequent pagination request.\n\nCertificateSummaryList (list) --\nA list of ACM certificates.\n\n(dict) --\nThis structure is returned in the response object of  ListCertificates action.\n\nCertificateArn (string) --\nAmazon Resource Name (ARN) of the certificate. This is of the form:\n\narn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012\n\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n\nDomainName (string) --\nFully qualified domain name (FQDN), such as www.example.com or example.com, for the certificate.\n\n\n\n\n\n\n\n\n\n\n\n
    :return: {\n    'NextToken': 'string',\n    'CertificateSummaryList': [\n        {\n            'CertificateArn': 'string',\n            'DomainName': 'string'\n        },\n    ]\n}\n\n
    """
    pass

def list_tags_for_certificate(CertificateArn=None):
    """
    Lists the tags that have been applied to the ACM certificate. Use the certificate\'s Amazon Resource Name (ARN) to specify the certificate. To add a tag to an ACM certificate, use the  AddTagsToCertificate action. To delete a tag, use the  RemoveTagsFromCertificate action.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_certificate(\n    CertificateArn='string'\n)\n\n
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nString that contains the ARN of the ACM certificate for which you want to list the tags. This must have the following form:\n\narn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    :rtype: dict\nReturnsResponse Syntax{\n    'Tags': [\n        {\n            'Key': 'string',\n            'Value': 'string'\n        },\n    ]\n}\n\n\nResponse Structure\n\n(dict) --\nTags (list) --The key-value pairs that define the applied tags.\n\n(dict) --A key-value pair that identifies or specifies metadata about an ACM resource.\n\nKey (string) --The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n\n\n\n\n\n\n
    :return: {\n    'Tags': [\n        {\n            'Key': 'string',\n            'Value': 'string'\n        },\n    ]\n}\n\n
    """
    pass

def remove_tags_from_certificate(CertificateArn=None, Tags=None):
    """
    Remove one or more tags from an ACM certificate. A tag consists of a key-value pair. If you do not specify the value portion of the tag when calling this function, the tag will be removed regardless of value. If you specify a value, the tag is removed only if it is associated with the specified value.
    To add tags to a certificate, use the  AddTagsToCertificate action. To view all of the tags that have been applied to a specific ACM certificate, use the  ListTagsForCertificate action.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags_from_certificate(\n    CertificateArn='string',\n    Tags=[\n        {\n            'Key': 'string',\n            'Value': 'string'\n        },\n    ]\n)\n\n
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nString that contains the ARN of the ACM Certificate with one or more tags that you want to remove. This must be of the form:\n\narn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe key-value pair that defines the tag to remove.\n\n(dict) --A key-value pair that identifies or specifies metadata about an ACM resource.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    """
    pass

def request_certificate(DomainName=None, ValidationMethod=None, SubjectAlternativeNames=None, IdempotencyToken=None, DomainValidationOptions=None, Options=None, CertificateAuthorityArn=None):
    """
    Requests an ACM certificate for use with other AWS services. To request an ACM certificate, you must specify a fully qualified domain name (FQDN) in the DomainName parameter. You can also specify additional FQDNs in the SubjectAlternativeNames parameter.
    If you are requesting a private certificate, domain validation is not required. If you are requesting a public certificate, each domain name that you specify must be validated to verify that you own or control the domain. You can use DNS validation or email validation . We recommend that you use DNS validation. ACM issues public certificates after receiving approval from the domain owner.
    See also: AWS API Documentation
    
    
    :example: response = client.request_certificate(\n    DomainName='string',\n    ValidationMethod='EMAIL'|'DNS',\n    SubjectAlternativeNames=[\n        'string',\n    ],\n    IdempotencyToken='string',\n    DomainValidationOptions=[\n        {\n            'DomainName': 'string',\n            'ValidationDomain': 'string'\n        },\n    ],\n    Options={\n        'CertificateTransparencyLoggingPreference': 'ENABLED'|'DISABLED'\n    },\n    CertificateAuthorityArn='string'\n)\n\n
    :type DomainName: string
    :param DomainName: [REQUIRED]\nFully qualified domain name (FQDN), such as www.example.com, that you want to secure with an ACM certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, *.example.com protects www.example.com, site.example.com, and images.example.com.\nThe first domain name you enter cannot exceed 63 octets, including periods. Each subsequent Subject Alternative Name (SAN), however, can be up to 253 octets in length.\n

    :type ValidationMethod: string
    :param ValidationMethod: The method you want to use if you are requesting a public certificate to validate that you own or control domain. You can validate with DNS or validate with email . We recommend that you use DNS validation.

    :type SubjectAlternativeNames: list
    :param SubjectAlternativeNames: Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate. For example, add the name www.example.net to a certificate for which the DomainName field is www.example.com if users can reach your site by using either name. The maximum number of domain names that you can add to an ACM certificate is 100. However, the initial limit is 10 domain names. If you need more than 10 names, you must request a limit increase. For more information, see Limits .\nThe maximum length of a SAN DNS name is 253 octets. The name is made up of multiple labels separated by periods. No label can be longer than 63 octets. Consider the following examples:\n\n(63 octets).(63 octets).(63 octets).(61 octets) is legal because the total length is 253 octets (63+1+63+1+63+1+61) and no label exceeds 63 octets.\n(64 octets).(63 octets).(63 octets).(61 octets) is not legal because the total length exceeds 253 octets (64+1+63+1+63+1+61) and the first label exceeds 63 octets.\n(63 octets).(63 octets).(63 octets).(62 octets) is not legal because the total length of the DNS name (63+1+63+1+63+1+62) exceeds 253 octets.\n\n\n(string) --\n\n

    :type IdempotencyToken: string
    :param IdempotencyToken: Customer chosen string that can be used to distinguish between calls to RequestCertificate . Idempotency tokens time out after one hour. Therefore, if you call RequestCertificate multiple times with the same idempotency token within one hour, ACM recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, ACM recognizes that you are requesting multiple certificates.

    :type DomainValidationOptions: list
    :param DomainValidationOptions: The domain name that you want ACM to use to send you emails so that you can validate domain ownership.\n\n(dict) --Contains information about the domain names that you want ACM to use to send you emails that enable you to validate domain ownership.\n\nDomainName (string) -- [REQUIRED]A fully qualified domain name (FQDN) in the certificate request.\n\nValidationDomain (string) -- [REQUIRED]The domain name that you want ACM to use to send you validation emails. This domain name is the suffix of the email addresses that you want ACM to use. This must be the same as the DomainName value or a superdomain of the DomainName value. For example, if you request a certificate for testing.example.com , you can specify example.com for this value. In that case, ACM sends domain validation emails to the following five addresses:\n\nadmin@example.com\nadministrator@example.com\nhostmaster@example.com\npostmaster@example.com\nwebmaster@example.com\n\n\n\n\n\n

    :type Options: dict
    :param Options: Currently, you can use this parameter to specify whether to add the certificate to a certificate transparency log. Certificate transparency makes it possible to detect SSL/TLS certificates that have been mistakenly or maliciously issued. Certificates that have not been logged typically produce an error message in a browser. For more information, see Opting Out of Certificate Transparency Logging .\n\nCertificateTransparencyLoggingPreference (string) --You can opt out of certificate transparency logging by specifying the DISABLED option. Opt in by specifying ENABLED .\n\n\n

    :type CertificateAuthorityArn: string
    :param CertificateAuthorityArn: The Amazon Resource Name (ARN) of the private certificate authority (CA) that will be used to issue the certificate. If you do not provide an ARN and you are trying to request a private certificate, ACM will attempt to issue a public certificate. For more information about private CAs, see the AWS Certificate Manager Private Certificate Authority (PCA) user guide. The ARN must have the following form:\n\narn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012\n

    :rtype: dict\n\nReturnsResponse Syntax\n{\n    'CertificateArn': 'string'\n}\n\n\nResponse Structure\n\n(dict) --\n\nCertificateArn (string) --\nString that contains the ARN of the issued certificate. This must be of the form:\n\narn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012\n\n\n\n\n\n\n\n\n
    :return: {\n    'CertificateArn': 'string'\n}\n\n
    """
    pass

def resend_validation_email(CertificateArn=None, Domain=None, ValidationDomain=None):
    """
    Resends the email that requests domain ownership validation. The domain owner or an authorized representative must approve the ACM certificate before it can be issued. The certificate can be approved by clicking a link in the mail to navigate to the Amazon certificate approval website and then clicking I Approve . However, the validation email can be blocked by spam filters. Therefore, if you do not receive the original mail, you can request that the mail be resent within 72 hours of requesting the ACM certificate. If more than 72 hours have elapsed since your original request or since your last attempt to resend validation mail, you must request a new certificate. For more information about setting up your contact email addresses, see Configure Email for your Domain .
    See also: AWS API Documentation
    
    
    :example: response = client.resend_validation_email(\n    CertificateArn='string',\n    Domain='string',\n    ValidationDomain='string'\n)\n\n
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nString that contains the ARN of the requested certificate. The certificate ARN is generated and returned by the RequestCertificate action as soon as the request is made. By default, using this parameter causes email to be sent to all top-level domains you specified in the certificate request. The ARN must be of the form:\n\narn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012\n

    :type Domain: string
    :param Domain: [REQUIRED]\nThe fully qualified domain name (FQDN) of the certificate that needs to be validated.\n

    :type ValidationDomain: string
    :param ValidationDomain: [REQUIRED]\nThe base validation domain that will act as the suffix of the email addresses that are used to send the emails. This must be the same as the Domain value or a superdomain of the Domain value. For example, if you requested a certificate for site.subdomain.example.com and specify a ValidationDomain of subdomain.example.com , ACM sends email to the domain registrant, technical contact, and administrative contact in WHOIS and the following five addresses:\n\nadmin@subdomain.example.com\nadministrator@subdomain.example.com\nhostmaster@subdomain.example.com\npostmaster@subdomain.example.com\nwebmaster@subdomain.example.com\n\n

    """
    pass

def update_certificate_options(CertificateArn=None, Options=None):
    """
    Updates a certificate. Currently, you can use this function to specify whether to opt in to or out of recording your certificate in a certificate transparency log. For more information, see Opting Out of Certificate Transparency Logging .
    See also: AWS API Documentation
    
    
    :example: response = client.update_certificate_options(\n    CertificateArn='string',\n    Options={\n        'CertificateTransparencyLoggingPreference': 'ENABLED'|'DISABLED'\n    }\n)\n\n
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]\nARN of the requested certificate to update. This must be of the form:\n\n``arn:aws:acm:us-east-1:account :certificate/12345678-1234-1234-1234-123456789012 ``\n

    :type Options: dict
    :param Options: [REQUIRED]\nUse to update the options for your certificate. Currently, you can specify whether to add your certificate to a transparency log. Certificate transparency makes it possible to detect SSL/TLS certificates that have been mistakenly or maliciously issued. Certificates that have not been logged typically produce an error message in a browser.\n\nCertificateTransparencyLoggingPreference (string) --You can opt out of certificate transparency logging by specifying the DISABLED option. Opt in by specifying ENABLED .\n\n\n

    """
    pass

