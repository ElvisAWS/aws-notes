
# EC2 instance health check
    # Amazon EC2 performs automated checks on every running EC2 instance to identify hardware and software issues.
    # Status checks are performed every minute and each returns a pass or a fail status.
    # Instance Status Checks: Monitor the software and network configuration of your individual instance. Amazon 
    # EC2 checks the health of an instance by sending an address resolution protocol (ARP) request to the ENI. 
    # These checks detect problems that require your involvement to repair.
# Elastic Load Balancer (ELB) health check
    # To discover the availability of your registered EC2 instances, a load balancer periodically sends pings, 
    # attempts connections, or sends requests to test the EC2 instances.
    # When configuring a health check, you would need to provide the following:
        # a specific port
        # protocol to use
        # a specific porting path
    # HTTP/HTTPS health check succeeds if the instance returns a 200 response code within the health check 
    # interval.
    # A TCP health check succeeds if the TCP connection succeeds.
    # An SSL health check succeeds if the SSL handshake succeeds.
# Auto Scaling and Custom health checks
    # All instances in your Auto Scaling group start in the healthy state. Instances are assumed to be healthy 
    # unless EC2 Auto Scaling receives notification that they are unhealthy. This notification can come from one 
    # or more of the following sources:
        # a specific portAmazon EC2 (default)
        # a specific portElastic Load Balancing
        # a specific portA custom health check.
    # After Amazon EC2 Auto Scaling marks an instance as unhealthy, it is scheduled for replacement. If you do 
    # not want instances to be replaced, you can suspend the health check process for any individual Auto 
    # Scaling group. If an instance is in any state other than running or if the system status is impaired, Amazon 
    # EC2 Auto Scaling considers the instance to be unhealthy and launches a replacement instance. If you attached 
    # a load balancer or target group to your Auto Scaling group,  Amazon EC2 Auto Scaling determines the health 
    # status of the instances by checking both the EC2 status checks and the Elastic Load Balancing health checks.
    # Amazon EC2 Auto Scaling waits until the health check grace period ends before checking the health status of 
    # the instance. Ensure that the health check grace period covers the expected startup time for your application.
    # Health check grace period does not start until lifecycle hook actions are completed and the instance enters 
    # the InService state. With custom health checks, you can send an instance’s health information directly from 
    # your system to Amazon EC2 Auto Scaling.