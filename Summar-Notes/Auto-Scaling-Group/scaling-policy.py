
# Dynamic scaling scales the capacity of your Auto Scaling group as traffic changes occur.
# Amazon EC2 Auto Scaling supports the following types of dynamic scaling policies:
    # Target tracking scaling:
        # Increase and decrease the current capacity of the group based on a Amazon CloudWatch metric and a 
        # target value. It works similar to the way that your thermostat maintains the temperature of your home—you 
        # select a temperature and the thermostat does the rest. e.g CPU should stay at 40%
        # Metrics are the fundamental concept in CloudWatch. A metric represents a time-ordered set of data points 
            # that are published to CloudWatch. Think of a metric as a variable to monitor, and the data points as 
            # representing the values of that variable over time. For example, the CPU usage of a particular EC2 
            # instance is one metric provided by Amazon EC2. The data points themselves can come from any application 
            # or business activity from which you collect data.
    # Step scaling:
        # Increase and decrease the current capacity of the group based on a set of scaling adjustments, known 
        # as step adjustments, that vary based on the size of the alarm breach. CloudWatch alarm e.g CPU> 49% 
        # add 3 units
    # Simple scaling: 
        # Increase and decrease the current capacity of the group based on a single scaling adjustment, with a 
        # cooldown period between each scaling activity.
    # scheduled:
        # Anticipate a scaling based on known usage
        # Example increase max capacity to 10 at 20pm on Saturday
# If you are scaling based on a metric that increases or decreases proportionally to the number of instances in 
# an Auto Scaling group, we recommend that you use target tracking scaling policies. Otherwise, we recommend 
# that you use step scaling policies.
# With target tracking, an Auto Scaling group scales in direct proportion to the actual load on your application. 
# That means that in addition to meeting the immediate need for capacity in response to load changes, a target 
# tracking policy can also adapt to load changes that take place over time, for example, due to seasonal variations.
# By default, new Auto Scaling groups start without any scaling policies. When you use an Auto Scaling group 
# without any form of dynamic scaling, it doesn't scale on it own unless you set up scheduled scaling or 
# predictive scaling.
    # This uses machine scaling