
# An Auto Scaling group contains a collection of EC2 instances that are treated as a logical grouping for the 
# purposes of automatic scaling and management. An Auto Scaling group also lets you use Amazon EC2 Auto Scaling 
# features such as health check replacements and scaling policies. Both maintaining the number of instances in 
# an Auto Scaling group and automatic scaling are the core functionality of the Amazon EC2 Auto Scaling service.
# The size of an Auto Scaling group depends on the number of instances that you set as the desired capacity. 
# You can adjust its size to meet demand, either manually or by using automatic scaling.
# An Auto Scaling group starts by launching enough instances to meet its desired capacity. It maintains this 
# number of instances by performing periodic health checks on the instances in the group. The Auto Scaling group 
# continues to maintain a fixed number of instances even if an instance becomes unhealthy. If an instance becomes 
# unhealthy, the group terminates the unhealthy instance and launches another instance to replace it.
# You can use scaling policies to increase or decrease the number of instances in your group dynamically to meet 
# changing conditions. When the scaling policy is in effect, the Auto Scaling group adjusts the desired capacity 
# of the group, between the minimum and maximum capacity values that you specify, and launches or terminates the 
# instances as needed. You can also scale on a schedule.
# Desired capacity: 
    # Represents the initial capacity of the Auto Scaling group at the time of creation. An Auto Scaling group 
    # attempts to maintain the desired capacity. It starts by launching the number of instances that are specified 
    # for the desired capacity, and maintains this number of instances as long as there are no scaling policies 
    # or scheduled actions attached to the Auto Scaling group.
# Minimum capacity: 
    # Represents the minimum group size. When scaling policies are set, an Auto Scaling group cannot 
    # decrease its desired capacity lower than the minimum size limit.
# Maximum capacity: 
    # Represents the maximum group size. When scaling policies are set, an Auto Scaling group cannot increase its 
    # desired capacity higher than the maximum size limit.