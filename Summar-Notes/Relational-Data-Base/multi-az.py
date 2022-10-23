
# Multi-AZ deployments can have one standby or two standby DB instances. When the deployment has one standby DB 
# instance, it's called a Multi-AZ DB instance deployment. A Multi-AZ DB instance deployment has one standby DB 
# instance that provides failover support, but doesn't serve read traffic. When the deployment has two standby 
# DB instances, it's called a Multi-AZ DB cluster deployment. A Multi-AZ DB cluster deployment has standby DB 
# instances that provide failover support and can also serve read traffic.
# There is just one DNS name and incase of failover, the application connects automatic to the stand-by RDS
# You do not need to stop the instance to switch to multi-AZ. All you need to do is click on 'Modify' on the UI
# Multi-AZ DB instance deployment
    # A Multi-AZ DB instance deployment has the following characteristics:
    # There is only one row for the DB instance.
    # The value of Role is Instance or Primary.
    # The value of Multi-AZ is Yes.
# A Multi-AZ DB cluster deployment
    # A Multi-AZ DB cluster deployment has the following characteristics:
    # There is a cluster-level row with three DB instance rows under it.
    # For the cluster-level row, the value of Role is Multi-AZ DB cluster.
    # For each instance-level row, the value of Role is Writer instance or Reader instance.
    # For each instance-level row, the value of Multi-AZ is 3 Zones.
