

# Updating a CloudFormation Stack
    # There are two basic ways to make changes to a stack that you have deployed using a CloudFormation template.
        # Update template
            # Update the corresponding template, then immediately deploy the updated template using one of the 
            # deployment methods described above. This method is what AWS calls a direct update. It is the fastest 
            # but also the bluntest way to update your deployment. It does not provide a chance to view the impact 
            # of your intended changes before applying them.
        # Create Change set
            # This offers more control and the ability to preview changes before they take effect, creates a change 
            # set and uses it to make the updates. You can create a changeset in the CloudFormation console by selecting 
            # Stacks and then Stack actions. You can then select the template you want to update, and the console will 
            # then walk through the steps of changing your template, reviewing the changes, and applying them. You can 
            # also create a change set on the AWS CLI using the create-change-set command.