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

def create_budget(AccountId=None, Budget=None, NotificationsWithSubscribers=None):
    """
    Creates a budget and, if included, notifications and subscribers.
    See also: AWS API Documentation
    
    
    :example: response = client.create_budget(
        AccountId='string',
        Budget={
            'BudgetName': 'string',
            'BudgetLimit': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'CostFilters': {
                'string': [
                    'string',
                ]
            },
            'CostTypes': {
                'IncludeTax': True|False,
                'IncludeSubscription': True|False,
                'UseBlended': True|False,
                'IncludeRefund': True|False,
                'IncludeCredit': True|False,
                'IncludeUpfront': True|False,
                'IncludeRecurring': True|False,
                'IncludeOtherSubscription': True|False,
                'IncludeSupport': True|False,
                'IncludeDiscount': True|False,
                'UseAmortized': True|False
            },
            'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
            'TimePeriod': {
                'Start': datetime(2015, 1, 1),
                'End': datetime(2015, 1, 1)
            },
            'CalculatedSpend': {
                'ActualSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'ForecastedSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
            },
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE',
            'LastUpdatedTime': datetime(2015, 1, 1)
        },
        NotificationsWithSubscribers=[
            {
                'Notification': {
                    'NotificationType': 'ACTUAL'|'FORECASTED',
                    'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                    'Threshold': 123.0,
                    'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                    'NotificationState': 'OK'|'ALARM'
                },
                'Subscribers': [
                    {
                        'SubscriptionType': 'SNS'|'EMAIL',
                        'Address': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget.
            

    :type Budget: dict
    :param Budget: [REQUIRED]
            The budget object that you want to create.
            BudgetName (string) -- [REQUIRED]The name of a budget. The name must be unique within accounts. The : and \ characters aren't allowed in BudgetName .
            BudgetLimit (dict) --The total amount of cost, usage, RI utilization, or RI coverage that you want to track with your budget.
            BudgetLimit is required for cost or usage budgets, but optional for RI utilization or coverage budgets. RI utilization or coverage budgets default to 100 , which is the only valid value for RI utilization or coverage budgets.
            Amount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            CostFilters (dict) --The cost filters, such as service or region, that are applied to a budget.
            AWS Budgets supports the following services as a filter for RI budgets:
            Amazon Elastic Compute Cloud - Compute
            Amazon Redshift
            Amazon Relational Database Service
            Amazon ElastiCache
            Amazon Elasticsearch Service
            (string) --A generic string.
            (list) --
            (string) --A generic string.
            
            CostTypes (dict) --The types of costs that are included in this COST budget.
            USAGE , RI_UTILIZATION , and RI_COVERAGE budgets do not have CostTypes .
            IncludeTax (boolean) --Specifies whether a budget includes taxes.
            The default value is true .
            IncludeSubscription (boolean) --Specifies whether a budget includes subscriptions.
            The default value is true .
            UseBlended (boolean) --Specifies whether a budget uses a blended rate.
            The default value is false .
            IncludeRefund (boolean) --Specifies whether a budget includes refunds.
            The default value is true .
            IncludeCredit (boolean) --Specifies whether a budget includes credits.
            The default value is true .
            IncludeUpfront (boolean) --Specifies whether a budget includes upfront RI costs.
            The default value is true .
            IncludeRecurring (boolean) --Specifies whether a budget includes recurring fees such as monthly RI fees.
            The default value is true .
            IncludeOtherSubscription (boolean) --Specifies whether a budget includes non-RI subscription costs.
            The default value is true .
            IncludeSupport (boolean) --Specifies whether a budget includes support subscription fees.
            The default value is true .
            IncludeDiscount (boolean) --Specifies whether a budget includes discounts.
            The default value is true .
            UseAmortized (boolean) --Specifies whether a budget uses the amortized rate.
            The default value is false .
            TimeUnit (string) -- [REQUIRED]The length of time until a budget resets the actual and forecasted spend. DAILY is available only for RI_UTILIZATION and RI_COVERAGE budgets.
            TimePeriod (dict) --The period of time that is covered by a budget. The period has a start date and an end date. The start date must come before the end date. The end date must come before 06/15/87 00:00 UTC .
            If you create your budget and don't specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn't set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . If you didn't specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            You can change either date with the UpdateBudget operation.
            After the end date, AWS deletes the budget and all associated notifications and subscribers.
            Start (datetime) --The start date for a budget. If you created your budget and didn't specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn't set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            You can change your start date with the UpdateBudget operation.
            End (datetime) --The end date for a budget. If you didn't specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            After the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.
            CalculatedSpend (dict) --The actual and forecasted cost or usage that the budget tracks.
            ActualSpend (dict) -- [REQUIRED]The amount of cost, usage, or RI units that you have used.
            Amount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            ForecastedSpend (dict) --The amount of cost, usage, or RI units that you are forecasted to use.
            Amount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            
            BudgetType (string) -- [REQUIRED]Whether this budget tracks monetary costs, usage, RI utilization, or RI coverage.
            LastUpdatedTime (datetime) --The last time that you updated this budget.
            

    :type NotificationsWithSubscribers: list
    :param NotificationsWithSubscribers: A notification that you want to associate with a budget. A budget can have up to five notifications, and each notification can have one SNS subscriber and up to 10 email subscribers. If you include notifications and subscribers in your CreateBudget call, AWS creates the notifications and subscribers for you.
            (dict) --A notification with subscribers. A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.
            Notification (dict) -- [REQUIRED]The notification that is associated with a budget.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you're forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.
            Threshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.
            NotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.
            Subscribers (list) -- [REQUIRED]A list of subscribers who are subscribed to this notification.
            (dict) --The subscriber to a budget notification. The subscriber consists of a subscription type and either an Amazon SNS topic or an email address.
            For example, an email subscriber would have the following parameters:
            A subscriptionType of EMAIL
            An address of example@example.com
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_notification(AccountId=None, BudgetName=None, Notification=None, Subscribers=None):
    """
    Creates a notification. You must create the budget before you create the associated notification.
    See also: AWS API Documentation
    
    
    :example: response = client.create_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        Subscribers=[
            {
                'SubscriptionType': 'SNS'|'EMAIL',
                'Address': 'string'
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget that you want to create a notification for.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget that you want AWS to notify you about. Budget names must be unique within an account.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification that you want to create.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you're forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.
            Threshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.
            NotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.
            

    :type Subscribers: list
    :param Subscribers: [REQUIRED]
            A list of subscribers that you want to associate with the notification. Each notification can have one SNS subscriber and up to 10 email subscribers.
            (dict) --The subscriber to a budget notification. The subscriber consists of a subscription type and either an Amazon SNS topic or an email address.
            For example, an email subscriber would have the following parameters:
            A subscriptionType of EMAIL
            An address of example@example.com
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_subscriber(AccountId=None, BudgetName=None, Notification=None, Subscriber=None):
    """
    Creates a subscriber. You must create the associated budget and notification before you create the subscriber.
    See also: AWS API Documentation
    
    
    :example: response = client.create_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        Subscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget that you want to create a subscriber for.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget that you want to subscribe to. Budget names must be unique within an account.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification that you want to create a subscriber for.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you're forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.
            Threshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.
            NotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.
            

    :type Subscriber: dict
    :param Subscriber: [REQUIRED]
            The subscriber that you want to associate with a budget notification.
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_budget(AccountId=None, BudgetName=None):
    """
    Deletes a budget. You can delete your budget at any time.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_budget(
        AccountId='string',
        BudgetName='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget that you want to delete.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget that you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_notification(AccountId=None, BudgetName=None, Notification=None):
    """
    Deletes a notification.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose notification you want to delete.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose notification you want to delete.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification that you want to delete.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you're forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.
            Threshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.
            NotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_subscriber(AccountId=None, BudgetName=None, Notification=None, Subscriber=None):
    """
    Deletes a subscriber.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        Subscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose subscriber you want to delete.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose subscriber you want to delete.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification whose subscriber you want to delete.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you're forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.
            Threshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.
            NotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.
            

    :type Subscriber: dict
    :param Subscriber: [REQUIRED]
            The subscriber that you want to delete.
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_budget(AccountId=None, BudgetName=None):
    """
    Describes a budget.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_budget(
        AccountId='string',
        BudgetName='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget that you want a description of.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget that you want a description of.
            

    :rtype: dict
    :return: {
        'Budget': {
            'BudgetName': 'string',
            'BudgetLimit': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'CostFilters': {
                'string': [
                    'string',
                ]
            },
            'CostTypes': {
                'IncludeTax': True|False,
                'IncludeSubscription': True|False,
                'UseBlended': True|False,
                'IncludeRefund': True|False,
                'IncludeCredit': True|False,
                'IncludeUpfront': True|False,
                'IncludeRecurring': True|False,
                'IncludeOtherSubscription': True|False,
                'IncludeSupport': True|False,
                'IncludeDiscount': True|False,
                'UseAmortized': True|False
            },
            'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
            'TimePeriod': {
                'Start': datetime(2015, 1, 1),
                'End': datetime(2015, 1, 1)
            },
            'CalculatedSpend': {
                'ActualSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'ForecastedSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
            },
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE',
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Amazon Elastic Compute Cloud - Compute
    Amazon Redshift
    Amazon Relational Database Service
    Amazon ElastiCache
    Amazon Elasticsearch Service
    
    """
    pass

def describe_budget_performance_history(AccountId=None, BudgetName=None, TimePeriod=None, MaxResults=None, NextToken=None):
    """
    Describes the history for DAILY , MONTHLY , and QUARTERLY budgets. Budget history isn't available for ANNUAL budgets.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_budget_performance_history(
        AccountId='string',
        BudgetName='string',
        TimePeriod={
            'Start': datetime(2015, 1, 1),
            'End': datetime(2015, 1, 1)
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The account ID of the user. It should be a 12-digit number.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            A string that represents the budget name. The ':' and '' characters aren't allowed.
            

    :type TimePeriod: dict
    :param TimePeriod: Retrieves how often the budget went into an ALARM state for the specified time period.
            Start (datetime) --The start date for a budget. If you created your budget and didn't specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn't set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            You can change your start date with the UpdateBudget operation.
            End (datetime) --The end date for a budget. If you didn't specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            After the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.
            

    :type MaxResults: integer
    :param MaxResults: An integer that represents how many entries a paginated response contains. The maximum is 100.

    :type NextToken: string
    :param NextToken: A generic string.

    :rtype: dict
    :return: {
        'BudgetPerformanceHistory': {
            'BudgetName': 'string',
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE',
            'CostFilters': {
                'string': [
                    'string',
                ]
            },
            'CostTypes': {
                'IncludeTax': True|False,
                'IncludeSubscription': True|False,
                'UseBlended': True|False,
                'IncludeRefund': True|False,
                'IncludeCredit': True|False,
                'IncludeUpfront': True|False,
                'IncludeRecurring': True|False,
                'IncludeOtherSubscription': True|False,
                'IncludeSupport': True|False,
                'IncludeDiscount': True|False,
                'UseAmortized': True|False
            },
            'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
            'BudgetedAndActualAmountsList': [
                {
                    'BudgetedAmount': {
                        'Amount': 'string',
                        'Unit': 'string'
                    },
                    'ActualAmount': {
                        'Amount': 'string',
                        'Unit': 'string'
                    },
                    'TimePeriod': {
                        'Start': datetime(2015, 1, 1),
                        'End': datetime(2015, 1, 1)
                    }
                },
            ]
        },
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_budgets(AccountId=None, MaxResults=None, NextToken=None):
    """
    Lists the budgets that are associated with an account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_budgets(
        AccountId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budgets that you want descriptions of.
            

    :type MaxResults: integer
    :param MaxResults: An optional integer that represents how many entries a paginated response contains. The maximum is 100.

    :type NextToken: string
    :param NextToken: The pagination token that you include in your request to indicate the next set of results that you want to retrieve.

    :rtype: dict
    :return: {
        'Budgets': [
            {
                'BudgetName': 'string',
                'BudgetLimit': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'CostFilters': {
                    'string': [
                        'string',
                    ]
                },
                'CostTypes': {
                    'IncludeTax': True|False,
                    'IncludeSubscription': True|False,
                    'UseBlended': True|False,
                    'IncludeRefund': True|False,
                    'IncludeCredit': True|False,
                    'IncludeUpfront': True|False,
                    'IncludeRecurring': True|False,
                    'IncludeOtherSubscription': True|False,
                    'IncludeSupport': True|False,
                    'IncludeDiscount': True|False,
                    'UseAmortized': True|False
                },
                'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
                'TimePeriod': {
                    'Start': datetime(2015, 1, 1),
                    'End': datetime(2015, 1, 1)
                },
                'CalculatedSpend': {
                    'ActualSpend': {
                        'Amount': 'string',
                        'Unit': 'string'
                    },
                    'ForecastedSpend': {
                        'Amount': 'string',
                        'Unit': 'string'
                    }
                },
                'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE',
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Amazon Elastic Compute Cloud - Compute
    Amazon Redshift
    Amazon Relational Database Service
    Amazon ElastiCache
    Amazon Elasticsearch Service
    
    """
    pass

def describe_notifications_for_budget(AccountId=None, BudgetName=None, MaxResults=None, NextToken=None):
    """
    Lists the notifications that are associated with a budget.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_notifications_for_budget(
        AccountId='string',
        BudgetName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose notifications you want descriptions of.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose notifications you want descriptions of.
            

    :type MaxResults: integer
    :param MaxResults: An optional integer that represents how many entries a paginated response contains. The maximum is 100.

    :type NextToken: string
    :param NextToken: The pagination token that you include in your request to indicate the next set of results that you want to retrieve.

    :rtype: dict
    :return: {
        'Notifications': [
            {
                'NotificationType': 'ACTUAL'|'FORECASTED',
                'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                'Threshold': 123.0,
                'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                'NotificationState': 'OK'|'ALARM'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    A notificationType of ACTUAL
    A thresholdType of PERCENTAGE
    A comparisonOperator of GREATER_THAN
    A notification threshold of 80
    
    """
    pass

def describe_subscribers_for_notification(AccountId=None, BudgetName=None, Notification=None, MaxResults=None, NextToken=None):
    """
    Lists the subscribers that are associated with a notification.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_subscribers_for_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose subscribers you want descriptions of.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose subscribers you want descriptions of.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification whose subscribers you want to list.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you're forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.
            Threshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.
            NotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.
            

    :type MaxResults: integer
    :param MaxResults: An optional integer that represents how many entries a paginated response contains. The maximum is 100.

    :type NextToken: string
    :param NextToken: The pagination token that you include in your request to indicate the next set of results that you want to retrieve.

    :rtype: dict
    :return: {
        'Subscribers': [
            {
                'SubscriptionType': 'SNS'|'EMAIL',
                'Address': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    A subscriptionType of EMAIL
    An address of example@example.com
    
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

def update_budget(AccountId=None, NewBudget=None):
    """
    Updates a budget. You can change every part of a budget except for the budgetName and the calculatedSpend . When you modify a budget, the calculatedSpend drops to zero until AWS has new usage data to use for forecasting.
    See also: AWS API Documentation
    
    
    :example: response = client.update_budget(
        AccountId='string',
        NewBudget={
            'BudgetName': 'string',
            'BudgetLimit': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'CostFilters': {
                'string': [
                    'string',
                ]
            },
            'CostTypes': {
                'IncludeTax': True|False,
                'IncludeSubscription': True|False,
                'UseBlended': True|False,
                'IncludeRefund': True|False,
                'IncludeCredit': True|False,
                'IncludeUpfront': True|False,
                'IncludeRecurring': True|False,
                'IncludeOtherSubscription': True|False,
                'IncludeSupport': True|False,
                'IncludeDiscount': True|False,
                'UseAmortized': True|False
            },
            'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
            'TimePeriod': {
                'Start': datetime(2015, 1, 1),
                'End': datetime(2015, 1, 1)
            },
            'CalculatedSpend': {
                'ActualSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'ForecastedSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
            },
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE',
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget that you want to update.
            

    :type NewBudget: dict
    :param NewBudget: [REQUIRED]
            The budget that you want to update your budget to.
            BudgetName (string) -- [REQUIRED]The name of a budget. The name must be unique within accounts. The : and \ characters aren't allowed in BudgetName .
            BudgetLimit (dict) --The total amount of cost, usage, RI utilization, or RI coverage that you want to track with your budget.
            BudgetLimit is required for cost or usage budgets, but optional for RI utilization or coverage budgets. RI utilization or coverage budgets default to 100 , which is the only valid value for RI utilization or coverage budgets.
            Amount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            CostFilters (dict) --The cost filters, such as service or region, that are applied to a budget.
            AWS Budgets supports the following services as a filter for RI budgets:
            Amazon Elastic Compute Cloud - Compute
            Amazon Redshift
            Amazon Relational Database Service
            Amazon ElastiCache
            Amazon Elasticsearch Service
            (string) --A generic string.
            (list) --
            (string) --A generic string.
            
            CostTypes (dict) --The types of costs that are included in this COST budget.
            USAGE , RI_UTILIZATION , and RI_COVERAGE budgets do not have CostTypes .
            IncludeTax (boolean) --Specifies whether a budget includes taxes.
            The default value is true .
            IncludeSubscription (boolean) --Specifies whether a budget includes subscriptions.
            The default value is true .
            UseBlended (boolean) --Specifies whether a budget uses a blended rate.
            The default value is false .
            IncludeRefund (boolean) --Specifies whether a budget includes refunds.
            The default value is true .
            IncludeCredit (boolean) --Specifies whether a budget includes credits.
            The default value is true .
            IncludeUpfront (boolean) --Specifies whether a budget includes upfront RI costs.
            The default value is true .
            IncludeRecurring (boolean) --Specifies whether a budget includes recurring fees such as monthly RI fees.
            The default value is true .
            IncludeOtherSubscription (boolean) --Specifies whether a budget includes non-RI subscription costs.
            The default value is true .
            IncludeSupport (boolean) --Specifies whether a budget includes support subscription fees.
            The default value is true .
            IncludeDiscount (boolean) --Specifies whether a budget includes discounts.
            The default value is true .
            UseAmortized (boolean) --Specifies whether a budget uses the amortized rate.
            The default value is false .
            TimeUnit (string) -- [REQUIRED]The length of time until a budget resets the actual and forecasted spend. DAILY is available only for RI_UTILIZATION and RI_COVERAGE budgets.
            TimePeriod (dict) --The period of time that is covered by a budget. The period has a start date and an end date. The start date must come before the end date. The end date must come before 06/15/87 00:00 UTC .
            If you create your budget and don't specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn't set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . If you didn't specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            You can change either date with the UpdateBudget operation.
            After the end date, AWS deletes the budget and all associated notifications and subscribers.
            Start (datetime) --The start date for a budget. If you created your budget and didn't specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn't set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            You can change your start date with the UpdateBudget operation.
            End (datetime) --The end date for a budget. If you didn't specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            After the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.
            CalculatedSpend (dict) --The actual and forecasted cost or usage that the budget tracks.
            ActualSpend (dict) -- [REQUIRED]The amount of cost, usage, or RI units that you have used.
            Amount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            ForecastedSpend (dict) --The amount of cost, usage, or RI units that you are forecasted to use.
            Amount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            
            BudgetType (string) -- [REQUIRED]Whether this budget tracks monetary costs, usage, RI utilization, or RI coverage.
            LastUpdatedTime (datetime) --The last time that you updated this budget.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_notification(AccountId=None, BudgetName=None, OldNotification=None, NewNotification=None):
    """
    Updates a notification.
    See also: AWS API Documentation
    
    
    :example: response = client.update_notification(
        AccountId='string',
        BudgetName='string',
        OldNotification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        NewNotification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose notification you want to update.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose notification you want to update.
            

    :type OldNotification: dict
    :param OldNotification: [REQUIRED]
            The previous notification that is associated with a budget.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you're forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.
            Threshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.
            NotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.
            

    :type NewNotification: dict
    :param NewNotification: [REQUIRED]
            The updated notification to be associated with a budget.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you're forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.
            Threshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.
            NotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_subscriber(AccountId=None, BudgetName=None, Notification=None, OldSubscriber=None, NewSubscriber=None):
    """
    Updates a subscriber.
    See also: AWS API Documentation
    
    
    :example: response = client.update_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        OldSubscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        },
        NewSubscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose subscriber you want to update.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose subscriber you want to update.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification whose subscriber you want to update.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you're forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.
            Threshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.
            NotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.
            

    :type OldSubscriber: dict
    :param OldSubscriber: [REQUIRED]
            The previous subscriber that is associated with a budget notification.
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            

    :type NewSubscriber: dict
    :param NewSubscriber: [REQUIRED]
            The updated subscriber that is associated with a budget notification.
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

