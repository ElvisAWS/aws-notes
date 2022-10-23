

# Amazon Elastic Container Registry (Amazon ECR) 
    # It is an AWS managed container image registry service that is secure, scalable, and reliable. Amazon ECR 
    # supports private repositories with resource-based permissions using AWS IAM. This is so that specified 
    # users or Amazon EC2 instances can access your container repositories and images. You can use your 
    # preferred CLI to push, pull, and manage Docker images, Open Container Initiative (OCI) images, and OCI 
    # compatible artifacts.
    # Authenticating with ECR
        # The get-login-password is the preferred method for authenticating to an Amazon ECR private registry 
        # when using the AWS CLI. 
        # aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
        # docker tag hello-world:latest aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository
        # docker push aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository
        # docker pull aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository:latest