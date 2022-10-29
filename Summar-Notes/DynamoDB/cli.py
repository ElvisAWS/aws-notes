


# DynamoDB CLI
    # --projection-expression
        # Specify attributes to retrieve
        # We want just a subset
    # --filter-expression
        # filter items before they are returned
    # pagination
        # --page-size:
            # Retrive the full list of items but making many api calls, each call will return items based on 
            # page to avoid time out due to large data retrieval default: 1000 items
        # --max-item
            # Maximum number of items to show in the CLI (returns NextToken)
        # --starting-token:
            # specifies the last token to retrieve the next set of items
