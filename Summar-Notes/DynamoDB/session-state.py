

# Session state accross services applications
    # Elastic Cache will be in memory
    # Dynamodb will be severless
    # EFS must be attached to EC2 instances as network drive
    # EBS 7 instance store can only be used for local caching not shared caching
    # S3 has higher latency and meant for large objects
