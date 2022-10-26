
# Asynchronous invocation implies function is invocked but we do not know the results
    # S3, SNS, CloudWatch Events
    # The events are placed in event queues
    # lambda attempts to re-try
    # Make sure your lambda function is idempotent
    # Duplicate log entries will be seen in cloudwatch log incase of retries
    # DLQ will be needed to process the failed events. 
        # When we invoke a function asynchronously, we do not get the results but just the status code that the function
        # was successfully invoked. We thus need a DLQ to capture any failed invokations
        # We can always configure a number of retries before sending to our DLQ in SQS
    # 
