
# All Aurora instances have a share volume that is auto expanding from 10G to 128TB
# The master is the only that writes to the storage
# There is a writer endpoint connected from the client to the master for writes
# Incase of failover, the client connects to the new master using this writer endpoint
# The Reader Enpoint connects automatically to all the read replicas
# You can create a read-replica policy to scale if needed or auto-scaling
# Amazon Aurora (Aurora) is a fully managed relational database engine that's compatible 
# with MySQL and PostgreSQL
# Max 15 read replicas for Aurora
# Features
    # Automatic fail-over
    # Backup and recovery
    # Isolation and security
    # Industry compliance
    # Push-button scaling
    # Automated patching with zero down time
    # Advanced monitoring
    # Routine Maintenance
    # Backtrack: Stores data at any point intime without back-ups

# Amazon Aurora vs Amazon RDS
# Architecture Design
    # RDS architecture is similar to installing database engine on Amazon EC2 manually but leaving the provisioning 
    # and maintenance to AWS. RDS provides many features like automatic failover, backups, etc. RDS use Amazon EBS 
    # volumes for database and log storage. To achieve reliability, you need to enable the Multi-AZ feature on your 
    # RDS instance and replicate it synchronously to a standby replica in another Availability Zone.

    # Aurora database storage is reliable and fault-tolerant by design. Aurora’s database storage is separate from 
    # the instances. In Aurora, data has 6 copies (as 10GB chunks distributed) to three Availability Zones. Hence, 
    # even if you have only one Aurora instance, your data will still have 6 copies.
# Performance
    # RDS uses SSDs storage for better I/O throughput performance. You can choose between two SSD-backed storage 
    # options, that is, one that is optimized for high-performance OLTP applications and another one for cost-effective 
    # general-purpose use.

    # Aurora gives two times throughput performance provided by PostgreSQL or five times the throughput provided 
    # by standard MySQL running on similar hardware.
    # Aurora’s performance is higher and more consistent. Aurora writes logs directly to the storage without keeping 
    # log buffers. The replication to the replicas is asynchronous and for only cached data. Because the replicas 
    # also share the same storage cluster, the replica lag is small and consistent over time. Due to its unique 
    # storage design, Aurora’s performance stays consistent when the load increases.
# Availability and Durability
    # Aurora offers higher availability and better durability than RDS, due to its unique storage model, and ability 
    # to perform continuous backups and restore with a very low RPO (recovery point objective).
    # In Aurora, data is durable by design. You always have multiple copies of your data. Every Aurora cluster has 
    # six storage nodes, spread across three AZs, even if you have just one compute node. In RDS, you have to max 
    # out your read replicas for this level of durability.
# Resiliency
    # Aurora is more resilient than RDS because of its architecture design. It has fast recovery from failures. 
    # If a compute node crashes, Aurora can recover quickly. It can start new read replicas with minimal lag, and 
    # if the writer fails, another replica can be promoted to take over without waiting for the other nodes to 
    # reach consensus. All the shared state is in the data nodes, so failed nodes can be replaced almost immediately.
# Storage
    # RDS storage auto scaling automatically scales storage capacity up to 64 TiB (except SQL Server’s 16 TiB) in 
    # response to growing database workloads, with zero downtime. With RDS Storage Auto Scaling, you simply set 
    # your desired maximum storage limit, and Auto Scaling takes care of the rest.
    # Aurora automatically increases storage from a minimum of 10 GB to a maximum of 128 TiB. This is done in increments 
    # of 10 GB without any impact on the database performance. You are not required to provide the storage in advance.
# Scalability
    # Vertical Scaling: Both, Aurora and RDS, allow you to scale the memory and compute resources up and down, 
    # to a maximum of 244 GiB of RAM and 32 vCPUs. Scaling operations can be done within a few clicks.
    # Dynamic Scaling: Aurora Auto Scaling dynamically adjusts the number of Aurora Replicas provisioned for an 
    # Aurora DB cluster using single-master replication. It enables your Aurora DB cluster to handle sudden 
    # increases in connectivity or workload. When the connectivity or workload decreases, It removes unnecessary 
    # Aurora Replicas, so that you don’t pay for unused provisioned DB instances.
    # RDS does not support such Auto Scaling.
# Replication
    # RDS allows you to provision up to 5 replicas, and the process of replication is slower compared to Aurora.
    # Aurora allows you to provision up to 15 replicas, and the replication is done in milliseconds.
    # Aurora scales faster because it can add new read replicas quickly. Because replicas all use the shared 
    # storage volume, a new replica can serve queries almost immediately. It doesn’t have to wait to replicate 
    # data from the other nodes. Aurora does some asynchronous cache replication between nodes, but nothing 
    # synchronous. This reduces the inter-node I/O, which means Aurora can have more replicas.
# Failover
    # In RDS, Failover to read replica is done manually, which could lead to data loss. You can use Multi-AZ 
    # (Standby instance) feature for automatic failover, and to prevent downtime and data loss.
    # In Aurora, Failover to read replica is done automatically to prevent data loss. Failover time is faster 
    # on Aurora.
# Cluster Endpoints
    # In RDS, there is a cluster endpoint which you use for your write queries. It is the DNS endpoint pointing 
    # to your current master db instance. During a failover, RDS routes this endpoint to the new master by a 
    # simple DNS change. However, for read replicas, you have to balance the load in your application using the 
    # instance endpoints. RDS does not provide a load balancer for read replicas.
    # In Aurora, you still use cluster endpoint for your write queries. It also provides a reader endpoint 
    # acting as a load balancer for your read replicas. So you can use this endpoint for your read queries. In 
    # the case of a failover, one of the read replicas become master and is removed from this reader set.
# Backup
    # RDS creates and saves automated backups of your DB instance during the backup window of your DB instance. 
    # RDS creates a storage volume snapshot of your DB instance, backing up the entire DB instance and not just 
    # individual databases according to the backup retention period that you specify. If necessary, you can 
    # recover your database to any point in time during the backup retention period. While the snapshot is being 
    # taken, storage I/O may be interrupted while data is copied, affecting database performance.
    # Aurora backs up your cluster volume automatically and retains restore data for the length of the backup 
    # retention period. Aurora backups are continuous and incremental so you can quickly restore to any point 
    # within the backup retention period. No performance impact or interruption of database service occurs as 
    # backup data is being written.
    # For both, Backups are stored in Amazon S3.