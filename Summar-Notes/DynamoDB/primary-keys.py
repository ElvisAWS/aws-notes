

# Option 1: Primary key (HASH)
    # Partition key must be unique
    # Partition key must be diversed so that data is distributed
# Option 2: Primary + Sort key (HASH + RANGE)
    # The combination must be unique for each item
    # Data is grouped by partition key

    # NB Partition key must be unique just for option 1, but for option 2, the combination of Partition key plus
    # Sort keys must be unque