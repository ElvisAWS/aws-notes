

# Producers
    # Puts data into streams
    # Data consist of 
        # Sequence number
        # Partition Key
        # Data Blb
    # Producers use
        # AWS SDK 
        # Kinesis producer library
        # Kinesis agent
    # Write throughput is 1MB/s per shard
    # PuRecord API
    # Use batching to increase throughput
    # Always use a highly distributed partition key to avoid throttling
    