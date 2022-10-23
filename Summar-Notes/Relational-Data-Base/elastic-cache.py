# Elastic Cache: 
    # It comes as a fully managed solution that has the ability to deploy, manage, and scale a distributed in-memory 
    # cache environment in the cloud. Amazon describes it as a service that allows you to easily create, operate, and 
    # scale open-source compatible in-memory data stores within the cloud. Simply, this means that it eliminates the 
    # complexity associated with setting up and managing a distributed cache environment. The system itself is built 
    # to boost the performance of web-based applications by reducing the database load through the quick retrieval 
    # of data from high throughput and low latency in-memory data stores. As such, you can think of it as a 
    # high-performance caching system that facilitates demanding web applications requiring a quick response. That 
    # said, it’s worth noting that Amazon ElastiCache relies on two different caching engines — Memcached and Redis.
    # Make applications stateless by storing states of users in elastic cache
# Memcached
    # Multi-node for partitioning and sharding
    # No replication
    # No high availability
    # No persistent
    # No back-up and restore
    # Multi-threaded architecture
# Redis
    # Multi-AZ with fail-overs
    # Read Replicas
    # data durability
    # back-up and restore
    # looks like RDS