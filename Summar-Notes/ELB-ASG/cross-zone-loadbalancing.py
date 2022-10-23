
# With cross-zone load balancing, (…) each load balancer node distributes requests evenly across the registered 
# instances in all enabled Availability Zones. If cross-zone load balancing is disabled, each load balancer node 
# distributes requests evenly across the registered instances in its Availability Zone only.
# Classic Load Balancer: 
    # With the API or CLI, cross-zone load balancing is disabled by default. With the AWS 
    # Management Console, the option to enable cross-zone load balancing is selected by default.

# Application Load Balancer: 
    # Cross-zone load balancing is always enabled

# Network Load Balancer: 
    # Cross-zone load balancing is disabled by default. You can enable or disable cross-zone load balancing at 
    # any time.