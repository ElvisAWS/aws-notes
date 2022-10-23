

# We recommend that you assign a task an IAM role. Its role can be distinguished from the role of the Amazon EC2 
# instance that it's running on. Assigning each task a role aligns with the principle of least privileged access 
# and allows for greater granular control over actions and resources.
# When assigning IAM roles for a task, you must use the following trust policy so that each of your tasks can 
# assume an IAM role that's different from the one that your EC2 instance uses. This way, your task doesn't inherit 
# the role of your EC2 instance.

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

# You can manually retrieve the temporary role credentials from inside a container by appending the environment 
# variable to the IP address of the Amazon ECS container agent and running the curl command on the resulting 
# string.
# curl 192.0.2.0$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI
# The expected output is as follows:

{
	"RoleArn": "arn:aws:iam::123456789012:role/SSMTaskRole-SSMFargateTaskIAMRole-DASWWSF2WGD6",
	"AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
	"SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
	"Token": "IQoJb3JpZ2luX2VjEEM/Example==",
	"Expiration": "2021-01-16T00:51:53Z"
}

# Task execution role
    # The task execution role is used to grant the Amazon ECS container agent permission to call specific AWS API 
    # actions on your behalf. For example, when you use AWS Fargate, Fargate needs an IAM role that allows it to 
    # pull images from Amazon ECR and write logs to CloudWatch Logs. An IAM role is also required when a task 
    # references a secret that's stored in AWS Secrets Manager, such as an image pull secret.
# Amazon EC2 container instance role
    # The Amazon ECS container agent is a container that runs on each Amazon EC2 instance in an Amazon ECS cluster. 
    # It's initialized outside of Amazon ECS using the init command that's available on the operating system. 
    # Consequently, it can't be granted permissions through a task role. Instead, the permissions have to be assigned 
    # to the Amazon EC2 instances that the agents run on. The actions list in the example 
    # AmazonEC2ContainerServiceforEC2Role policy need to be granted to the ecsInstanceRole. If you don't do this, 
    # your instances cannot join the cluster.
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeTags",
                "ecs:CreateCluster",
                "ecs:DeregisterContainerInstance",
                "ecs:DiscoverPollEndpoint",
                "ecs:Poll",
                "ecs:RegisterContainerInstance",
                "ecs:StartTelemetrySession",
                "ecs:UpdateContainerInstancesState",
                "ecs:Submit*",
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}

# In this policy, the ecr and logs API actions allow the containers that are running on your instances to pull images 
# from Amazon ECR and write logs to Amazon CloudWatch. The ecs actions allow the agent to register and de-register 
# instances and to communicate with the Amazon ECS control plane. Of these, the ecs:CreateCluster action is optional.
# Iam roles are defined at the task definition level and used at the service level