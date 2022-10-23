


# Code-Build
    # AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and 
    # produces software packages that are ready to deploy. With CodeBuild, you don’t need to provision, manage, and 
    # scale your own build servers. CodeBuild scales continuously and processes multiple builds concurrently, so 
    # your builds are not left waiting in a queue.
    # Output logs can be stored in S3 and CloudWatch logs
    # Use Cloudwatch metrics to monitor build statistics
    # Use Cloudwatch events to detect failed builds and trigger notifications
    # Use Cloudwatch alarms to notify if you need "thresholds" for failures
    # Buildspec.yml is used as build file, stored at the root of the project
    # Codebuild stores artifacts in S3
    # Codebuild can cache artifacts in S3 for optimization during the build process
# Buildspec.yml
    # env-variables 
        # Store them as plain text at the begening of the file in the env section
        # Store variables in SMS Parameter Store
        # Store secrets in AWS Secrets Manager
    # Phases
        # Install
        # Pre_build
        # Build
        # Post_build
    # Artifacts
        # Load files in S3 (Encrypted using KMS)
    # Cache
        # Files to cache in S3 usually dependencies for optimization of the build process
# Typically, AWS CodeBuild cannot access resources in a VPC. To enable access, you must provide additional 
# VPC-specific configuration information in your CodeBuild project configuration. This includes the VPC ID, 
# the VPC subnet IDs, and the VPC security group IDs. VPC-enabled builds can then access resources inside your 
# VPC.