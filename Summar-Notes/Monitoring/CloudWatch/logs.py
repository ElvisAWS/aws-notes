

# Logs
    # You can use Amazon CloudWatch Logs to monitor, store, and access your log files from Amazon Elastic Compute 
    # Cloud (Amazon EC2) instances, AWS CloudTrail, Route 53, and other sources.
    # CloudWatch Logs enables you to centralize the logs from all of your systems, applications, and AWS services 
    # that you use, in a single, highly scalable service. You can then easily view them, search them for specific 
    # error codes or patterns, filter them based on specific fields, or archive them securely for future analysis. 
    # CloudWatch Logs enables you to see all of your logs, regardless of their source, as a single and consistent 
    # flow of events ordered by time, and you can query them and sort them based on other dimensions, group them 
    # by specific fields, create custom computations with a powerful query language, and visualize log data in 
    # dashboards.
    # Log Groups > Log streams > Log Lines
    # CloudWatch logs never expire by default
# CloudWatch log retention
    # You can change the log data retention setting for CloudWatch logs. By default, logs are kept indefinitely and 
    # never expire. You can adjust the retention policy for each log group, keeping the indefinite retention, or 
    # choosing a retention period between 10 years and one day. To view the allowed minimum retention period in 
    # AMS, see the AMS Technical Standards document available through AWS Artifact. To access AWS Artifact, contact 
    # your CSDM for instructions or go to Getting Started with AWS Artifact. The CloudWatch Logs log retention feature 
    # deletes the log events in a stream based on retention policy. It doesn't delete log streams or log groups.