
# Source
# Build
# Test
# Deploy
    # Codedeploy, ElasticBeanstalk, cloudFormation, ECS, S3


# Code Pipeline
    # AWS CodePipeline is a fully managed continuous delivery service that helps you automate your release pipelines 
    # for fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and deploy 
    # phases of your release process every time there is a code change, based on the release model you define. This 
    # enables you to rapidly and reliably deliver features and updates. You can easily integrate AWS CodePipeline with 
    # third-party services such as GitHub or with your own custom plugin. 
    # Stages
        # A stage is a logical unit you can use to isolate an environment and to limit the number of concurrent 
        # changes in that environment. Each stage contains actions that are performed on the application artifacts. 
        # Your source code is an example of an artifact. A stage might be a build stage, where the source code is built 
        # and tests are run. It can also be a deployment stage, where code is deployed to runtime environments. Each 
        # stage is made up of a series of serial or parallel actions.
    # Actions
        # An action is a set of operations performed on application code and configured so that the actions run in the 
        # pipeline at a specified point. This can include things like a source action from a code change, an action for 
        # deploying the application to instances, and so on. For example, a deployment stage might contain a deployment 
        # action that deploys code to a compute service like Amazon EC2 or AWS Lambda.
    # Valid CodePipeline action types are source, build, test, deploy, approval, and invoke.
    # CloudWatchEvent is used to detect changes in code-piepline from codecommit
    # Actions can run in sequence and in parallel