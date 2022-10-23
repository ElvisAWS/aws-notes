

# x-ray
    # AWS X-Ray makes it easy for developers to analyze the behavior of their production, distributed applications 
    # with end-to-end tracing capabilities. You can use X-Ray to identify performance bottlenecks, edge case errors, 
    # and other hard to detect issues. X-Ray supports applications, either in development or in production, of any 
    # type or size, from simple asynchronous event calls and three-tier web applications to complex distributed 
    # applications built using a microservices architecture. This enables developers to quickly find and address 
    # problems in their applications and improve the experience for end users of their applications.
    # Traces
        # A trace ID tracks the path of a request through your application. A trace collects all the segments generated 
        # by a single request. That request is typically an HTTP GET or POST request that travels through a load 
        # balancer, hits your application code, and generates downstream calls to other AWS services or external 
        # web APIs. The first supported service that the HTTP request interacts with adds a trace ID header to the 
        # request, and propagates it downstream to track the latency, disposition, and other request data.
    # Segments
        # The compute resources running your application logic send data about their work as segments. A segment 
        # provides the resource's name, details about the request, and details about the work done. For example, 
        # when an HTTP request reaches your application, it can record the following data about:
            # The host – hostname, alias or IP address
            # The request – method, client address, path, user agent
            # The response – status, content
            # The work done – start and end times, subsegments
            # Issues that occur – errors, faults and exceptions, including automatic capture of exception stacks.
    # Subsegments
        # A segment can break down the data about the work done into subsegments. Subsegments provide more granular 
        # timing information and details about downstream calls that your application made to fulfill the original 
        # request. A subsegment can contain additional details about a call to an AWS service, an external HTTP API, 
        # or an SQL database. You can even define arbitrary subsegments to instrument specific functions or lines of 
        # code in your application.
    # Sampling
        # To ensure efficient tracing and provide a representative sample of the requests that your application 
        # serves, the X-Ray SDK applies a sampling algorithm to determine which requests get traced. By default, 
        # the X-Ray SDK records the first request each second, and five percent of any additional requests.
    # Annotations
        # When you instrument your application, the X-Ray SDK records information about incoming and outgoing requests, 
        # the AWS resources used, and the application itself. You can add other information to the segment document as 
        # annotations and metadata. Annotations and metadata are aggregated at the trace level, and can be added to any 
        # segment or subsegment.
        # Annotations are simple key-value pairs that are indexed for use with filter expressions. Use annotations 
        # to record data that you want to use to group traces in the console, or when calling the GetTraceSummaries 
        # API. X-Ray indexes up to 50 annotations per trace.
    # Metadata
        # Metadata are key-value pairs with values of any type, including objects and lists, but that are not indexed. 
        # Use metadata to record data you want to store in the trace but don't need to use for searching traces.
        # You can view annotations and metadata in the segment or subsegment details in the X-Ray console.
    # x-ray security
        # IAM for authorization
        # KMS for encryption at rest
    # x-ray daemon
        # The AWS X-Ray daemon is a software application that listens for traffic on UDP port 2000, gathers raw 
        # segment data, and relays it to the AWS X-Ray API. The daemon works in conjunction with the AWS X-Ray SDKs 
        # and must be running so that data sent by the SDKs can reach the X-Ray service.
        # On AWS Lambda and AWS Elastic Beanstalk, use those services' integration with X-Ray to run the daemon. 
        # Lambda runs the daemon automatically any time a function is invoked for a sampled request. On Elastic 
        # Beanstalk, use the XRayEnabled configuration option to run the daemon on the instances in your environment.
        # To run the X-Ray daemon locally, on-premises, or on other AWS services, download it, run it, and then give 
        # it permission to upload segment documents to X-Ray
        # Traces are sent to x-ray using the deamon to avoid throttling, the daemon sends traces in batches
        # Lambda
            #If X-Ray tracing is enabled for a service, Lambda automatically sends the data to X-Ray. The upstream 
            # service will sample the incoming requests, add a tracing header, and tell Lambda to send the trace data. 
            # This works for applications hosted on EC2 using X-Ray SDK.
        # BeanStalk
            # Elastic Beanstalk does not provide the X-Ray daemon on the Multicontainer Docker (Amazon ECS) platform.
            # You can use the console to turn on X-Ray integration
            # You can configure it in your application source code with a configuration file. Use the .ebextension file
            # Example .ebextensions/xray-daemon.config
                        # option_settings:
                        # aws:elasticbeanstalk:xray:
                        #     XRayEnabled: true
    # ECS and X-Ray Integration
        # ECS Cluster
            # We can install the deamon in each EC2 Instance as a single X-Ray Daemon container
            # We can install on each container app running on the EC2 instance as an X-Ray Sidecar
        # Fargate Cluster
            # This uses the X-Ray SideCar method
