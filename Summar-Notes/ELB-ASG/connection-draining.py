
# To allow for optimization, clients maintain a keep alive connection to the container service. This is so that 
# subsequent requests from that client can reuse the existing connection. When you want to stop traffic to a 
# container, you notify the load balancer. When you tell the load balancer to stop traffic to the container, it 
# periodically checks to see if the client closed the keep alive connection. The Amazon ECS agent monitors the 
# load balancer and waits the load balancer to report that the keep alive connection is closed.
# The amount of time that the load balancer waits is the deregistraion delay. You can configure the following 
# load balancer setting to speed up your deployments.
    # deregistration_delay.timeout_seconds: 300 (default)
# When you have a service with a response time that's under one second, set the parameter to the following value 
# to have the load balancer only wait five seconds before it breaks the connection between the client and the 
# backend service:
    # deregistration_delay.timeout_seconds: 5
# Connection draining only takes place after the LB receives no response from the application, then the 
# de-registration process begins. This ensures there are no requests that are broken.