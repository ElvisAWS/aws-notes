

# Subscriptions
    # You can use subscriptions to get access to a real-time feed of log events from CloudWatch Logs and have it 
    # delivered to other services such as an Amazon Kinesis stream, an Amazon Kinesis Data Firehose stream, or AWS 
    # Lambda for custom processing, analysis, or loading to other systems. When log events are sent to the receiving 
    # service, they are base64 encoded and compressed with the gzip format. To begin subscribing to log events, 
    # create the receiving resource, such as a Kinesis stream, where the events will be delivered. A subscription 
    # filter defines the filter pattern to use for filtering which log events get delivered to your AWS resource, 
    # as well as information about where to send matching log events to.
    # If the destination service returns a retryable error such as a throttling exception or a retryable service 
    # exception (HTTP 5xx for example), CloudWatch Logs continues to retry delivery for up to 24 hours. CloudWatch 
    # Logs does not try to re-deliver if the error is a non-retryable error, such as AccessDeniedException or 
    # ResourceNotFoundException.