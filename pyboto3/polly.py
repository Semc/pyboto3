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

def delete_lexicon(Name=None):
    """
    Deletes the specified pronunciation lexicon stored in an AWS Region. A lexicon which has been deleted is not available for speech synthesis, nor is it possible to retrieve it using either the GetLexicon or ListLexicon APIs.
    For more information, see Managing Lexicons .
    See also: AWS API Documentation
    
    Examples
    Deletes a specified pronunciation lexicon stored in an AWS Region.
    Expected Output:
    
    :example: response = client.delete_lexicon(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the lexicon to delete. Must be an existing lexicon in the region.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_voices(LanguageCode=None, IncludeAdditionalLanguageCodes=None, NextToken=None):
    """
    Returns the list of voices that are available for use when requesting speech synthesis. Each voice speaks a specified language, is either male or female, and is identified by an ID, which is the ASCII version of the voice name.
    When synthesizing speech ( SynthesizeSpeech ), you provide the voice ID for the voice you want from the list of voices returned by DescribeVoices .
    For example, you want your news reader application to read news in a specific language, but giving a user the option to choose the voice. Using the DescribeVoices operation you can provide the user with a list of available voices to select from.
    You can optionally specify a language code to filter the available voices. For example, if you specify en-US , the operation returns a list of all available US English voices.
    This operation requires permissions to perform the polly:DescribeVoices action.
    See also: AWS API Documentation
    
    Examples
    Returns the list of voices that are available for use when requesting speech synthesis. Displayed languages are those within the specified language code. If no language code is specified, voices for all available languages are displayed.
    Expected Output:
    
    :example: response = client.describe_voices(
        LanguageCode='cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
        IncludeAdditionalLanguageCodes=True|False,
        NextToken='string'
    )
    
    
    :type LanguageCode: string
    :param LanguageCode: The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don't specify this optional parameter, all available voices are returned.

    :type IncludeAdditionalLanguageCodes: boolean
    :param IncludeAdditionalLanguageCodes: Boolean value indicating whether to return any bilingual voices that use the specified language as an additional language. For instance, if you request all languages that use US English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US English, that voice will be included if you specify yes but not if you specify no .

    :type NextToken: string
    :param NextToken: An opaque pagination token returned from the previous DescribeVoices operation. If present, this indicates where to continue the listing.

    :rtype: dict
    :return: {
        'Voices': [
            {
                'Gender': 'Female'|'Male',
                'Id': 'Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Matthew'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Lea'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz'|'Vicki'|'Takumi'|'Seoyeon'|'Aditi'|'Zhiyu'|'Bianca'|'Lucia'|'Mia',
                'LanguageCode': 'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                'LanguageName': 'string',
                'Name': 'string',
                'AdditionalLanguageCodes': [
                    'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
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

def get_lexicon(Name=None):
    """
    Returns the content of the specified pronunciation lexicon stored in an AWS Region. For more information, see Managing Lexicons .
    See also: AWS API Documentation
    
    Examples
    Returns the content of the specified pronunciation lexicon stored in an AWS Region.
    Expected Output:
    
    :example: response = client.get_lexicon(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the lexicon.
            

    :rtype: dict
    :return: {
        'Lexicon': {
            'Content': 'string',
            'Name': 'string'
        },
        'LexiconAttributes': {
            'Alphabet': 'string',
            'LanguageCode': 'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
            'LastModified': datetime(2015, 1, 1),
            'LexiconArn': 'string',
            'LexemesCount': 123,
            'Size': 123
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

def get_speech_synthesis_task(TaskId=None):
    """
    Retrieves a specific SpeechSynthesisTask object based on its TaskID. This object contains information about the given speech synthesis task, including the status of the task, and a link to the S3 bucket containing the output of the task.
    See also: AWS API Documentation
    
    
    :example: response = client.get_speech_synthesis_task(
        TaskId='string'
    )
    
    
    :type TaskId: string
    :param TaskId: [REQUIRED]
            The Amazon Polly generated identifier for a speech synthesis task.
            

    :rtype: dict
    :return: {
        'SynthesisTask': {
            'TaskId': 'string',
            'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
            'TaskStatusReason': 'string',
            'OutputUri': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'RequestCharacters': 123,
            'SnsTopicArn': 'string',
            'LexiconNames': [
                'string',
            ],
            'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
            'SampleRate': 'string',
            'SpeechMarkTypes': [
                'sentence'|'ssml'|'viseme'|'word',
            ],
            'TextType': 'ssml'|'text',
            'VoiceId': 'Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Matthew'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Lea'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz'|'Vicki'|'Takumi'|'Seoyeon'|'Aditi'|'Zhiyu'|'Bianca'|'Lucia'|'Mia',
            'LanguageCode': 'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
        }
    }
    
    
    :returns: 
    (string) --
    
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

def list_lexicons(NextToken=None):
    """
    Returns a list of pronunciation lexicons stored in an AWS Region. For more information, see Managing Lexicons .
    See also: AWS API Documentation
    
    Examples
    Returns a list of pronunciation lexicons stored in an AWS Region.
    Expected Output:
    
    :example: response = client.list_lexicons(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: An opaque pagination token returned from previous ListLexicons operation. If present, indicates where to continue the list of lexicons.

    :rtype: dict
    :return: {
        'Lexicons': [
            {
                'Name': 'string',
                'Attributes': {
                    'Alphabet': 'string',
                    'LanguageCode': 'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                    'LastModified': datetime(2015, 1, 1),
                    'LexiconArn': 'string',
                    'LexemesCount': 123,
                    'Size': 123
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_speech_synthesis_tasks(MaxResults=None, NextToken=None, Status=None):
    """
    Returns a list of SpeechSynthesisTask objects ordered by their creation date. This operation can filter the tasks by their status, for example, allowing users to list only tasks that are completed.
    See also: AWS API Documentation
    
    
    :example: response = client.list_speech_synthesis_tasks(
        MaxResults=123,
        NextToken='string',
        Status='scheduled'|'inProgress'|'completed'|'failed'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Maximum number of speech synthesis tasks returned in a List operation.

    :type NextToken: string
    :param NextToken: The pagination token to use in the next request to continue the listing of speech synthesis tasks.

    :type Status: string
    :param Status: Status of the speech synthesis tasks returned in a List operation

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'SynthesisTasks': [
            {
                'TaskId': 'string',
                'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
                'TaskStatusReason': 'string',
                'OutputUri': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'RequestCharacters': 123,
                'SnsTopicArn': 'string',
                'LexiconNames': [
                    'string',
                ],
                'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
                'SampleRate': 'string',
                'SpeechMarkTypes': [
                    'sentence'|'ssml'|'viseme'|'word',
                ],
                'TextType': 'ssml'|'text',
                'VoiceId': 'Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Matthew'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Lea'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz'|'Vicki'|'Takumi'|'Seoyeon'|'Aditi'|'Zhiyu'|'Bianca'|'Lucia'|'Mia',
                'LanguageCode': 'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_lexicon(Name=None, Content=None):
    """
    Stores a pronunciation lexicon in an AWS Region. If a lexicon with the same name already exists in the region, it is overwritten by the new lexicon. Lexicon operations have eventual consistency, therefore, it might take some time before the lexicon is available to the SynthesizeSpeech operation.
    For more information, see Managing Lexicons .
    See also: AWS API Documentation
    
    Examples
    Stores a pronunciation lexicon in an AWS Region.
    Expected Output:
    
    :example: response = client.put_lexicon(
        Name='string',
        Content='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long.
            

    :type Content: string
    :param Content: [REQUIRED]
            Content of the PLS lexicon as string data.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_speech_synthesis_task(LexiconNames=None, OutputFormat=None, OutputS3BucketName=None, OutputS3KeyPrefix=None, SampleRate=None, SnsTopicArn=None, SpeechMarkTypes=None, Text=None, TextType=None, VoiceId=None, LanguageCode=None):
    """
    Allows the creation of an asynchronous synthesis task, by starting a new SpeechSynthesisTask . This operation requires all the standard information needed for speech synthesis, plus the name of an Amazon S3 bucket for the service to store the output of the synthesis task and two optional parameters (OutputS3KeyPrefix and SnsTopicArn). Once the synthesis task is created, this operation will return a SpeechSynthesisTask object, which will include an identifier of this task as well as the current status.
    See also: AWS API Documentation
    
    
    :example: response = client.start_speech_synthesis_task(
        LexiconNames=[
            'string',
        ],
        OutputFormat='json'|'mp3'|'ogg_vorbis'|'pcm',
        OutputS3BucketName='string',
        OutputS3KeyPrefix='string',
        SampleRate='string',
        SnsTopicArn='string',
        SpeechMarkTypes=[
            'sentence'|'ssml'|'viseme'|'word',
        ],
        Text='string',
        TextType='ssml'|'text',
        VoiceId='Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Matthew'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Lea'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz'|'Vicki'|'Takumi'|'Seoyeon'|'Aditi'|'Zhiyu'|'Bianca'|'Lucia'|'Mia',
        LanguageCode='cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
    )
    
    
    :type LexiconNames: list
    :param LexiconNames: List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice.
            (string) --
            

    :type OutputFormat: string
    :param OutputFormat: [REQUIRED]
            The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.
            

    :type OutputS3BucketName: string
    :param OutputS3BucketName: [REQUIRED]
            Amazon S3 bucket name to which the output file will be saved.
            

    :type OutputS3KeyPrefix: string
    :param OutputS3KeyPrefix: The Amazon S3 key prefix for the output speech file.

    :type SampleRate: string
    :param SampleRate: The audio frequency specified in Hz.
            The valid values for mp3 and ogg_vorbis are '8000', '16000', and '22050'. The default value is '22050'.
            Valid values for pcm are '8000' and '16000' The default value is '16000'.
            

    :type SnsTopicArn: string
    :param SnsTopicArn: ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.

    :type SpeechMarkTypes: list
    :param SpeechMarkTypes: The type of speech marks returned for the input text.
            (string) --
            

    :type Text: string
    :param Text: [REQUIRED]
            The input text to synthesize. If you specify ssml as the TextType, follow the SSML format for the input text.
            

    :type TextType: string
    :param TextType: Specifies whether the input text is plain text or SSML. The default value is plain text.

    :type VoiceId: string
    :param VoiceId: [REQUIRED]
            Voice ID to use for the synthesis.
            

    :type LanguageCode: string
    :param LanguageCode: Optional language code for the Speech Synthesis request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).
            If a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the DescribeVoices operation for the LanguageCode parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.
            

    :rtype: dict
    :return: {
        'SynthesisTask': {
            'TaskId': 'string',
            'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
            'TaskStatusReason': 'string',
            'OutputUri': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'RequestCharacters': 123,
            'SnsTopicArn': 'string',
            'LexiconNames': [
                'string',
            ],
            'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
            'SampleRate': 'string',
            'SpeechMarkTypes': [
                'sentence'|'ssml'|'viseme'|'word',
            ],
            'TextType': 'ssml'|'text',
            'VoiceId': 'Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Matthew'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Lea'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz'|'Vicki'|'Takumi'|'Seoyeon'|'Aditi'|'Zhiyu'|'Bianca'|'Lucia'|'Mia',
            'LanguageCode': 'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def synthesize_speech(LexiconNames=None, OutputFormat=None, SampleRate=None, SpeechMarkTypes=None, Text=None, TextType=None, VoiceId=None, LanguageCode=None):
    """
    Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid, well-formed SSML. Some alphabets might not be available with all the voices (for example, Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For more information, see How it Works .
    See also: AWS API Documentation
    
    Examples
    Synthesizes plain text or SSML into a file of human-like speech.
    Expected Output:
    
    :example: response = client.synthesize_speech(
        LexiconNames=[
            'string',
        ],
        OutputFormat='json'|'mp3'|'ogg_vorbis'|'pcm',
        SampleRate='string',
        SpeechMarkTypes=[
            'sentence'|'ssml'|'viseme'|'word',
        ],
        Text='string',
        TextType='ssml'|'text',
        VoiceId='Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Matthew'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Lea'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz'|'Vicki'|'Takumi'|'Seoyeon'|'Aditi'|'Zhiyu'|'Bianca'|'Lucia'|'Mia',
        LanguageCode='cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
    )
    
    
    :type LexiconNames: list
    :param LexiconNames: List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see PutLexicon .
            (string) --
            

    :type OutputFormat: string
    :param OutputFormat: [REQUIRED]
            The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.
            When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.
            

    :type SampleRate: string
    :param SampleRate: The audio frequency specified in Hz.
            The valid values for mp3 and ogg_vorbis are '8000', '16000', and '22050'. The default value is '22050'.
            Valid values for pcm are '8000' and '16000' The default value is '16000'.
            

    :type SpeechMarkTypes: list
    :param SpeechMarkTypes: The type of speech marks returned for the input text.
            (string) --
            

    :type Text: string
    :param Text: [REQUIRED]
            Input text to synthesize. If you specify ssml as the TextType , follow the SSML format for the input text.
            

    :type TextType: string
    :param TextType: Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see Using SSML .

    :type VoiceId: string
    :param VoiceId: [REQUIRED]
            Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the DescribeVoices operation.
            

    :type LanguageCode: string
    :param LanguageCode: Optional language code for the Synthesize Speech request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).
            If a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the DescribeVoices operation for the LanguageCode parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.
            

    :rtype: dict
    :return: {
        'AudioStream': StreamingBody(),
        'ContentType': 'string',
        'RequestCharacters': 123
    }
    
    
    :returns: 
    If you request mp3 as the OutputFormat , the ContentType returned is audio/mpeg.
    If you request ogg_vorbis as the OutputFormat , the ContentType returned is audio/ogg.
    If you request pcm as the OutputFormat , the ContentType returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.
    If you request json as the OutputFormat , the ContentType returned is audio/json.
    
    """
    pass

