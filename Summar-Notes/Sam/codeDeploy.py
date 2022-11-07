

# Codedeploy
    # Sam framework uses codedeploy to update Lambda
    # Sam is build on CloudFormation
    # Sam requires the transform and resource sections
    # commands
        # Sam build: Fetch dependencies and create local artifacts
        # Sam package: Package and upload to Amazon S3, generate CF template
        # Sam deploy: Deploy to cloudFormation
    # Use Sam Policy templates for IAM auth
    # Sam is integrated with CodeDeploy to do deploy to Lambda aliases

    # $ sam package --output-template-file packaged.yaml --s3-bucket {bucket_name} --debug Using SAM Template at /home/ec2-user/sam-app/.aws-sam/build/template.yaml
    # $ aws cloudformation package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket {my-bucket}