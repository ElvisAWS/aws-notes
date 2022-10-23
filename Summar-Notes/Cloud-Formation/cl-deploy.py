

# ClodFormation Deploy
    # Once your template is ready, you can begin the deployment process to create the resources you have defined in 
    # the template in your actual AWS environment. There are multiple ways to deploy a CloudFormation template. 
    # The approach you take will depend in part on how you created your template and in part on which AWS interface 
    # you prefer:
        # The AWS console
            # If your template is a text file stored on your local computer, the easiest way to deploy it is to log 
            # into the AWS CloudFormation console https://console.aws.amazon.com/cloudformation and click Create New 
            # Stack. The console will walk you through the steps for naming your template and uploading your computer's 
            # template file. Once you have completed the steps and reviewed your configuration, click the Create button 
            # to deploy your template.
        # From CloudFormation Designer
            # If you create your template in CloudFormation Designer, you can deploy it directly from there by clicking 
            # the Create Stack button, following the directions on the screen, and pressing Create when you are ready to 
            # apply the template.
        # The AWS CLI
            # Using the AWS CLI tool, you can use the aws cloudformation deploy command to deploy a template. Use 
            # command-line arguments to define where your template is stored (typically, you would upload it to S3 
            # first and point the CLI to that file) and other options you may want to configure.