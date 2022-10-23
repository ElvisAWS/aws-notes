
# Elastic Load Balancing automatically distributes your incoming traffic across multiple targets, such as EC2 
# instances, containers, and IP addresses, in one or more Availability Zones. It monitors the health of its 
# registered targets, and routes traffic only to the healthy targets. Elastic Load Balancing scales your load 
# balancer capacity automatically in response to changes in incoming traffic.

# Application Load-Balancer
    # Choose an Application Load Balancer when you need a flexible feature set for your applications with HTTP 
    # and HTTPS traffic. Operating at the request level, Application Load Balancers provide advanced routing 
    # and visibility features targeted at application architectures, including microservices and containers.
    # Supports redirect
    # Supports routing (Parameter/Query string)
    # Supports target grouping
    # Fixed DNS or host name
    # Client IP-Address is inserted in header X-Forwarded-For
    # Port is inserted in header X-Forwarded-Port
    # Proto is inserted in header X-Forwarded-Proto
    # Clients can only see load balancer private ip
    # Application Load Balancers does notsupport both TCP
# Network Load-Balancer
    # Choose a Network Load Balancer when you need ultra-high performance, TLS offloading at scale, centralized 
    # certificate deployment, support for UDP, and static IP addresses for your applications. Operating at the 
    # connection level, Network Load Balancers are capable of handling millions of requests per second securely 
    # while maintaining ultra-low latencies.
    # Fixed DNS or host name plus static IPv4
    # Network Load Balancers support both TCP and UDP protocols.
# Gateway Loadbalancer
    # Choose a Gateway Load Balancer when you need to deploy and manage a fleet of third-party virtual appliances 
    # that support GENEVE. These appliances enable you to improve security, compliance, and policy controls.