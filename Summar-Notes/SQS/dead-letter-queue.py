

# This queue can be enabled on the console
# if a consumer can not process a message, the message goes back into the queue
# This can go on and on if the message has a problem i.e a no ending loop of reading and back in the queue
# The MaximumReceives thresh hold can be set and the message will be moved into a dead letter queue
# This is were an application of someone can determine the cause of the read failure
# Always set the max retension period (14 days) for the dead letter queue to avoid messages from expiring
# Redrive
    # You can configure a dead-letter queue redrive to move standard unconsumed messages out of an existing 
    # dead-letter queue back to their source queues.
    # Amazon SQS supports dead-letter queue redrive only for standard queues in the Amazon SQS console.
    # Amazon SQS doesn't support filtering and modifying messages while redriving them from the dead-letter 
    # queue.
    # A dead-letter queue redrive task can run a maximum of 36 hours. Amazon SQS supports a maximum of 100 
    # active redrive tasks per account.
    # The redrive task resets the retention period. A new messageID and enqueueTime are assigned to redriven 
    # messages.