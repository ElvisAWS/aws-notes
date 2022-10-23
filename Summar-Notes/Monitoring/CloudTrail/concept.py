

# Cloudtrail
    # AWS CloudTrail is an AWS service that helps you enable operational and risk auditing, governance, and compliance 
    # of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events 
    # include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs. CloudTrail 
    # is enabled on your AWS account when you create it. When activity occurs in your AWS account, that activity is recorded 
    # in a CloudTrail event. You can easily view recent events in the CloudTrail console by going to Event history. 
    # For an ongoing record of activity and events in your AWS account, create a trail. Visibility into your AWS account 
    # activity is a key aspect of security and operational best practices. You can use CloudTrail to view, search, download, 
    # archive, analyze, and respond to account activity across your AWS infrastructure. You can identify who or what took 
    # which action, what resources were acted upon, when the event occurred, and other details to help you analyze and 
    # respond to activity in your AWS account. Optionally, you can enable AWS CloudTrail Insights on a trail to 
    # help you identify and respond to unusual activity.
# You can put logs from Cloudtrail into S3 and CloudWatch logs
# Events are stored in 90 days
# For longer retension, transfer them to S3 then use Athena to analyse the logs
