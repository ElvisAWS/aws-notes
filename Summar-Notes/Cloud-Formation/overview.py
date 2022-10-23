

# CloudFormation
    # CloudFormation allows you to create and manage Amazon Web Services infrastructure deployments predictably and 
    # repeatedly. You can use CloudFormation to leverage Amazon Web Services products, such as Amazon Elastic Compute 
    # Cloud, Amazon Elastic Block Store, Amazon Simple Notification Service, Elastic Load Balancing, and Auto Scaling 
    # to build highly reliable, highly scalable, cost-effective applications without creating or configuring the 
    # underlying Amazon Web Services infrastructure.
    # With CloudFormation, you declare all your resources and dependencies in a template file. The template defines 
    # a collection of resources as a single unit called a stack. CloudFormation creates and deletes all member resources 
    # of the stack together and manages all dependencies between the resources for you.
    # Available Commands
        # activate-type
        # batch-describe-type-configurations
        # cancel-update-stack
        # continue-update-rollback
        # create-change-set
        # create-stack
        # create-stack-instances
        # create-stack-set
        # deactivate-type
        # delete-change-set
        # delete-stack
        # delete-stack-instances
        # delete-stack-set
        # deploy
        # deregister-type
        # describe-account-limits
        # describe-change-set
        # describe-change-set-hooks
        # describe-publisher
        # describe-stack-drift-detection-status
        # describe-stack-events
        # describe-stack-instance
        # describe-stack-resource
        # describe-stack-resource-drifts
        # describe-stack-resources
        # describe-stack-set
        # describe-stack-set-operation
        # describe-stacks
        # describe-type
        # describe-type-registration
        # detect-stack-drift
        # detect-stack-resource-drift
        # detect-stack-set-drift
        # estimate-template-cost
        # execute-change-set
        # get-stack-policy
        # get-template
        # get-template-summary
        # import-stacks-to-stack-set
        # list-change-sets
        # list-exports
        # list-imports
        # list-stack-instances
        # list-stack-resources
        # list-stack-set-operation-results
        # list-stack-set-operations
        # list-stack-sets
        # list-stacks
        # list-type-registrations
        # list-type-versions
        # list-types
        # package
        # publish-type
        # record-handler-progress
        # register-publisher
        # register-type
        # rollback-stack
        # set-stack-policy
        # set-type-configuration
        # set-type-default-version
        # signal-resource
        # stop-stack-set-operation
        # test-type
        # update-stack
        # update-stack-instances
        # update-stack-set
        # update-termination-protection
        # validate-template
        # wait
# Concept
    # Template
        # A CloudFormation template is simply a text file, formatted in a specific way, that defines how AWS services 
        # or resources should be configured and deployed.
    # Stacks
        # A stack is a term AWS uses to refer to a collection of multiple AWS resources -- such as EC2 virtual machines, 
        # S3 storage, and IAM access controls -- that you can manage together using a single template.
    # Formatting
        # CloudFormation supports templates that are formatted using either JSON or YAML. These are widely used file 
        # formats for structuring text files. Most other IaC tools use the same formatting languages, as do platforms like 
        # Kubernetes.
    # Parameters
        # If you need to apply unique settings for each deployment, you can do so using parameters. Parameters let you 
        # define custom values for each deployment that CloudFormation will apply at runtime.
    # Conditions
        # You can also fine-tune deployments by setting conditions, which let you define conditional rules to govern 
        # precisely how each deployment proceeds.
    # Change sets
        # If you want to update a deployment using CloudFormation, you can update the template you used to create the 
        # deployment. You can then create a change set, which summarizes the changes that the updated template will apply 
        # before making the change.
    # Functions
        # There are several ways to get data into a CloudFormation template, with parameters being the primary. But those 
        # parameters may not be known at deployment time. CloudFormation Functions allow CloudFormation Designers to 
        # retrieve data from resources deployed in the current CloudFormation or from external sources in the AWS account. 
        # Ref is used extensively to reference other resources inside the template like the example below. It creates an 
        # EIP for the instance created earlier in the template.

"""
AWSTemplateFormatVersion: 2010-09-09
Description: A sample template
Resources:
  MyEC2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      ImageId: ami-0ff8a91507f77f867
      InstanceType: t2.micro
      KeyName: testkey
      BlockDeviceMappings:
        - DeviceName: /dev/sdm
          Ebs:
            VolumeType: io1
            Iops: 200
            DeleteOnTermination: false
            VolumeSize: 20
"""