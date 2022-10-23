
# Unified CloudWatch agent
    # Collect internal system-level metrics from Amazon EC2 instances across operating systems. The metrics can include 
    # in-guest metrics, in addition to the metrics for EC2 instances. The additional metrics that can be collected are 
    # listed in Metrics collected by the CloudWatch agent.
    # Collect system-level metrics from on-premises servers. These can include servers in a hybrid environment as 
    # well as servers not managed by AWS.
    # Retrieve custom metrics from your applications or services using the StatsD and collectd protocols. StatsD is 
    # supported on both Linux servers and servers running Windows Server. collectd is supported only on Linux servers.
    # Collect logs from Amazon EC2 instances and on-premises servers, running either Linux or Windows Server.

# By default no logs from your EC2 instance will go to ClodWatch
# You need to run a CloudWatch agent on EC2 to push the log files you want
# Make sure IAM permissions are correct
# This log agent can be set-up on-premise as well
# The newer one is the Unified agent and can send both logs and events
# Easy to configure using SSM Parameter store


