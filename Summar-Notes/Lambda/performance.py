

# Lambda Performance
    # From 128MB to 10GB in 1MB increament
    # Increase RAM if your application is CPU bound
    # U can only increase function CPU and not RAM
    # Default time out is 3 seconds and max is 900 seconds (15 min)
    # Always set timeout accordingly or else the function might run into an issue and run for a longer duration 
    # before throwing an error
# Lambda Concurrency and Throttling
    # Set a reserved concurrency at the function level
        # If invocation is synchronous => return throttleError 429
        # If invocation is asynchronous => retry then go to DLQ
            # return event to DLQ
            # Attempt to run function for up to 6 hours
            # retry interval increases exponentially from 1 sec after the first attempt to a max of 5 mins
    # Open support ticket if u need more than 1000 concurrency
