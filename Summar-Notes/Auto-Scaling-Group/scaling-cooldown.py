
# After your Auto Scaling group launches or terminates instances, it waits for a cooldown period to end before 
# any further scaling activities initiated by simple scaling policies can start. The intention of the cooldown 
# period is to prevent your Auto Scaling group from launching or terminating additional instances before the 
# effects of previous activities are visible.
# Suppose, for example:
    # That a simple scaling policy for CPU utilization recommends launching two instances. Amazon EC2 Auto 
    # Scaling launches two instances and then pauses the scaling activities until the cooldown period ends. 
    # After the cooldown period ends, any scaling activities initiated by simple scaling policies can resume. 
    # If CPU utilization breaches the alarm high threshold again, the Auto Scaling group scales out again, and 
    # the cooldown period takes effect again. However, if two instances were enough to bring the metric value 
    # back down, the group remains at its current size.
# The default value for the Cooldown Period is 300 seconds (5 minutes).