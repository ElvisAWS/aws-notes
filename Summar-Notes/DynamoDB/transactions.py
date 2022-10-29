

# DynamoDB transactions
    # If you’ve ever worked with DynamoDB, you may have noticed things get complicated when you need to create 
    # multiple all-or-nothing operations within and across tables. That’s why, in late 2018, Amazon introduced 
    # DynamoDB transactions.
    # DynamoDB transactions are used to support mission-critical applications that require an all-or-nothing 
    # approach, even if there’s a disruption to the system. They allow cloud engineers to implement complicated 
    # business logic into a single atomic transaction, which can be made up of multiple related tasks. This 
    # means they’re really useful for handling order fulfillment and management, processing financial transactions, 
    # or building multiplayer games.

    # Modes
        # Read Modes
            # Eventual consistency, Strong consistency and Transactional
        # Write modes
            # Transactional
        # Consumes 2x WCU and RCU 
    # Operations
        # TransactGetItems
        # TransactWriteItems

    # ACID
        # The concept of ACID transactions predates DynamoDB transactions by a couple of decades. But DynamoDB 
        # transactions can be ACID transactions. ACID is an (awesome) acronym used to describe four ideal properties 
        # of a database transaction. 
        # Atomic
            # Each transaction is treated as a single unit and cannot be partially completed – a critical ingredient 
            # to their all-or-nothing-ness.
        # Consistent
            # Transactions are valid and must leave the database in a valid state. This prevents databases from 
            # being corrupted or suffering from data integrity issues.
        # Isolated
            # Different transactions are not dependent on one another. Even if they’re treated in parallel or 
            # sequentially, the effect of the transactions are the same in the end.
        # Durable
            # A committed transaction will remain committed, because the data is written to disc and not just held 
            # in memory. So there will be no breakdown even in the event of a system failure, such as a power loss.
