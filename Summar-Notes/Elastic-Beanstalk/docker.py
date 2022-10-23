


# Elastic Beanstalk supports the deployment of web applications from Docker containers. With Docker containers, 
# you can define your own runtime environment. You can also choose your own platform, programming language, and 
# any application dependencies, such as package managers or tools, which typically aren't supported by other 
# platforms. Docker containers are self contained and include all the configuration information and software that 
# your web application requires to run. All environment variables that are defined in the Elastic Beanstalk console 
# are passed to the containers.
# By using Docker with Elastic Beanstalk, you have an infrastructure that handles all the details of capacity 
# provisioning, load balancing, scaling, and application health monitoring. You can easily manage your web application 
# in an environment that supports the range of services that are integrated with Elastic Beanstalk.
# Docker running on Amazon Linux 2
    # This platform branch offers both single-container and multi-container support. Elastic Beanstalk deploys a 
    # Docker image and source code to EC2 instances on this platform branch. Use the Docker Compose tool on the 
    # Docker platform to simplify your application configuration, testing, and deployment.
    # Docker file for deploying application
# ECS running on 64bit Amazon Linux 2
    # This platform branch uses Amazon ECS to coordinate a deployment of multiple Docker containers to an Amazon 
    # ECS cluster in an Elastic Beanstalk environment. The instances in the environment each run the same set of 
    # containers, which are defined in a Dockerrun.aws.json file
    # Dockerrun.aws.json file contains the task definition