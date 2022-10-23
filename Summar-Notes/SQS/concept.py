

# Simple Queue Service
    # Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets 
    # you integrate and decouple distributed software systems and components. Amazon SQS offers common constructs 
    # such as dead-letter queues and cost allocation tags.
    # There are three main parts in a distributed messaging system: the components of your distributed system, 
    # your queue (distributed on Amazon SQS servers), and the messages in the queue.
    # In the following scenario, your system has several producers (components that send messages to the queue) 
    # and consumers (components that receive messages from the queue). The queue (which holds messages A through E) 
    # redundantly stores the messages across multiple Amazon SQS servers.
# Benefits of using Amazon SQS
    # Security
        # You control who can send messages to and receive messages from an Amazon SQS queue. You can choose to 
        # transmit sensitive data by protecting the contents of messages in queues by using default Amazon SQS 
        # managed server-side encryption (SSE), or by using custom SSE keys managed in AWS Key Management 
        # Service (AWS KMS).
    # Durability
        # For the safety of your messages, Amazon SQS stores them on multiple servers. Standard queues support
        #  at-least-once message delivery, and FIFO queues support exactly-once message processing and 
        # high-throughput mode.
    # Availability
        # Amazon SQS uses redundant infrastructure to provide highly-concurrent access to messages and high 
        # availability for producing and consuming messages.
    # Scalability – Amazon SQS can process each buffered request independently, scaling transparently to handle 
    # any load increases or spikes without any provisioning instructions.
# Reliability
    # Amazon SQS locks your messages during processing, so that multiple producers can send and multiple consumers 
    # can receive messages at the same time.
# Customization
    # Your queues don't have to be exactly alike—for example, you can set a default delay on a queue. You can 
    # store the contents of messages larger than 256 KB using Amazon Simple Storage Service (Amazon S3) or 
    # Amazon DynamoDB, with Amazon SQS holding a pointer to the Amazon S3 object, or you can split a large 
    # message into smaller messages.

