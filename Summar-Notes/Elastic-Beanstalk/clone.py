


# Clone
    # You can use an existing Elastic Beanstalk environment as the basis for a new environment by cloning the 
    # existing environment. For example, you might want to create a clone so that you can use a newer version 
    # of the platform branch used by the original environment's platform. Elastic Beanstalk configures the clone 
    # with the same environment settings used by the original environment. By cloning an existing environment 
    # instead of creating a new environment, you don't have to manually configure option settings, environment 
    # variables, and other settings. Elastic Beanstalk also creates a copy of any AWS resource associated with 
    # the original environment. However, during the cloning process, Elastic Beanstalk doesn't copy data from 
    # Amazon RDS to the clone. After you create the clone environment, you can modify environment configuration 
    # settings as needed.
# 
    # You can only clone an environment to a different platform version of the same platform branch. A different 
    # platform branch isn't guaranteed to be compatible. To use a different platform branch, you have to manually 
    # create a new environment, deploy your application code, and make any necessary changes in code and options 
    # to ensure your application works correctly on the new platform branch.