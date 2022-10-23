
# Your Application Load Balancer periodically sends requests to its registered targets to test their status. These 
# tests are called health checks. Each load balancer node routes requests only to the healthy targets in the enabled 
# Availability Zones for the load balancer. Each load balancer node checks the health of each target, using the 
# health check settings for the target groups with which the target is registered. After your target is registered, 
# it must pass one health check to be considered healthy. After each health check is completed, the load balancer 
# node closes the connection that was established for the health check. If a target group contains only unhealthy 
# registered targets, the load balancer routes requests to all those targets, regardless of their health status. 
# This means that if all targets fail health checks at the same time in all enabled Availability Zones, the load 
# balancer fails open. The effect of the fail-open is to allow traffic to all targets in all enabled Availability 
# Zones, regardless of their health status, based on the load balancing algorithm. Health checks do not support 
# WebSockets.

# HealthyThreshold:
    # The number of consecutive health checks successes required before moving the instance to the Healthy state.
    # Valid Range: Minimum value of 2. Maximum value of 10.
# Interval:
    # The approximate interval, in seconds, between health checks of an individual instance.
    # Valid Range: Minimum value of 5. Maximum value of 300.
# Target:
    # The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is 
    # one (1) through 65535.
# For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a HTTP:port;/;PathToPing; 
# grouping, for example "HTTP:80/weather/us/wa/seattle". In this case, a HTTP GET request is issued to the 
# instance on the given port and path. Any answer other than "200 OK" within the timeout period is considered 
# unhealthy. The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.
# Timeout:
    # The amount of time, in seconds, during which no response means a failed health check.
    # This value must be less than the Interval value.
# UnhealthyThreshold:
    # The number of consecutive health check failures required before moving the instance to the Unhealthy state.
