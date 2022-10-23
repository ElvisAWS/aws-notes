

# CloudTrail Insights
    # AWS CloudTrail Insights helps AWS users identify and respond to unusual activity associated with write API calls 
    # by continuously analyzing CloudTrail management events.
    # Insights events are logged when CloudTrail detects unusual write management API activity in your account. If you 
    # have CloudTrail Insights enabled and CloudTrail detects unusual activity, Insights events are delivered to the 
    # destination S3 bucket for your trail. You can also see the type of insight and the incident time period when you 
    # view Insights events on the CloudTrail console. Unlike other types of events captured in a CloudTrail trail, 
    # Insights events are logged only when CloudTrail detects changes in your account's API usage that differ significantly 
    # from the account's typical usage patterns.
    # CloudTrail Insights continuously monitors CloudTrail write management events, and uses mathematical models to determine 
    # the normal levels of API event and error rate activity for an account. CloudTrail Insights identifies behavior 
    # that is outside normal patterns, generates Insights events, and delivers those events to a /CloudTrail-Insight 
    # folder in the chosen destination S3 bucket for your trail. You can also access and view Insights events in the 
    # AWS Management Console for CloudTrail. For more information about how to access and view Insights events in the 
    # console and by using the AWS