

# Conditional writes
    # It ensures an item has not changed before you update or delete it
    # Optimistic locking is a strategy to ensure that the client-side item that you are updating (or deleting) 
    # is the same as the item in Amazon DynamoDB. If you use this strategy, your database writes are protected 
    # from being overwritten by the writes of others, and vice versa.
    # With optimistic locking, each item has an attribute that acts as a version number. If you retrieve an item 
    # from a table, the application records the version number of that item. You can update the item, but only if 
    # the version number on the server side has not changed. If there is a version mismatch, it means that someone 
    # else has modified the item before you did. The update attempt fails, because you have a stale version of 
    # the item. If this happens, you simply try again by retrieving the item and then trying to update it. 
    # Optimistic locking prevents you from accidentally overwriting changes that were made by others. It also 
    # prevents others from accidentally overwriting your changes.