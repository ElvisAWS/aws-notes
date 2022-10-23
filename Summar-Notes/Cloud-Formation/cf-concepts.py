

# AWS CloudFormation template
    # An AWS CloudFormation template is a formatted text file in JSON or YAML language that describes your AWS 
    # infrastructure. To create, view and modify templates, you can use AWS CloudFormation Designer or any text 
    # editor tool. An AWS CloudFormation template consists of nine main objects:
        # Format version
            # Format version defines the capability of a template.
        # Description
            # Any comments about your template can be specified in the description.
        # Metadata
            # Metadata can be used in the template to provide further information using JSON or YAML objects.
        # Parameters
            # Templates can be customized using parameters. Each time you create or update your stack, parameters 
            # help you give your template custom values at runtime. 
        # Mappings
            # Mapping enables you to map keys to a corresponding named value that you specify in a conditional 
            # parameter. Also, you can retrieve values in a map by using the “Fn:: FindInMap” intrinsic function. 
        # Conditions
            # In a template, conditions define whether certain resources are created or when resource properties 
            # are assigned to a value during stack creation or updating. Conditions can be used when you want to 
            # reuse the templates by creating resources in different contexts. You can use intrinsic functions to 
            # define conditions. 
            # # In a template, during stack creation, all the conditions in your template are evaluated. Any 
            # resources that are associated with a true condition are created, and the invalid conditions are 
            # ignored automatically. 
        # Transform
            # Transform builds a simple declarative language for AWS CloudFormation and enables reuse of template 
            # components. Here, you can declare a single transform or multiple transforms within a template. 
        # Resources
            # Using this section, you can declare the AWS resource that you want to create and specify in the 
            # stack, such as an Amazon S3 bucket or AWS Lambda. 
        # Output
            # In a template, the output section describes the output values that you can import into other stacks 
            # or the values that are returned when you view your own stack properties. For example, for an S3 bucket 
            # name, you can declare an output and use the “Description-stacks” command from the AWS CloudFormation 
            # service to make the bucket name easier to find.

