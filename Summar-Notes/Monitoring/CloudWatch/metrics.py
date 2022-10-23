

# Metrics
    # You can push a metrics in the past and future
    # Use the PutMetricData API to send metrics to CloudWatch
    # aws cloudwatch put-metric-data --metric-name PageViewCount --namespace MyService --statistic-values Sum=11
    # ,Minimum=2,Maximum=5,SampleCount=3 --timestamp 2016-10-14T12:00:00.000Z

    # Metrics are data about the performance of your systems. By default, many services provide free metrics for 
    # resources (such as Amazon EC2 instances, Amazon EBS volumes, and Amazon RDS DB instances). You can also enable 
    # detailed monitoring for some resources, such as your Amazon EC2 instances, or publish your own application 
    # metrics. Amazon CloudWatch can load all the metrics in your account (both AWS resource metrics and application 
    # metrics that you provide) for search, graphing, and alarms. Metric data is kept for 15 months, enabling you 
    # to view both up-to-the-minute data and historical data.
    # Basic monitoring
        # Many AWS services offer basic monitoring by publishing a default set of metrics to CloudWatch with no charge 
        # to customers. By default, when you start using one of these AWS services, basic monitoring is automatically 
        # enabled
    # Detailed monitoring
        # Detailed monitoring is offered by only some services. It also incurs charges. To use it for an AWS service, 
        # you must choose to activate it. 
        # Detailed monitoring options differ based on the services that offer it. For example, Amazon EC2 detailed 
        # monitoring provides more frequent metrics, published at one-minute intervals, instead of the five-minute 
        # intervals used in Amazon EC2 basic monitoring. Detailed monitoring for Amazon S3 and Amazon Managed Streaming 
        # for Apache Kafka means more fine-grained metrics.
        # In different AWS services, detailed monitoring also has different names. For example, in Amazon EC2 it is 
        # called detailed monitoring, in AWS Elastic Beanstalk it is called enhanced monitoring, and in Amazon S3 it 
        # is called request metrics.
        # Using detailed monitoring for Amazon EC2 helps you better manage your Amazon EC2 resources, so that you can 
        # find trends and take action faster. 
    # CloudWatch Metrics Insights
        # CloudWatch Metrics Insights is a powerful high-performance SQL query engine that you can use to query your 
        # metrics at scale. You can identify trends and patterns within all of your CloudWatch metrics in real time.
        # You can perform a Metrics Insights query using the CloudWatch console, or by using GetMetricData or PutDashboard 
        # using the AWS CLI or the AWS SDKs. When you use the CloudWatch console, you can choose from a wide variety 
        # of pre-built sample queries and also create your own queries. With Metrics Insights you can run queries at 
        # scale. By using the GROUP BY clause, you can flexibly group your metrics in real time into separate time series 
        # per specific dimension value, based on your use cases. Because Metrics Insights queries include an ORDER BY 
        # ability, you can use Metrics Insights to make "Top N" type queries that can scan millions of metrics in 
        # your account, and return the top 10 most CPU consuming instances, for example, to help you pinpoint and remedy l
        # atency issues in your applications.
    # Custom metrics
        # You can publish your own metrics to CloudWatch using the AWS CLI or an API. You can view statistical graphs of 
        # your published metrics with the AWS Management Console. CloudWatch stores data about a metric as a series 
        # of data points. Each data point has an associated time stamp. You can even publish an aggregated set of data 
        # points called a statistic set.
        # High-resolution metrics
            # Metrics produced by AWS services are standard resolution by default. When you publish a custom metric, you 
            # can define it as either standard resolution or high resolution. When you publish a high-resolution metric, 
            # CloudWatch stores it with a resolution of 1 second, and you can read and retrieve it with a period of 1 
            # second, 5 seconds, 10 seconds, 30 seconds, or any multiple of 60 seconds.
            # f you set an alarm on a high-resolution metric, you can specify a high-resolution alarm with a period of 10 
            # seconds or 30 seconds, or you can set a regular alarm with a period of any multiple of 60 seconds. There is 
            # a higher charge for high-resolution alarms with a period of 10 or 30 seconds
        # Using dimensions
            # In custom metrics, the --dimensions parameter is common. A dimension further clarifies what the metric is 
            # and what data it stores. You can have up to 30 dimensions assigned to one metric, and each dimension is 
            # defined by a name and value pair.
            # How you specify a dimension is different when you use different commands. With put-metric-data, you specify 
            # each dimension as MyName=MyValue, and with get-metric-statistics or put-metric-alarm you use the format 
            # Name=MyName, Value=MyValue. For example, the following command publishes a Buffers metric with two dimensions 
            # named InstanceId and InstanceType.
            # aws cloudwatch put-metric-data --metric-name Buffers --namespace MyNameSpace --unit Bytes --value 231434333 --dimensions InstanceId=1-23456789,InstanceType=m1.small
        # Publishing single data points
            # To publish a single data point for a new or existing metric, use the put-metric-data command with one value 
            # and time stamp. For example, the following actions each publish one data point.