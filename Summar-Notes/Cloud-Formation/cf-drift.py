

# CloudFormation Drift
    # There may be cases where a resource's configuration has drifted from its intended configuration and you want 
    # to accept the new configuration as the intended configuration. In most cases, you would resolve the drift 
    # results by updating the resource definition in the stack template with a new configuration and then perform 
    # a stack update. However, if the new configuration updates a resource property that requires replacement, 
    # then the resource will be recreated during the stack update. If you want to retain the existing resource, you 
    # can use the resource import feature to update the resource and resolve the drift results without causing the 
    # resource to be replaced.
    # Resolving drift for a resource through an import operation consists of the following basic steps:
        # Add a DeletionPolicy attribute, set to Retain, to the resource. This ensures the existing resource is 
        # retained rather than deleted when it's removed from the stack.
        # Remove the resource from the template and run a stack update operation. This removes the resource from the 
        # stack, but doesn't delete it.
        # Describe the resource’s actual state in the stack template, and then import the existing resource back into 
        # the stack. This adds the resource back into the stack and resolves the property differences that were causing 
        # the drift results.