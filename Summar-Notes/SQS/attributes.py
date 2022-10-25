
# Asynchronous communication between the appications and the middle ware (decoupled layer)
# Producers send messages to the SQS Queue, we can have many producers
# Consumers pull messgaes from the SQS Queue, we can have many consumers, and they delete the message after
# consuming
# Ulimitted throughput ie send as many messages as you want and no limmit of messages in the queue
# Each message has a 4 days default life span and max of 14 days
# We can schedule between 1 min and 14 days
# 10 ms of latency
# Limitation of 256kb per message sent
# Can have duplicate messages sometimes the producers might deliver a message twice)
# Can have out of order messaging
# Producers use SDK wth SendMessage API to send messages into the queue
# Consumers may receive a max of 10 messages at a time
# Consumers can process messgaes in paraallel
# Consumer deletes messages from the queue using DeleteMessageAPI
# Consumers can use metrix (CloudWatch Mtrix-Queue length: ApproximateNumberOf Messages) to scale up 
# worker instances setting up an alram.
# Encryption in flight by using HTTPS
# Server side encryption using KMS Keys
# IAM policies for access control