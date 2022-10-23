

# Load Balancing EC2 Launch Type
    # We get Dynamic Host Mapping if you define only the container port in the task definition
    # With dynamic host port mapping, the container ports keep changing
    # Do the set the host port on the task definition
    # thanks to the ECS service, the load balancer when connected can determine the changing container ports
    # hence can direct traffic to the containers
    # A classic load balancer will not work with this setup
    # You must allow from the EC2 instance SG any port from the ALB's security group
# Load balancer Fargate
    # Each task has a unique private IP address
    # Connected using an ENI
    # Each ENI is going to get same container port thus the ALB can connect to the containers on the port 80
    # Only the container port is defined, no host is applicable

# Port mapping
    # The challenge was , If you have a service with 2 containers (tasks), you need at least 2 ECS container 
    # instances because multiple containers can’t run on the same port on the same server, each container is 
    # hosted on a separate server. So in order to run multiple containers over the same container instance we 
    # need Dynamic port mapping !
    # Well , Dynamic port mapping allows you to run multiple tasks over the same host using multiple random host 
    # ports (in spite of defined host port).
    # Dynamic port mapping with an Application Load Balancer makes it easier to run multiple tasks on the same 
    # Amazon ECS service on an Amazon ECS cluster.With the Classic Load Balancer, you must statically map port 
    # numbers on a container instance. The Classic Load Balancer does not allow you to run multiple copies of a 
    # task on the same instance because the ports conflict. An Application Load Balancer uses dynamic port 
    # mapping so that you can run multiple tasks from a single service on the same container instance.