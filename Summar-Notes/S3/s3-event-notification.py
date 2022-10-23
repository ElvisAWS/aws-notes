
# You can use the Amazon S3 Event Notifications feature to receive notifications when certain events happen in your 
# S3 bucket. To enable notifications, add a notification configuration that identifies the events that you want 
# Amazon S3 to publish. Make sure that it also identifies the destinations where you want Amazon S3 to send the 
# notifications. You store this configuration in the notification subresource that's associated with a bucket.
# Supported event destinations
    # Amazon SNS topic
        # Amazon SNS is a flexible, fully managed push messaging service. You can use this service to push messages 
        # to mobile devices or distributed services. With SNS, you can publish a message once, and deliver it one or 
        # more times. Currently, Standard SNS is only allowed as an S3 event notification destination, whereas SNS 
        # FIFO is not allowed.
        # Amazon SNS both coordinates and manages sending and delivering messages to subscribing endpoints or clients. 
        # You can use the Amazon SNS console to create an Amazon SNS topic that your notifications can be sent to.
        # The topic must be in the same AWS Region as your Amazon S3 bucket
    # Amazon SQS queue
        # Amazon SQS offers reliable and scalable hosted queues for storing messages as they travel between computers. 
        # You can use Amazon SQS to transmit any volume of data without requiring other services to be always available. 
        # You can use the Amazon SQS console to create an Amazon SQS queue that your notifications can be sent to.
        # The Amazon SQS queue must be in the same AWS Region as your Amazon S3 bucket.
    # Lambda function
        # You can use AWS Lambda to extend other AWS services with custom logic, or create your own backend that 
        # operates at AWS scale, performance, and security. With Lambda, you can create discrete, event-driven 
        # applications that run only when needed. You can also use it to scale these applications automatically from 
        # a few requests a day to thousands a second.
    # Amazon EventBridge
        # Amazon EventBridge is a serverless event bus, which receives events from AWS services. You can set up 
        # rules to match events and deliver them to targets, such as an AWS service or an HTTP endpoint. 
        # Unlike other destinations, you can either enable or disable events to be delivered to EventBridge for 
        # a bucket. If you enable delivery, all events are sent to EventBridge. Moreover, you can use EventBridge 
        # rules to route events to additional targets.