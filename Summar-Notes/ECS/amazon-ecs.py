

# Amazon ECS
    # Amazon Elastic Container Service (Amazon ECS) is a highly scalable and fast container management service. 
    # You can use it to run, stop, and manage containers on a cluster. With Amazon ECS, your containers are defined 
    # in a task definition that you use to run an individual task or task within a service. In this context, a service 
    # is a configuration that you can use to run and maintain a specified number of tasks simultaneously in a cluster. 
    # You can run your tasks and services on a serverless infrastructure that's managed by AWS Fargate. Alternatively, 
    # for more control over your infrastructure, you can run your tasks and services on a cluster of Amazon EC2 instances 
    # that you manage.
    # Launch Types
        # There are two models that you can use to run your containers:
            # Fargate launch type: This is a serverless pay-as-you-go option. You can run containers without needing 
            # to manage your infrastructure.
                # Large workloads that need to be optimized for low overhead
                # Small workloads that have occasional burst
                # Tiny workloads
                # Batch workloads
                    # No infastructure to provision
                    # Create task definitions
                    # AWS will run ECS Tasks for you based on the CPU/RAM you need
                    # To scale, just increase the number of tasks
            # EC2 launch type - Configure and deploy EC2 instances in your cluster to run your containers.
                # Workloads that require consistently high CPU core and memory usage
                # Large workloads that need to be optimized for price
                # Your applications need to access persistent storage
                # You must directly manage your infrastructure
                    # Create an EC2 Instance Profile
                        # This will be used by the ECS agent
                        # To make API calls to ECS service
                        # Send container logs to CloudWatch Logs
                        # Pull Docker image from ECR
                        # Reference sensitive data in Secrets Manager or SSM Parameter Store
                    # ECS Task Role
                        # Allows each task to have a specific role
                        # This different roles will connect to different AWS services
                        # Task Role is defined in the Task Definition
                    # ECS ELB
                        # You can connect an ELB infront of your ECS tasks
                    # Data Volumes (EFS)
                        # Mount EFS file systems onto ECS tasks
                        # Works for both EC2 and Fargate launch types
                        # This will connect tasks running in different AZ's so they can share data
                        # S3 cannot be used as a file system for ECS tasks
    # ECS Service Auto-Scaling for ECS Tasks
        # We can use AWS application auto-scaling
            # We can use ECS Service Average CPU Utilization metrics
            # We can use ECS Service memory utilization (RAM) Utilization metrics
            # ALB request count per Target (Metrics coming from the ALB)
        # We can then use the below to scale
            # Target Tracking: scale based on target value for a specific CloudWatch Metrics
            # Step Scaling: scale based on a specified CloudWatch Alarm
            # Scheduled Scaling: scale based on date/time
    # ECS Service Auto-Scaling for EC2 Instances
        # Auto scaling group scaling
            # Scale ur ASG based on CPU utilization
            # Add EC2 instances over time
        # ECS Cluster Capacity provider
            # Used to automatically scale the infastructure for ur ECS tasks
            # Paired with an ASG
            # Add's EC2 instances when u are missing CPU or RAM
    # Updating an ECS service (Rolling updates)
        # Min 50% max 100% healthy percentages 4 tasks
            # Terminate 2 keep two running, create 2 new with latest updates
            # Terminate the 2 old instances, keep the 2 new then create 2 new with latest updates
        # Min 100% max 150% healthy percentages 4 tasks
            # We need to create 2 new tasks to get at 150 max capacity
            # Terminate 2 and we are back at 100% capacity, create 2 with new updates and we are back at 150
            # repeat the process untill we are complete with rolling updates