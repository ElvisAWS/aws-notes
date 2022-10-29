

# DynamoDB Local Secondary Index (LSI)
    # Alternative sirt key
    # Up to 5 per table
    # Must be defined at table creation
    # Can contain some or all attributes of the table

    # Local Secondary Indexes use the same hash key as the primary index but allow you to use a different sort key. 
    # That also means that they can be created only on tables with composite primary key.
    # Limit you to only 10GB of data per Hash/Partition Key.
    # Unlike GSIs, they share throughput with base table - if you query for data using LSI, the usage will be calculated 
    # against capacity of the underlying table and its base index.
    # They have to be specified at table creation - you can't add or remove them after provisioning the table.
# DynamoDB Global Secondary Index (GSI)
    # Alternative primary key
    # Can contain some or all attributes of the table
    # They can be modified after table creation
    # They need their own provisioned RCU and WCU
    # Even if the WCU of the main table are ok, throttling on the GSI will throttle the main table

    # Global Secondary Keys are much more flexible and don't have LSI limitations. They don't have to share the same 
    # hash key, and they can also be created on a table with a simple key schema. Most of the time, you'll find yourself 
    # using GSIs over LSIs because they enable much more flexible query access patterns.
    # Moreover, GSIs:
    # Don't have that 10GB of data per Hash/Partition Key limit like LSIs have.
    # Global Secondary Indexes don't have to be unique! Two items can have the same partition and sortkey pair on a GSI.
    # They don't share throughput with the base table. Each of the GSIs is billed independently, and throttling is also 
    # separated as a consequence.
    # GSIs can be altered after the table has been created. You can add and delete them whenever you want. Moreover, 
    # if you create GSI on the attribute already defined in a collection of items, the index will also be backfilled 
    # with that data.
    # They are eventually consistent - if you're writing an item to a table, it is asynchronously propagated to the 
    # rest of GSIs. It means that query results might sometimes not be consistent and you should be aware of that when 
    # creating your application. However, if you want to get the most up-to-date data, you can use "Strongly Consistent 
    # Reads". They cost x2 more, they might have a little bit bigger latency and you cannot use them on GSIs but they are 
    # reflecting the most accurate state of the database.