
# Versions
    # Each time you upload a new version of your application with the Elastic Beanstalk console or the EB CLI, 
    # Elastic Beanstalk creates an application version. If you don't delete versions that you no longer use, you 
    # will eventually reach the application version quota and be unable to create new versions of that application.
# lifecycle policy
    # A lifecycle policy tells Elastic Beanstalk to delete application versions that are old, or to delete 
    # application versions when the total number of versions for an application exceeds a specified number.
    # he application version quota applies across all applications in a region. If you have several applications, 
    # configure each application with a lifecycle policy appropriate to avoid reaching the quota. For example, if 
    # you have 10 applications in a region and the quota is 1,000 application versions, consider setting a lifecycle 
    # policy with a quota of 99 application versions for all applications, or set other values in each application 
    # as long as the total is less than 1,000 application versions. Elastic Beanstalk only applies the policy if the 
    # application version creation succeeds, so if you have already reached the quota, you must delete some versions 
    # manually prior to creating a new version.
    # By default, Elastic Beanstalk leaves the application version's source bundle in Amazon S3 to prevent loss of 
    # data. You can delete the source bundle to save space.