

# In-memory acceleration with DynamoDB Accelerator (DAX)
    # Solves the Hot Key problem
    # We need to provision nodes up to 10 and supports Multi-AZ
    # 5 mins TTL for caache by default
    # Amazon DynamoDB is designed for scale and performance. In most cases, the DynamoDB response times can be measured 
    # in single-digit milliseconds. However, there are certain use cases that require response times in microseconds. 
    # For these use cases, DynamoDB Accelerator (DAX) delivers fast response times for accessing eventually consistent 
    # data.
    # DAX is a DynamoDB-compatible caching service that enables you to benefit from fast in-memory performance for 
    # demanding applications. DAX addresses three core scenarios:
        # As an in-memory cache
            # DAX reduces the response times of eventually consistent read workloads by an order of magnitude from 
            # single-digit milliseconds to microseconds.
        # DAX reduces operational and application complexity 
            # By providing a managed service that is API-compatible with DynamoDB. Therefore, it requires only minimal 
            # functional changes to use with an existing application.
        # For read-heavy or bursty workloads, 
            # DAX provides increased throughput and potential operational cost savings 
            # by reducing the need to overprovision read capacity units. This is especially beneficial for applications 
            # that require repeated reads for individual keys.
    # DAX supports server-side encryption. With encryption at rest, the data persisted by DAX on disk will be encrypted. 
    # DAX writes data to disk as part of propagating changes from the primary node to read replicas.
    # DAX also supports encryption in transit, ensuring that all requests and responses between your application and 
    # the cluster are encrypted by transport level security (TLS), and connections to the cluster can be authenticated 
    # by verification of a cluster x509 certificate.