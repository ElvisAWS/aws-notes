

# Access Point
    # Amazon S3 access points simplify data access for any AWS service or customer application that stores data in 
    # S3. Access points are named network endpoints that are attached to buckets that you can use to perform S3 
    # object operations, such as GetObject and PutObject. Each access point has distinct permissions and network 
    # controls that S3 applies for any request that is made through that access point. Each access point enforces 
    # a customized access point policy that works in conjunction with the bucket policy that is attached to the 
    # underlying bucket. You can configure any access point to accept requests only from a virtual private cloud 
    # (VPC) to restrict Amazon S3 data access to a private network.
    # You can only use access points to perform operations on objects. You can't use access points to perform other 
    # Amazon S3 operations, such as modifying or deleting buckets. Access points work with some, but not all, AWS 
    # services and features. For example, you can't configure Cross-Region Replication to operate through an access 
    # point
# Object Lambda
    # With S3 Object Lambda, you can add your own code to S3 GET, HEAD, and LIST requests to modify and process 
    # data as it is returned to an application. You can use custom code to modify the data returned by S3 GET 
    # requests to filter rows, dynamically resize images, redact confidential data, and much more. You can also 
    # use S3 Object Lambda to modify the output of S3 LIST requests to create a custom view of objects in a bucket 
    # and S3 HEAD requests to modify object metadata like object name and size. Powered by AWS Lambda functions, 
    # your code runs on infrastructure that is fully managed by AWS, eliminating the need to create and store 
    # derivative copies of your data or to run expensive proxies, all with no changes required to your applications.
    # S3 Object Lambda uses AWS Lambda functions to automatically process the output of a standard S3 GET, HEAD, 
    # and LIST request. With just a few clicks in the AWS Management Console, you can configure a Lambda function 
    # and attach it to an S3 Object Lambda Access Point. From that point forward, S3 will automatically call your 
    # Lambda function to process any data retrieved through the S3 Object Lambda Access Point, returning a transformed 
    # result back to the application. You can author and execute your own custom Lambda functions, tailoring S3 Object 
    # Lambda’s data transformation to your specific use case.