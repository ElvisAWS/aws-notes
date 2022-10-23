

# Amazon Athena 
    # Is an interactive query service that makes it easy to analyze data directly from Amazon S3 using standard SQL. 
    # Athena is serverless, so there is no infrastructure to set up or manage and you can start analyzing your data 
    # immediately. You don’t even need to load your data into Athena, or have complex ETL processes.  Athena works 
    # directly with data stored in S3.
    # Athena uses Presto, a distributed SQL engine to run queries. It also uses Apache Hive to create, drop, and 
    # alter tables and partitions. You can write Hive-compliant DDL statements and ANSI SQL statements in the Athena 
    # query editor. You can also use complex joins, window functions and complex datatypes on Athena. Athena uses an 
    # approach known as schema-on-read, which allows you to project your schema on to your data at the time you execute 
    # a query. This eliminates the need for any data loading or ETL.