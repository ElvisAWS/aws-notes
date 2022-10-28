

# Strongly Consistent Reads
    # When you request a strongly consistent read, DynamoDB returns a response with the most up-to-date data, 
    # reflecting the updates from all prior write operations that were successful.
# Eventually Consistent Reads 
    # The eventual consistency option is the default in Amazon DynamoDB and maximizes the read throughput. 
    # However, an eventually consistent read might not always reflect the results of a recently completed write. 
    # Consistency across all copies of data is usually reached within a second.