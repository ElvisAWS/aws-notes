
# DynamoDB Accelerator (DAX)
    # DynamoDB Accelerator (DAX) is a fully managed, custom cache for Dynamo. 
    # It saves the results of various DynamoDB queries in order to speed up read heavy applications. 
    # To use it, simply provision a DAX cluster and shift your existing calls to it. No re-coding necessary.
    # DAX is extensively used for intensive reads through eventual consistent reads and for latency sensitive 
    # applications. Also DAX stores cache using these parameters:-
        # Item cache - populated with items with based on GetItem results.
        # Query cache - based on parameters used while using query or scan method
    # You can not invalidate cache only after 5 mins TTL is reached
    # High latency
# ElastiCache
    # You can get the same Dax results with ElastiCache but you need to do more of the heavy lifting.
    # ElastiCache (available as a managed service) can cache the results from anything. The difference here 
    # is that you need to manage invalidation and you must adjust your code to check the cache before querying 
    # the main query store.
    # Most fo the time, you’ll want to go w/DAX if you’re using DyanmoDB as a data store. Otherwise, use 
    # ElastiCache.