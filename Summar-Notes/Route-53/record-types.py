
# A record type
    # You use an A record to route traffic to a resource, such as a web server, using an IPv4 address in dotted 
    # decimal notation. e.g <Value>192.0.2.1</Value>
    # Maps a host name to an IPV4 address
# AAAA record type
    # Maps a host name to an IPV6 address
# CNAME record type
    # A CNAME record maps DNS queries for the name of the current record, such as acme.example.com, to another 
    # domain (example.com or example.net) or subdomain (acme.example.com or zenith.example.org). The DNS protocol 
    # does not allow you to create a CNAME record for the top node of a DNS namespace, also known as the zone apex. 
    # For example, if you register the DNS name example.com, the zone apex is example.com. You cannot create a CNAME 
    # record for example.com, but you can create CNAME records for www.example.com, newproduct.example.com, and so on.
    # In addition, if you create a CNAME record for a subdomain, you cannot create any other records for that subdomain. 
    # For example, if you create a CNAME for www.example.com, you cannot create any other records for which the value 
    # of the Name field is www.example.com.
# NS record type
    # An NS record identifies the name servers for the hosted zone. Note the following: The most common use for an 
    # NS record is to control how internet traffic is routed for a domain. To use the records in a hosted zone to 
    # route traffic for a domain, you update the domain registration settings to use the four name servers in the 
    # default NS record. (This is the NS record that has the same name as the hosted zone.) You can create a separate 
    # hosted zone for a subdomain (acme.example.com) and use that hosted zone to route internet traffic for the subdomain 
    # and its subdomains (subdomain.acme.example.com). You set up this configuration, known as "delegating responsibility 
    # for a subdomain to a hosted zone" by creating another NS record in the hosted zone for the root domain (example.com).
# Alias record type
    # Amazon Route 53 alias records are mapped internally to the DNS name of alias targets such as AWS resources. Route 53 
    # monitors the IP address associated with an alias target's DNS name for scaling actions and software updates. The 
    # authoritative response from Route 53 name servers contains an A record (for IPv4 addresses) or AAAA record (for IPv6 
    # addresses) with the IP address of the alias target.
    # They can are only of A or AAAA
    # TTL is set atomatically thus you can not set it
    # You can set an apex DNS name to point to a resource
    # You can't set an ALIAS record for an EC2 DNS name
    # Set yes to automatically evaluate health checks
# Hosted Zones
    # A hosted zone is a container for records, and records contain information about how you want to route traffic 
    # for a specific domain, such as example.com, and its subdomains (acme.example.com, zenith.example.com). A hosted 
    # zone and the corresponding domain have the same name. There are two types of hosted zones:
        # Public hosted zones contain records that specify how you want to route traffic on the internet
        # Private hosted zones contain records that specify how you want to route traffic in an Amazon VPC
# Time To Live
    # The amount of time, in seconds, that you want a DNS resolver to cache (store) the values for a record before 
    # submitting another request to Route 53 to get the current values for that record. If the DNS resolver receives 
    # another request for the same domain before the TTL expires, the resolver returns the cached value. A longer 
    # TTL reduces your Route 53 charges, which are based in part on the number of DNS queries that Route 53 responds 
    # to. A shorter TTL reduces the amount of time that DNS resolvers route traffic to older resources after you change 
    # the values in a record, for example, by changing the IP address for the web server for www.example.com.