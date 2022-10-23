# Amazon RDS uses the MariaDB, Microsoft SQL Server, MySQL, Oracle, and PostgreSQL DB engines' built-in replication 
# functionality to create a special type of DB instance called a read replica from a source DB instance. The source 
# DB instance becomes the primary DB instance. Updates made to the primary DB instance are asynchronously copied 
# to the read replica. You can reduce the load on your primary DB instance by routing read queries from your 
# applications to the read replica. Using read replicas, you can elastically scale out beyond the capacity constraints 
# of a single DB instance for read-heavy database workloads.
# When you create a read replica, you first specify an existing DB instance as the source. Then Amazon RDS takes 
# a snapshot of the source instance and creates a read-only instance from the snapshot. Amazon RDS then uses the 
# asynchronous replication method for the DB engine to update the read replica whenever there is a change to the 
# primary DB instance. The read replica operates as a DB instance that allows only read-only connections. Applications 
# connect to a read replica the same way they do to any DB instance. Amazon RDS replicates all databases in the 
# source DB instance.
# Read replicas can query only using the select statement
# Overview of Amazon RDS read replicas
    # Scaling beyond the compute or I/O capacity of a single DB instance for read-heavy database workloads. You 
    # can direct this excess read traffic to one or more read replicas.
    # Serving read traffic while the source DB instance is unavailable. In some cases, your source DB instance 
    # might not be able to take I/O requests, for example due to I/O suspension for backups or scheduled maintenance. 
    # In these cases, you can direct read traffic to your read replicas. For this use case, keep in mind that the 
    # data on the read replica might be "stale" because the source DB instance is unavailable.
    # Business reporting or data warehousing scenarios where you might want business reporting queries to run against 
    # a read replica, rather than your production DB instance.
    # Implementing disaster recovery. You can promote a read replica to a standalone instance as a disaster recovery 
    # solution if the primary DB instance fails.
# Promoting a read replica to be a standalone DB instance: You can promote a read replica into a standalone DB 
# instance. When you promote a read replica, the DB instance is rebooted before it becomes available. Replication is 
# asynchronous
    # Stop any transactions from being written to the primary DB instance, and then wait for all updates to be 
    # made to the read replica. Database updates occur on the read replica after they have occurred on the 
    # primary DB instance, and this replication lag can vary significantly. Use the Replica Lag metric to determine 
    # when all updates have been made to the read replica.
    # For MySQL and MariaDB only: If you need to make changes to the MySQL or MariaDB read replica, you must set 
    # the read_only parameter to 0 in the DB parameter group for the read replica. You can then perform all needed 
    # DDL operations, such as creating indexes, on the read replica. Actions taken on the read replica don't affect 
    # the performance of the primary DB instance.
    # Promote the read replica by using the Promote option on the Amazon RDS console, the AWS CLI command 
    # promote-read-replica, or the PromoteReadReplica Amazon RDS API operation.
    # The application must update the connection string to leverage read replicas
# Cross-Region replication costs
    # The data transferred for cross-Region replication incurs Amazon RDS data transfer charges. These cross-Region 
    # replication actions generate charges for the data transferred out of the source AWS Region:
# You can transform read-replicas to multi-AZ
# Max 5 read replicas for RDS
# Max 15 read replicas for Aurora