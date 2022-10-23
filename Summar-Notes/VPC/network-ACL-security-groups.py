
# A network access control list (ACL) 
    # Allows or denies specific inbound or outbound traffic at the subnet level. You can use the default network 
    # ACL for your VPC, or you can create a custom network ACL for your VPC with rules that are similar to the rules 
    # for your security groups in order to add an additional layer of security to your VPC.
    # Fire walls
    # Can have Allow and Deny rules
    # Rules only include IP Addresses
    # Layer of control between the internet and subnet
    # Are at the subnet level
# Security Group
    # A security group controls the traffic that is allowed to reach and leave the resources that it is associated 
    # with. For example, after you associate a security group with an EC2 instance, it controls the inbound and 
    # outbound traffic for the instance.
    # You can specify allow rules, but not deny rules.
    # When you first create a security group, it has no inbound rules. Therefore, no inbound traffic is allowed until 
    # you add inbound rules to the security group.
    # When you first create a security group, it has an outbound rule that allows all outbound traffic from the resource. 
    # You can remove the rule and add outbound rules that allow specific outbound traffic only. If your security group 
    # has no outbound rules, no outbound traffic is allowed.
    # When you associate multiple security groups with a resource, the rules from each security group are aggregated 
    # to form a single set of rules that are used to determine whether to allow access.
    # When you add, update, or remove rules, your changes are automatically applied to all resources associated with 
    # the security group. The effect of some rule changes can depend on how the traffic is tracked.