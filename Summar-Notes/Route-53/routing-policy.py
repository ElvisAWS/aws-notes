# AWS Route 53 routing policy determines how AWS would respond to the DNS queries and provides multiple routing 
# policy options.
# Simple Routing Policy
    # Does not allow for health checks
    # Can have two resources or IP addresses to route to.
    # Simple routing policy is a simple round-robin policy and can be applied when there is a single resource doing 
    # the function for the domain e.g. web server that serves content for the website.
    # Simple routing helps configure standard DNS records, with no special Route 53 routing such as weighted or latency.
    # Route 53 responds to the DNS queries based on the values in the resource record set e.g. IP address in an A record.
    # Simple routing does not allow the creation of multiple records with the same name and type, but multiple values can be 
    # specified in the same record, such as multiple IP addresses.
    # Route 53 displays all the values to resolve it recursively in random order and the resolver displays the values for the 
    # client. The client then chooses a value and resends the query.
    # Simple routing policy does not support health checks, so the record would be returned to the client even if it is unhealthy.
    # With Alias record enabled, only one AWS resource or one record can be specified in the current hosted zone.
# Weighted Routing Policy
    # Weighted routing policy helps route traffic to different resources in specified proportions (weights) e.g., 
    # 75% to one server and 25% to the other during a pilot release
    # Weighted routing policy can be applied when there are multiple resources that perform the same function e.g., 
    # webservers serving the same site
    # Weighted routing policy supports health checks.
# Latency-based Routing (LBR) Policy
    # Latency-based Routing Policy helps respond to the DNS query based on which data center gives the user the lowest 
    # network latency.
    # Latency-based routing policy can be used when there are multiple resources performing the same function and Route 
    # 53 needs to be configured to respond to the DNS queries with the resources that provide the fastest response with 
    # the lowest latency.
    # A latency resource record set can be created for the EC2 resource in each region that hosts the application. 
    # When Route 53 receives a query for the corresponding domain, it selects the latency resource record set for 
    # the EC2 region that gives the user the lowest latency. Route 53 then responds with the value associated with 
    # that resource record set for e.g., you might have web servers for example.com in the EC2 data centers in Ireland 
    # and in Tokyo. When a user browses example.com from Singapore, Route 53 will pick up the data center (Tokyo) 
    # which has the lowest latency from the user’s location
    # Latency between hosts on the Internet can change over time as a result of changes in network connectivity and 
    # routing. Latency-based routing is based on latency measurements performed over a period of time, and the 
    # measurements reflect these changes for e.g. if the latency from the user in Singapore to Ireland improves, the 
    # user can be routed to Ireland
    # Latency-based routing cannot guarantee users from the same geographic will be served from the same location for 
    # any compliance reason
    # Latency resource record sets can be created using any record type that Route 53 supports except NS or SOA.
    # Latency-based routing policy supports health checks.
# Failover Routing Policy
    # Failover routing policy allows active-passive failover configuration, in which one resource (primary) takes 
    # all traffic when it’s healthy and the other resource (secondary) takes all traffic when the first isn’t healthy.
    # Route 53 health checking agents will monitor each location/endpoint of the application to determine its availability.
    # Failover routing policy is applicable for Public hosted zones only.
# Geolocation Routing Policy
    # Geolocation routing policy helps respond to DNS queries based on the geographic location of the users i.e. 
    # location from which the DNS queries originate.
    # localization of content and presenting some or all of the website in the user’s language
    # restrict distribution of content to only the locations in which you have distribution rights.
    # balancing load across endpoints in a predictable, easy-to-manage way, so that each user location is consistently 
    # routed to the same endpoint.
    # Geolocation routing policy allows geographic locations to be specified by continent, country, or by state (only 
    # in the US)
    # Geolocation record sets, if created, for overlapping geographic regions for e.g. continent, and then for the country 
    # within the same continent, priority goes to the smallest geographic region, which allows some queries for a 
    # continent to be routed to one resource and queries for selected countries on that continent to a different resource
    # Geolocation works by mapping IP addresses to locations, which might not be mapped to an exact geographic location.
    # A default resource record set can be created to handle these queries and also the ones which do not have an explicit 
    # record set created.
# Geoproximity Routing Policy
    # The ability to shift traffic to resources based on bias
    # Helps when shifting traffic from one region to another
    # To change the size of the geographic region, specify bias values:
        # To expand (1 to 99) more traffic to the resource
        # To expand (-1 to -99) less traffic to the resource
    # Geoproximity routing helps route traffic to the resources based on the geographic location of the users and 
    # the resources.
    # Geoproximity routing can be configured with a bias to optionally choose to route more traffic or less to a given 
    # resource. A bias expands or shrinks the size of the geographic region from which traffic is routed to a resource.
    # Route 53 Traffic flow can be used to create Geoproximity routing flows.
    # Route 53 supports both the AWS region where the resource is created and the latitude and longitude of the resource.
# Multivalue Routing Policy
    # Multivalue routing helps return multiple values, e.g. IP addresses for the web servers, in response to DNS queries.
    # Multivalue routing also helps check the health of each resource, so only the values for healthy resources are returned.
    # Route 53 responds to DNS queries with up to eight healthy records and gives different answers to different DNS resolvers.
    # Multivalue answer routing is not a substitute for a load balancer, but the ability to return multiple health-checkable IP 
    # addresses is a way to use DNS to improve availability and load balancing.
    # To route traffic approximately randomly to multiple resources, such as web servers, one multivalue answer record can be 
    # created for each resource and, optionally, associate a Route 53 health check with each record. If a web server becomes unavailable after the resolver caches a response, client software can try another IP address in the response.