

# The Amazon ECS container agent 
    # This allows container instances to connect to your cluster. The Amazon ECS container agent is included in 
    # the Amazon ECS-optimized AMIs, but you can also install it on any Amazon EC2 instance that supports the 
    # Amazon ECS specification. The Amazon ECS container agent is supported on Amazon EC2 instances and external 
    # instances (on-premises server or VM).
    # Connecting all the containers in the custer so they can interact with each other and share data
    # he Linux variants of the Amazon ECS-optimized AMI look for agent configuration data in the /etc/ecs/ecs.config 
    # file when the container agent starts. You can specify this configuration data at launch with Amazon EC2 user 
    # data.
    # #!/bin/bash
        # echo "ECS_CLUSTER=MyCluster" >> /etc/ecs/ecs.config
    # #!/bin/bash
        # cat <<'EOF' >> /etc/ecs/ecs.config
        # ECS_CLUSTER=MyCluster
        # ECS_ENGINE_AUTH_TYPE=docker
        # ECS_ENGINE_AUTH_DATA={"https://index.docker.io/v1/":{"username":"my_name","password":"my_password","email":"email@example.com"}}
        # ECS_LOGLEVEL=debug
        # EOF