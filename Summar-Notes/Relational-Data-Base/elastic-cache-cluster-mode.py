# Replication: Redis (Cluster Mode Disabled) vs. Redis (Cluster Mode Enabled)
    # Redis (Cluster Mode Disabled)
        # A Redis (cluster mode disabled) cluster has a single shard, inside of which is a collection of Redis 
        # nodes; one primary read/write node and up to five secondary, read-only replica nodes. Each read 
        # replica maintains a copy of the data from the cluster's primary node. Asynchronous replication mechanisms 
        # are used to keep the read replicas synchronized with the primary. Applications can read from any node in 
        # the cluster. Applications can write only to the primary node. Read replicas improve read throughput and 
        # guard against data loss in cases of a node failure. You can use Redis (cluster mode disabled) clusters 
        # with replica nodes to scale your Redis solution for ElastiCache to handle applications that are 
        # read-intensive or to support large numbers of clients that simultaneously read from the same cluster.
    # Redis (Cluster Mode Enabled)
        # A Redis (cluster mode enabled) cluster is comprised of from 1 to 500 shards (API/CLI: node groups). 
        # Each shard has a primary node and up to five read-only replica nodes. The configuration can range from 
        # 90 shards and 0 replicas to 15 shards and 5 replicas, which is the maximum number or replicas allowed.
        # The node or shard limit can be increased to a maximum of 500 per cluster if the Redis engine version is 
        # 5.0.6 or higher. Each read replica in a shard maintains a copy of the data from the shard's primary. 
        # Asynchronous replication mechanisms are used to keep the read replicas synchronized with the primary. 
        # Applications can read from any node in the cluster. Applications can write only to the primary nodes. 
        # Read replicas enhance read scalability and guard against data loss. Data is partitioned across the 
        # shards in a Redis (cluster mode enabled) cluster.
