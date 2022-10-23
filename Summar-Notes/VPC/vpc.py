# VPC
    # Amazon VPC lets you provision a logically isolated section of the Amazon Web Services (AWS) cloud where you can 
    # launch AWS resources in a virtual network that you define. You have complete control over your virtual networking 
    # environment, including selection of your own IP address ranges, creation of subnets, and configuration of route 
    # tables and network gateways. You can also create a hardware Virtual Private Network (VPN) connection between your 
    # corporate datacenter and your VPC and leverage the AWS cloud as an extension of your corporate datacenter. You 
    # can easily customize the network configuration for your Amazon VPC. For example, you can create a public-facing 
    # subnet for your web servers that have access to the Internet, and place your backend systems such as databases or 
    # application servers in a private-facing subnet with no Internet access. You can leverage multiple layers of security, 
    # including security groups and network access control lists, to help control access to Amazon EC2 instances in each 
    # subnet.
# Subnets
    # A subnet is a range of IP addresses in your VPC. A subnet must reside in a single Availability Zone. After you 
    # add subnets, you can deploy AWS resources in your VPC.
    # There are public and private subnets
# IP addressing
    # You can assign IPv4 addresses and IPv6 addresses to your VPCs and subnets. You can also bring your public 
    # IPv4 and IPv6 GUA addresses to AWS and allocate them to resources in your VPC, such as EC2 instances, NAT gateways, 
    # and Network Load Balancers.
# Routing
    # Use route tables to determine where network traffic from your subnet or gateway is directed.
# Gateways and endpoints
    # A gateway connects your VPC to another network. For example, use an internet gateway to connect your VPC to the 
    # internet. Use a VPC endpoint to connect to AWS services privately, without the use of an internet gateway or NAT 
    # device.
    # Use a VPC endpoint gateway to connect your EC2 instance in a private subnet to your S3 or DynamoDB which are outside
    #  of the VPC probably in another VPC
    # Any time you want to privately connect to an AWS service, use VPC endpoint
# Nat Gateway
    # Manages internet connection between your AWS resources and the internet while keeping them private
    # The Nat is placed in the public subnet and receives trafffic from the internet gateway then routes traffic
    # to the private resources in the private subnet
# Nat Instance
    # Unlike NAT Gateway and Internet Gateway, a NAT Instance is not a special service offered by AWS. It is just 
    # a term for when using an EC2 instance to perform NAT Gateway-like functionality. It is similar to hosting database 
    # software on an EC2 instance rather than using Amazon RDS.
    # Because it is a self-managed instance, configuring routing, updating the software and operating system, and right-sizing 
    # instances is the responsibility of the owner. 
    # Similar to a NAT Gateway, a NAT Instance will need to be in a public subnet, and a private subnet will need a route 
    # to the NAT Instance to have internet access.
# Peering connections
    # Use a VPC peering connection to route traffic between the resources in two VPCs.
# Traffic Mirroring
    # Copy network traffic from network interfaces and send it to security and monitoring appliances for deep packet 
    # inspection.
# Transit gateways
    # Use a transit gateway, which acts as a central hub, to route traffic between your VPCs, VPN connections, and AWS 
    # Direct Connect connections.
# VPC Flow Logs
    # A flow log captures information about the IP traffic going to and from network interfaces in your VPC.
# VPN connections
    # Connect your VPCs to your on-premises networks using AWS Virtual Private Network (AWS VPN).
    # Site to Site VPN
        # Connects an on-premise VPN to AWS
        # Encrypted connection
        # Goes over the public network
    # Direct Connect
        # Physical connection between AWS and on-premise
        # private and secure
        # Private network

